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



def get_ar_epic_capability_data(org_ins,worksheet):
    if AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).exists():
        data = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins)
        worksheet.write('A1', "Capability_key")
        worksheet.write('B1', "Capability_desc")
        worksheet.write('C1', "product")
        worksheet.write('D1', "created_by")
        worksheet.write('E1', "create_dt")
        worksheet.write('F1', "update_by")
        worksheet.write('G1', "update_dt")
        worksheet.write('H1', "organization_name")
        i = 2
        for rows in data:
            worksheet.write('A' + str(i), str(rows.Cepic_key))
            worksheet.write('B' + str(i), str(rows.Cepic_desc))
            worksheet.write('C' + str(i), str(list_to_string_project_name(rows.PROJECT_ID.all())))
            worksheet.write('D' + str(i), str(rows.created_by))
            worksheet.write('E' + str(i), str(rows.create_dt))
            worksheet.write('F' + str(i), str(rows.update_by))
            worksheet.write('G' + str(i), str(rows.update_dt))
            worksheet.write('H' + str(i), str(org_ins))
            i += 1
    return True


def get_ar_epic_capability_data_CSV(org_ins, file_name):
    if AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).exists():
        data = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ "Capability_key","Capability_desc","product", "created_by","create_dt","update_by","update_dt","organization_name"])
            for rows in data:
                file_writer.writerow([str(rows.Cepic_key),str(rows.Cepic_desc),str(list_to_string_project_name(rows.PROJECT_ID.all())),str(rows.created_by),str(rows.create_dt),str(rows.update_by),str(rows.update_dt),str(org_ins)])
    return True

def list_to_string_project_name(objcts):
    data = ""
    i=0
    for items in objcts:
        if i == 0:
            data = items.Product_name
        else:
            data +="|"+str(items.Product_name)
        i += 1
    return data