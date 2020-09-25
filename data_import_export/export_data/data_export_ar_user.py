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

def get_user_name_by_id(user_id):
    userName = ""
    if str(user_id) == "0":
        userName = ""
    else:
        if Ar_user.objects.filter(id=user_id).exists():
            data = Ar_user.objects.get(id=user_id)
            userName = data.user_name
    return userName

def list_to_string_profile_permission(objcts):
    data = ""
    i = 0
    for items in objcts:
        if i == 0:
            data = items.profile_key
        else:
            data += "|" + str(items.profile_key)
        i += 1
    return data


def get_ar_user_data(org_ins, worksheet):
    if Ar_user.objects.filter(org_id=org_ins).exists():
        data = Ar_user.objects.filter(org_id=org_ins)
        worksheet.write('A1', "user_name")
        worksheet.write('B1', "address")
        worksheet.write('C1', "email")
        worksheet.write('D1', "is_active")
        worksheet.write('E1', "city")
        worksheet.write('F1', "state")
        worksheet.write('G1', "zip")
        worksheet.write('H1', "country")
        worksheet.write('I1', "phone")
        worksheet.write('J1', "backup_email")
        worksheet.write('K1', "user_type")
        worksheet.write('L1', "subscription_level")
        worksheet.write('M1', "active_user")
        worksheet.write('N1', "user_to_invite")
        worksheet.write('O1', "status")
        worksheet.write('P1', "profile_permission")
        worksheet.write('Q1', "login_status")
        worksheet.write('R1', "activate_status")
        worksheet.write('S1', "organization_name")
        worksheet.write('T1', "verification_status")
        worksheet.write('U1', "created_by")
        worksheet.write('V1', "created_dt")
        worksheet.write('W1', "updated_by")
        worksheet.write('X1', "updated_dt")
        i = 2
        for rows in data:
            print(i)
            worksheet.write('A' + str(i), str(rows.user_name))
            worksheet.write('B' + str(i), str(rows.address))
            worksheet.write('C' + str(i), str(rows.user.email))
            worksheet.write('D' + str(i), str(rows.user.is_active))
            worksheet.write('E' + str(i), str(rows.city))
            worksheet.write('F' + str(i), str(rows.state))
            worksheet.write('G' + str(i), str(rows.zip))
            worksheet.write('H' + str(i), str(rows.country))
            worksheet.write('I' + str(i), str(rows.phone))
            worksheet.write('J' + str(i), str(rows.backup_email))
            worksheet.write('K' + str(i), str(rows.user_type))
            worksheet.write('L' + str(i), str(rows.subscription_level))
            worksheet.write('M' + str(i), str(rows.active_user))
            worksheet.write('N' + str(i), str(rows.user_to_invite))
            worksheet.write('O' + str(i), str(rows.status))
            worksheet.write('P' + str(i), str(list_to_string_profile_permission(rows.profile_permission.all())))
            worksheet.write('Q' + str(i), str(rows.login_status))
            worksheet.write('R' + str(i), str(rows.activate_status))
            worksheet.write('S' + str(i), str(rows.org_id.organization_name))
            worksheet.write('T' + str(i), str(rows.verification_status))
            worksheet.write('U' + str(i), str(get_user_name_by_id(rows.created_by)))
            worksheet.write('V' + str(i), str(rows.created_dt))
            worksheet.write('W' + str(i), str(get_user_name_by_id(rows.updated_by)))
            worksheet.write('X' + str(i), str(rows.updated_dt))
            i += 1
    return True



def get_ar_user_data_csv(org_ins, file_name):
    if Ar_user.objects.filter(org_id=org_ins).exists():
        data = Ar_user.objects.filter(org_id=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['user_name','address','email','is_active','city','state','zip','country','phone','backup_email','user_type','subscription_level','active_user','user_to_invite','status','profile_permission','login_status','activate_status','organization_name','verification_status','created_by','created_dt','updated_by','updated_dt'])
            for rows in data:
                file_writer.writerow([str(rows.user_name),str(rows.address),str(rows.user.email),str(rows.user.is_active),str(rows.city),str(rows.state),str(rows.zip),str(rows.country),str(rows.phone),str(rows.backup_email),str(rows.user_type),str(rows.subscription_level),str(rows.active_user),str(rows.user_to_invite),str(rows.status),str(list_to_string_profile_permission(rows.profile_permission.all())),str(rows.login_status),str(rows.activate_status),str(str(rows.org_id.organization_name)),str(rows.verification_status),str(get_user_name_by_id(rows.created_by)),str(rows.created_dt),str(get_user_name_by_id(rows.updated_by)),str(rows.updated_dt)])
    return True
