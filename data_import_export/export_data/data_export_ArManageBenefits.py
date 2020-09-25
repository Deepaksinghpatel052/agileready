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



def get_ArManageBenefits_data(org_ins,worksheet):
    if ArManageBenefits.objects.filter(ORG_ID=org_ins).exists():
        data = ArManageBenefits.objects.filter(ORG_ID=org_ins)
        worksheet.write('A1', "Benefits_id")
        worksheet.write('B1', "Benefits_title")
        worksheet.write('C1', "Benefits_description")
        worksheet.write('D1', "Use_in")
        worksheet.write('E1', "created_by")
        worksheet.write('F1', "created_dt")
        worksheet.write('G1', "updated_by")
        worksheet.write('H1', "updated_dt")
        worksheet.write('I1', "organization_name")
        i = 2
        for rows in data:
            worksheet.write('A' + str(i), str(rows.Benefits_id))
            worksheet.write('B' + str(i), str(rows.Benefits_title))
            worksheet.write('C' + str(i), str(rows.Benefits_description))
            worksheet.write('D' + str(i), str(rows.Use_in))
            worksheet.write('E' + str(i), str(rows.created_by))
            worksheet.write('F' + str(i), str(rows.created_dt))
            worksheet.write('G' + str(i), str(rows.updated_by))
            worksheet.write('H' + str(i), str(rows.updated_dt))
            worksheet.write('I' + str(i), str(org_ins))
            i += 1
    return True

def get_ArManageBenefits_data_CSV(org_ins, file_name):
    if ArManageBenefits.objects.filter(ORG_ID=org_ins).exists():
        data = ArManageBenefits.objects.filter(ORG_ID=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["Benefits_id","Benefits_title","Benefits_description","Use_in","created_by","created_dt","updated_by","updated_dt"])
            for rows in data:
                file_writer.writerow([str(rows.Benefits_id),str(rows.Benefits_title),str(rows.Benefits_description), str(rows.Use_in),str(rows.created_by),str(rows.created_dt),str(rows.updated_by),str(rows.updated_dt),str(org_ins)])
    return True