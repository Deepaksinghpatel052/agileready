from account.models import AR_organization,Ar_user
from manage_backlogs.models import AR_BACKLOG
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from user_story_points.models import ArUserStoryPoints
from user_story_view.models import AR_USER_STORY,file_attachment
from manage_iterations.models import ArIterations
from manage_role.models import ArRole
from manage_goals.models import ArManageGoals
from manage_benefits.models import ArManageBenefits
import xlsxwriter
from datetime import date
import pathlib
import csv
import os
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from manage_product.models import AR_product
from ar_scenario.models import AR_SCENARIO
from django.db.models import Q
from django.shortcuts import render,get_object_or_404,redirect




def get_ar_scenario_data(org_ins,worksheet):
    if AR_USER_STORY.objects.filter(ORG_id=org_ins).exists():
        data = AR_USER_STORY.objects.filter(ORG_id=org_ins)
        worksheet.write('A1', "scenario_name")
        worksheet.write('B1', "scenario_desc")
        worksheet.write('C1', "product_id")
        worksheet.write('D1', "created_by")
        worksheet.write('E1', "created_dt")
        worksheet.write('F1', "updated_by")
        worksheet.write('G1', "updated_dt")
        worksheet.write('H1', "organization_name")
        i = 2
        for rows in data:
            worksheet.write('A' + str(i), str(rows.scenario_name))
            worksheet.write('B' + str(i), str(rows.scenario_desc))
            worksheet.write('C' + str(i), str(rows.product_id))
            worksheet.write('D' + str(i), str(rows.created_by))
            worksheet.write('E' + str(i), str(rows.created_dt))
            worksheet.write('F' + str(i), str(rows.updated_by))
            worksheet.write('G' + str(i), str(rows.updated_dt))
            worksheet.write('H' + str(i), str(rows.ORG_ID))

            i += 1
    return True



def get_ar_scenario_data_CSV(org_ins, file_name):
    if AR_SCENARIO.objects.filter(ORG_ID=org_ins).exists():
        data = AR_SCENARIO.objects.filter(ORG_ID=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ "scenario_name","scenario_desc","product_id","created_by","created_dt","updated_by","updated_dt","organization_name"])
            for rows in data:

                file_writer.writerow([str(rows.scenario_name), str(rows.scenario_desc),str(rows.product_id),str(rows.created_by),str(rows.created_dt),str(rows.updated_by),str(rows.updated_dt),str(rows.ORG_ID)])
    return True


def get_ar_scenario_data_CSV2(request,org_ins, file_name):

    # ======================================================
    filters = Q(ORG_ID=org_ins)

    if request.POST["product_list"] == "":
        pass
    else:
        product_list = request.POST["product_list"]

        if product_list == "none":
            filters = filters & Q(product_id__product_slug__exact=product_list) | Q(
                product_id__product_slug__isnull=True)
        else:
            filters = filters & Q(product_id__product_slug__exact=product_list)

    if AR_SCENARIO.objects.filter(filters).exists():
        data = AR_SCENARIO.objects.filter(filters).order_by("-id")
    # ======================================================
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ "scenario_name","scenario_desc","product_id","created_by","created_dt","updated_by","updated_dt","organization_name"])
            for rows in data:
                file_writer.writerow([str(rows.scenario_name), str(rows.scenario_desc),str(rows.product_id),str(rows.created_by),str(rows.created_dt),str(rows.updated_by),str(rows.updated_dt),str(rows.ORG_ID)])

    else:
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ "scenario_name","scenario_desc","product_id","created_by","created_dt","updated_by","updated_dt","organization_name"])
            # for rows in data:
            #     file_writer.writerow([str(rows.scenario_name), str(rows.scenario_desc),str(rows.product_id),str(rows.created_by),str(rows.created_dt),str(rows.updated_by),str(rows.updated_dt),str(rows.ORG_ID)])



    return True

