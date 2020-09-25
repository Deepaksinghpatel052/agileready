from account.models import AR_organization,Ar_user
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from manage_backlogs.models import AR_BACKLOG
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from user_story_points.models import ArUserStoryPoints
from user_story_view.models import AR_USER_STORY
from manage_iterations.models import ArIterations
from manage_role.models import ArRole
from manage_goals.models import ArManageGoals
from manage_benefits.models import ArManageBenefits
import xlsxwriter
from datetime import date
import pathlib
import csv
import os
from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect



def get_ArIterations_data(org_ins,worksheet):
    if ArIterations.objects.filter(ORG_ID=org_ins).exists():
        data = ArIterations.objects.filter(ORG_ID=org_ins)
        worksheet.write('A1', "IterationName")
        worksheet.write('B1', "owner")
        worksheet.write('C1', "StartDate")
        worksheet.write('D1', "EndDate")
        worksheet.write('E1', "Description")
        worksheet.write('F1', "Product")
        worksheet.write('G1', "Backlog")
        worksheet.write('H1', "UserStory")
        worksheet.write('I1', "Team")
        worksheet.write('J1', "IterationScore")
        worksheet.write('K1', "IterationSize")
        worksheet.write('L1', "create_by")
        worksheet.write('M1', "create_dt")
        worksheet.write('N1', "update_by")
        worksheet.write('O1', "update_dt")
        worksheet.write('P1', "IterationId")
        worksheet.write('Q1', "organization_name")
        i = 2
        for rows in data:
            score_and_size = get_storyes_scores_and_size(rows.UserStory.all())
            worksheet.write('A' + str(i), str(rows.IterationName))
            worksheet.write('B' + str(i), str(rows.owner))
            worksheet.write('C' + str(i), str(rows.StartDate))
            worksheet.write('D' + str(i), str(rows.EndDate))
            worksheet.write('E' + str(i), str(rows.Description))
            worksheet.write('F' + str(i), str(rows.Product))
            worksheet.write('G' + str(i), str(rows.Backlog))
            worksheet.write('H' + str(i), str(list_to_string_UserStory(rows.UserStory.all())))
            worksheet.write('I' + str(i), str(rows.Team))
            worksheet.write('J' + str(i), str(score_and_size[0]))
            worksheet.write('K' + str(i), str(score_and_size[1]))
            worksheet.write('L' + str(i), str(rows.create_by))
            worksheet.write('M' + str(i), str(rows.create_dt))
            worksheet.write('N' + str(i), str(rows.update_by))
            worksheet.write('O' + str(i), str(rows.update_dt))
            worksheet.write('P' + str(i), str(rows.IterationId))
            worksheet.write('Q' + str(i), str(org_ins))
            i += 1
    return True


def get_ArIterations_data_CSV(org_ins, file_name):
    if ArIterations.objects.filter(ORG_ID=org_ins).exists():
        data = ArIterations.objects.filter(ORG_ID=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["IterationName","owner","StartDate","EndDate","Description","Product","Backlog","UserStory","Team","IterationScore","IterationSize","create_by","create_dt","update_by","update_dt","IterationId","organization_name"])
            for rows in data:
                score_and_size = get_storyes_scores_and_size(rows.UserStory.all())
                file_writer.writerow([str(rows.IterationName),str(rows.owner),str(rows.StartDate),str(rows.EndDate),str(rows.Description),str(rows.Product),str(rows.Backlog),str(list_to_string_UserStory(rows.UserStory.all())),str(rows.Team),str(score_and_size[0]),str(score_and_size[1]),str(rows.create_by),str(rows.create_dt),str(rows.update_by),str(rows.update_dt),str(rows.IterationId),str(org_ins)])
    return True


def get_ArIterations_data_CSV2(request,org_ins, file_name):
    # ======================================================
    filters1 = Q(ORG_ID=org_ins)
    filters2 = Q(ORG_ID=org_ins)
    filters3 = Q(ORG_ID=org_ins)
    filters4 = Q(ORG_ID=org_ins)
    if request.POST["product_list"] == "":
        pass
    else:
        product_list = request.POST["product_list"]

        if product_list == "none":
            filters1 = filters1 & Q(Product__product_slug__exact=product_list) | Q(
                Product__product_slug__isnull=True)
        else:

            filters1 = filters1 & Q(Product__product_slug__exact=product_list)


        # filters = filters & Q(Product__product_slug__exact=product_list)

    if request.POST["team_list"] == "":
        pass
    else:
        team_list = request.POST["team_list"]

        if team_list == "none":
            filters2 = filters2 & Q(Team__team_slug__exact=team_list) | Q(
                Team__team_slug__isnull=True)
        else:
            filters2 = filters2 & Q(Team__team_slug__exact=team_list)

        # filters = filters & Q(Team__team_slug__exact=team_list)

    if request.POST["backlog_list"] == "":
        pass
    else:
        backlog_list = request.POST["backlog_list"]

        if request.GET['backlog-parent'] == "none":
            filters3 = filters3 & Q(Backlog__backlog_slug__exact=backlog_list) | Q(
                Backlog__backlog_slug__isnull=True)
        else:
            filters3 = filters3 & Q(Backlog__backlog_slug__exact=backlog_list)

        # filters = filters & Q(Backlog__backlog_slug__exact=backlog_list)

    if ArIterations.objects.filter(filters1).filter(filters2).filter(filters3).exists():
        data = ArIterations.objects.filter(filters1).filter(filters2).filter(filters3)
    # ======================================================
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["IterationName","owner","StartDate","EndDate","Description","Product","Backlog","UserStory","Team","IterationScore","IterationSize","create_by","create_dt","update_by","update_dt","IterationId","organization_name"])
            for rows in data:
                score_and_size = get_storyes_scores_and_size(rows.UserStory.all())
                file_writer.writerow([str(rows.IterationName),str(rows.owner),str(rows.StartDate),str(rows.EndDate),str(rows.Description),str(rows.Product),str(rows.Backlog),str(list_to_string_UserStory(rows.UserStory.all())),str(rows.Team),str(score_and_size[0]),str(score_and_size[1]),str(rows.create_by),str(rows.create_dt),str(rows.update_by),str(rows.update_dt),str(rows.IterationId),str(org_ins)])

    else:
        # ======================================================
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(
                ["IterationName", "owner", "StartDate", "EndDate", "Description", "Product", "Backlog", "UserStory",
                 "Team", "IterationScore", "IterationSize", "create_by", "create_dt", "update_by", "update_dt",
                 "IterationId", "organization_name"])

    return True


def get_storyes_scores_and_size(objects):
    get_score = 0
    get_size = 0
    get_count_of_storyes = len(objects)
    if len(objects) > 0 :
        for data in objects:
            if AR_USER_STORY.objects.filter(id=data.id).exists():
                get_user_storyes = get_object_or_404(AR_USER_STORY, pk=data.id)
                get_score += get_user_storyes.readiness_quality_score
                if get_user_storyes.story_points != None:
                    get_size += get_user_storyes.story_points.Point_score
        get_score = get_score / get_count_of_storyes
        get_size = get_size
        list_get = [get_score, get_size]
        return list_get
    else:
        get_score = 0
        get_size = 0
        list_get = [get_score,get_size]
        return  list_get



def list_to_string_UserStory(objcts):
    data = ""
    i = 0
    for items in objcts:
        if i == 0:
            data = items.title
        else:
            data += "|" + str(items.title)
        i += 1
    return data