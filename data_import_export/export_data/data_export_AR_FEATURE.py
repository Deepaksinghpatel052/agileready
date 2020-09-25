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
import pathlib
import csv
import os



def get_ar_AR_FEATURE_data(org_ins,worksheet):
    if AR_FEATURE.objects.filter(ORG_ID=org_ins).exists():
        data = AR_FEATURE.objects.filter(ORG_ID=org_ins)
        worksheet.write('A1', "Feature_key")
        worksheet.write('B1', "Feature_desc")
        worksheet.write('C1', "Epic_Capanility")
        worksheet.write('C1', "User_story")
        worksheet.write('D1', "create_by")
        worksheet.write('E1', "create_dt")
        worksheet.write('F1', "update_by")
        worksheet.write('G1', "update_dt")
        worksheet.write('H1', "organization_name")
        i = 2
        for rows in data:
            worksheet.write('A' + str(i), str(rows.Feature_key))
            worksheet.write('B' + str(i), str(rows.Feature_desc))
            worksheet.write('B' + str(i), str(rows.CE_ID))
            worksheet.write('C' + str(i), str(list_to_string_user_story(rows.User_story.all())))
            worksheet.write('D' + str(i), str(rows.create_by))
            worksheet.write('E' + str(i), str(rows.create_dt))
            worksheet.write('F' + str(i), str(rows.update_by))
            worksheet.write('G' + str(i), str(rows.update_dt))
            worksheet.write('H' + str(i), str(org_ins))
            i += 1
    return True


def get_ar_AR_FEATURE_data_CSV(org_ins, file_name):
    if AR_FEATURE.objects.filter(ORG_ID=org_ins).exists():
        data = AR_FEATURE.objects.filter(ORG_ID=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["Feature_key", "Feature_desc","Epic_Capanility","User_story","create_by","create_dt","update_by","update_dt","organization_name"])
            for rows in data:
                file_writer.writerow([str(rows.Feature_key),str(rows.Feature_desc),str(rows.CE_ID),str(list_to_string_user_story(rows.User_story.all())),str(rows.create_by),str(rows.create_dt),str(rows.update_by), str(rows.update_dt),str(org_ins)])
    return True

def list_to_string_user_story(objcts):
    data = ""
    i=0
    for items in objcts:
        if i == 0:
            data = items.title
        else:
            data +="|"+str(items.title)
        i += 1
    return data