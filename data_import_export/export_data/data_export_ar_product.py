from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from agileproject import settings
from manage_product.models import AR_team
from manage_product.models import AR_product
from account.models import AR_organization,Ar_user
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
from manage_product.templatetags import team_data
import pathlib
import csv
import os
from django.db.models import Q


def get_ar_product_data(org_ins,worksheet):
    if AR_product.objects.filter(ORG_ID=org_ins).exists():
        data = AR_product.objects.filter(ORG_ID=org_ins)
        worksheet.write('A1', "Product_name")
        worksheet.write('B1', "Product_description")
        worksheet.write('C1', "Team_parent")
        worksheet.write('D1', "Business_unit")
        worksheet.write('E1', "Product_size")
        worksheet.write('F1', "Product_score")
        worksheet.write('G1', "Children_Backlog_List")
        worksheet.write('H1', "US_quality_threshold")
        worksheet.write('I1', "organization_name")
        worksheet.write('J1', "create_by")
        worksheet.write('K1', "create_dt")
        worksheet.write('L1', "update_by")
        worksheet.write('M1', "update_dt")
        i = 2
        for rows in data:
            worksheet.write('A' + str(i), str(rows.Product_name))
            worksheet.write('B' + str(i), str(rows.Product_description))
            worksheet.write('C' + str(i), str(team_data.team_add(org_ins.id,rows.id)))
            worksheet.write('D' + str(i), str(rows.Business_unit))
            worksheet.write('E' + str(i), "Product_size")
            worksheet.write('F' + str(i), str(team_data.mul_add(org_ins.id,rows.id)))
            worksheet.write('G' + str(i), str(list_to_string_childiran_backlog(rows.backlog_by_product.all())))
            worksheet.write('H' + str(i), str(rows.US_quality_threshold))
            worksheet.write('I' + str(i), str(org_ins.organization_name))
            worksheet.write('J' + str(i), str(rows.create_by))
            worksheet.write('K' + str(i), str(rows.create_dt))
            worksheet.write('L' + str(i), str(rows.update_by))
            worksheet.write('M' + str(i), str(rows.update_dt))
            i += 1
    return True

def list_to_string_childiran_backlog(objcts):
    data = ""
    i=0
    for items in objcts:
        if i == 0:
            data = items.title
        else:
            data +="|"+str(items.title)
        i += 1
    return data



def get_ar_product_data_CSV(org_ins, file_name):
    if AR_product.objects.filter(ORG_ID=org_ins).exists():
        data = AR_product.objects.filter(ORG_ID=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["Product_name","Product_description","Team_parent","Business_unit","Product_size","Product_score","Children_Backlog_List","US_quality_threshold","organization_name","create_by","create_dt","update_by", "update_dt"])
            for rows in data:
                file_writer.writerow([str(rows.Product_name),str(rows.Product_description),str(team_data.team_add(org_ins.id,rows.id)),str(rows.Business_unit),"Product_size",str(team_data.mul_add(org_ins.id,rows.id)),str(list_to_string_childiran_backlog(rows.backlog_by_product.all())),str(rows.US_quality_threshold),str(org_ins.organization_name),str(rows.create_by),str(rows.create_dt),str(rows.update_by),str(rows.update_dt)])
    return True



def get_ar_product_data_CSV2(request,org_ins, file_name):
    # ======================================================




    # ======================================================

    filters1 = Q(ORG_ID=org_ins)
    filters2 = Q(ORG_ID=org_ins)
    filters3 = Q(ORG_ID=org_ins)
    filters4 = Q(ORG_ID=org_ins)
    filters_remove = ~Q(Product_name='None')
    # ----------------------------------------- Team filter--------------------------------
    if request.POST["team_list"] == "":
        pass
    else:
        team_list = request.POST["team_list"]

        # ------------------------------
        if team_list == "none":
            filter_team_ins = get_object_or_404(AR_team, team_slug=team_list, ORG_id=org_ins)
            QTB = Q(team_list=filter_team_ins)
            all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id").filter(
                ~Q(title='None'))
            result = []
            for data_back in all_backlog_get:
                result.append(data_back.product_parent.id)
            final_result_team = result
            # ----------------------------- -------------------------
            filters1 = filters1 & Q(id__in=final_result_team) | Q(backlog_by_product__isnull=True) & Q(
                ORG_ID=org_ins)

        else:

            filter_team_ins = get_object_or_404(AR_team, team_slug=team_list, ORG_id=org_ins)
            QTB = Q(team_list=filter_team_ins)
            all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id").filter(
                ~Q(title='None'))
            result = []
            for data_back in all_backlog_get:
                result.append(data_back.product_parent.id)
            final_result_team = result
            # ----------------------------- -------------------------
            filters1 = filters1 & Q(id__in=final_result_team)
        # ------------------------------
        #
        # filter_team_ins = get_object_or_404(AR_team, team_slug=team_list, ORG_id=org_ins)
        # QTB = Q(team_list=filter_team_ins)
        # all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id").filter(~Q(title='None'))
        # result = []
        # for data_back in all_backlog_get:
        #     result.append(data_back.product_parent.id)
        # final_result_team = result
        # filters = filters & Q(id__in=final_result_team)

    # ----------------------------------------- Backlog filter--------------------------------

    if request.POST["backlog_list"] == "":
        pass
    else:
        backlog_list = request.POST["backlog_list"]

        if backlog_list == "none":
            all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(
                backlog_slug=backlog_list).order_by("-id").filter(~Q(title='None'))
            result = []
            for data_back in all_backlog_get:
                result.append(data_back.product_parent.id)
            final_result_backlog = result
            filters2 = filters2 & Q(id__in=final_result_backlog) | Q(backlog_by_product__isnull=True) & Q(
                ORG_ID=org_ins)
        else:
            all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(
                backlog_slug=backlog_list).order_by("-id").filter(~Q(title='None'))
            result = []
            for data_back in all_backlog_get:
                result.append(data_back.product_parent.id)
            final_result_backlog = result
            filters2 = filters2 & Q(id__in=final_result_backlog)
        backlog_token = backlog_list
    # ----------------------------------------- Epic filter--------------------------------
    if request.POST["epic_capability_list"] == "":
        pass
    else:
        epic_capability_list = request.POST["epic_capability_list"]

        if epic_capability_list == "none":
            all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(
                epic_capability_slug=epic_capability_list).order_by("-id")
            got = ""
            for data_epic in all_epic_get:
                result = []
                got = ""
                for val in data_epic.PROJECT_ID.all():
                    got = val.id
                    result.append(got)
            final_result_epic = result

            filters3 = filters3 & Q(id__in=final_result_epic) | Q(epic_capability_product__isnull=True) & Q(
                ORG_ID=org_ins)
        else:

            all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(
                epic_capability_slug=epic_capability_list).order_by("-id")
            got = ""
            for data_epic in all_epic_get:
                result = []
                got = ""
                for val in data_epic.PROJECT_ID.all():
                    got = val.id
                    result.append(got)
            final_result_epic = result

            filters3 = filters3 & Q(id__in=final_result_epic)
        epic_capability_token = epic_capability_list

    # ----------------------------------------- Feature filter--------------------------------

    if request.POST["feature_list"] == "":
        pass
    else:
        feature_list = request.POST["feature_list"]

        if feature_list == "none":

            filter_feature_ins = get_object_or_404(AR_FEATURE, feature_slug=feature_list,
                                                   ORG_ID=org_ins)
            QTB = Q(epic_from_feature=filter_feature_ins)
            all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id")
            result = []
            for data_epic in all_epic_get:
                for val in data_epic.PROJECT_ID.all():
                    got = val.id
                    result.append(got)
            final_result_feature = result

            filters4 = filters4 & Q(id__in=final_result_feature) | Q(epic_capability_product__isnull=True) & Q(
                ORG_ID=org_ins)

        else:

            filter_feature_ins = get_object_or_404(AR_FEATURE, feature_slug=feature_list, ORG_ID=org_ins)
            QTB = Q(epic_from_feature=filter_feature_ins)
            all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id")
            result = []
            for data_epic in all_epic_get:
                for val in data_epic.PROJECT_ID.all():
                    got = val.id
                    result.append(got)
            final_result_feature = result

            filters4 = filters4 & Q(id__in=final_result_feature)
        feature_token = feature_list
    # ----------------------------------------- apply filter--------------------------------

    # return HttpResponse(filters)

    if AR_product.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).filter(filters_remove).exists():
        data = AR_product.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).filter(filters_remove).order_by("-id")


        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["Product_name","Product_description","Team_parent","Business_unit","Product_size","Product_score","Children_Backlog_List","US_quality_threshold","organization_name","create_by","create_dt","update_by", "update_dt"])
            for rows in data:
                file_writer.writerow([str(rows.Product_name),str(rows.Product_description),str(team_data.team_add(org_ins.id,rows.id)),str(rows.Business_unit),"Product_size",str(team_data.mul_add(org_ins.id,rows.id)),str(list_to_string_childiran_backlog(rows.backlog_by_product.all())),str(rows.US_quality_threshold),str(org_ins.organization_name),str(rows.create_by),str(rows.create_dt),str(rows.update_by),str(rows.update_dt)])
    else:
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["Product_name","Product_description","Team_parent","Business_unit","Product_size","Product_score","Children_Backlog_List","US_quality_threshold","organization_name","create_by","create_dt","update_by", "update_dt"])



    return True


