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


def get_ar_ArUserStoryPoints_data(org_ins,worksheet):
    if ArUserStoryPoints.objects.filter(ORG_ID=org_ins).exists():
        data = ArUserStoryPoints.objects.filter(ORG_ID=org_ins)
        worksheet.write('A1', "Point_Key")
        worksheet.write('B1', "Point_Description")
        worksheet.write('C1', "Point_score")
        worksheet.write('D1', "create_by")
        worksheet.write('E1', "create_dt")
        worksheet.write('F1', "update_by")
        worksheet.write('G1', "update_dt")
        worksheet.write('H1', "organization_name")
        i = 2
        for rows in data:
            worksheet.write('A' + str(i), str(rows.Point_Key))
            worksheet.write('B' + str(i), str(rows.Point_Description))
            worksheet.write('C' + str(i), str(rows.Point_score))
            worksheet.write('D' + str(i), str(rows.create_by))
            worksheet.write('E' + str(i), str(rows.create_dt))
            worksheet.write('F' + str(i), str(rows.update_by))
            worksheet.write('G' + str(i), str(rows.update_dt))
            worksheet.write('H' + str(i), str(org_ins.organization_name))
            i += 1
    return True


def get_ar_ArUserStoryPoints_data_CSV(org_ins, file_name):
    if ArUserStoryPoints.objects.filter(ORG_ID=org_ins).exists():
        data = ArUserStoryPoints.objects.filter(ORG_ID=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(["Point_Key", "Point_Description","Point_score","create_by","create_by","create_dt", "update_by","update_dt","organization_name"])
            for rows in data:
                file_writer.writerow([ str(rows.Point_Key),str(rows.Point_Description),str(rows.Point_score),str(rows.create_by),str(rows.create_dt),str(rows.update_by),str(rows.update_dt),str(org_ins.organization_name)])
    return True