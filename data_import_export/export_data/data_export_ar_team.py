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

def get_ar_team_data(org_ins,worksheet):
    if AR_team.objects.filter(ORG_id=org_ins).exists():
        data = AR_team.objects.filter(ORG_id=org_ins)

        worksheet.write('A1', "Team_name")
        worksheet.write('B1',"Team_description")
        worksheet.write('C1' , "organization_name")
        worksheet.write('D1', "Team_member_list")
        worksheet.write('E1', "create_by")
        worksheet.write('F1', "create_dt")
        worksheet.write('G1', "update_by")
        worksheet.write('H1', "update_dt")
        i = 2
        for rows in data:
            print(i)
            worksheet.write('A'+str(i), str(rows.Team_name))
            worksheet.write('B'+str(i), str(rows.Team_description))
            worksheet.write('C'+str(i), str(org_ins.organization_name))
            worksheet.write('D'+str(i), str(list_to_string_team_member(rows.Team_member_list.all())))
            worksheet.write('E'+str(i), str(rows.create_by))
            worksheet.write('F'+str(i), str(rows.create_dt))
            worksheet.write('G'+str(i), str(rows.update_by))
            worksheet.write('H'+str(i), str(rows.update_dt))
            i += 1
    return True



def get_ar_team_data_CSV(org_ins, file_name):
    if AR_team.objects.filter(ORG_id=org_ins).exists():
        data = AR_team.objects.filter(ORG_id=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ "Team_name","Team_description","organization_name", "Team_member_list","create_by","create_dt","update_by","update_dt"])
            for rows in data:
                file_writer.writerow([str(rows.Team_name),str(rows.Team_description),str(org_ins.organization_name),str(list_to_string_team_member(rows.Team_member_list.all())),str(rows.create_by),str(rows.create_dt),str(rows.update_by),str(rows.update_dt)])
    return True


def list_to_string_team_member(objcts):
    data = ""
    i=0
    for items in objcts:
        if i == 0:
            data = items.user_name
        else:
            data +="|"+str(items.user_name)
        i += 1
    return data
