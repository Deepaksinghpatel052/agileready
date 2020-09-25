from account.models import AR_organization,Ar_user
from manage_backlogs.models import AR_BACKLOG
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from user_story_points.models import ArUserStoryPoints
from user_story_view.models import AR_USER_STORY,file_attachment

from job_story_view.models import AR_JOB_STORY,job_story_file_attachment


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



def get_AR_JOB_STORY_data(org_ins,worksheet):
    if AR_JOB_STORY.objects.filter(ORG_id=org_ins).exists():
        data = AR_JOB_STORY.objects.filter(ORG_id=org_ins)
        worksheet.write('A1', "title")
        worksheet.write('B1', "story_tri_part_text")
        worksheet.write('C1', "acceptance_criteria")
        worksheet.write('D1', "ac_readability_score")
        worksheet.write('E1', "conversation")
        worksheet.write('F1', "backlog_parent")
        worksheet.write('G1', "convo_readability_score")
        worksheet.write('H1', "autoscoring_on")
        worksheet.write('I1', "archive_indicator")
        worksheet.write('J1', "readiness_quality_score")
        worksheet.write('K1', "story_points")
        worksheet.write('L1', "job_story_status")
        worksheet.write('M1', "User_story_type")
        worksheet.write('N1', "ar_user")
        worksheet.write('O1', "owner")
        worksheet.write('P1', "created_by")
        worksheet.write('Q1', "created_dt")
        worksheet.write('R1', "updated_dt")
        worksheet.write('S1', "updated_by")
        worksheet.write('T1', "organization_name")
        worksheet.write('U1', "attachments")
        i = 2
        for rows in data:
            worksheet.write('A' + str(i), str(rows.title))
            worksheet.write('B' + str(i), str(rows.story_tri_part_text))
            worksheet.write('C' + str(i), str(rows.acceptance_criteria))
            worksheet.write('D' + str(i), str(rows.ac_readability_score))
            worksheet.write('E' + str(i), str(rows.conversation))
            worksheet.write('F' + str(i), str(rows.backlog_parent))
            worksheet.write('G' + str(i), str(rows.convo_readability_score))
            worksheet.write('H' + str(i), str(rows.autoscoring_on))
            worksheet.write('I' + str(i), str(rows.archive_indicator))
            worksheet.write('J' + str(i), str(rows.readiness_quality_score))
            worksheet.write('K' + str(i), str(rows.story_points))
            worksheet.write('L' + str(i), str(rows.job_story_status))
            worksheet.write('M' + str(i), str(rows.UST_ID))
            worksheet.write('N' + str(i), str(rows.ar_user))
            worksheet.write('O' + str(i), str(rows.owner))
            worksheet.write('P' + str(i), str(rows.created_by))
            worksheet.write('Q' + str(i), str(rows.created_dt))
            worksheet.write('R' + str(i), str(rows.updated_dt))
            worksheet.write('S' + str(i), str(rows.updated_by))
            worksheet.write('H' + str(i), str(org_ins))
            set_attachment_url = ''
            if job_story_file_attachment.objects.filter(job_story=rows).exists():
                get_attachment = job_story_file_attachment.objects.filter(job_story=rows)
                for item in get_attachment:
                    if item.attachment:
                        set_attachment_url += str(item.attachment.url) + "&"
            worksheet.write('U' + str(i), str(set_attachment_url))
            i += 1
    return True


def get_AR_JOB_STORY_data_CSV(org_ins, file_name):
    if AR_JOB_STORY.objects.filter(ORG_id=org_ins).exists():
        data = AR_JOB_STORY.objects.filter(ORG_id=org_ins)
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ "title","story_tri_part_text","acceptance_criteria","ac_readability_score","conversation","backlog_parent","convo_readability_score","autoscoring_on","archive_indicator","readiness_quality_score","story_points","job_story_status","User_story_type","ar_user","owner","created_by","created_dt","updated_dt","updated_by","organization_name","attachments"])
            for rows in data:
                set_attachment_url = ''
                if job_story_file_attachment.objects.filter(job_story=rows).exists():
                    get_attachment = job_story_file_attachment.objects.filter(job_story=rows)
                    for item in get_attachment:
                        if item.attachment:
                            set_attachment_url  +=str(item.attachment.url)+"&"
                file_writer.writerow([str(rows.title), str(rows.story_tri_part_text),str(rows.acceptance_criteria),str(rows.ac_readability_score),str(rows.conversation),str(rows.backlog_parent),str(rows.convo_readability_score),str(rows.autoscoring_on),str(rows.archive_indicator),str(rows.readiness_quality_score),str(rows.story_points),str(rows.job_story_status),str(rows.UST_ID),str(rows.ar_user),str(rows.owner),str(rows.created_by),str(rows.created_dt),str(rows.updated_dt),str(rows.updated_by),str(org_ins),str(set_attachment_url)])
    return True


def get_AR_JOB_STORY_data_CSV2(request,org_ins, file_name):
    filters1 = Q(ORG_id=org_ins)
    filters2 = Q(ORG_id=org_ins)
    filters3 = Q(ORG_id=org_ins)
    filters4 = Q(ORG_id=org_ins)

    if request.POST["backlog_list"] == "":
        pass
    else:
        backlog_list = request.POST["backlog_list"]

        if backlog_list == "none":
            filters1 = filters1 & Q(backlog_parent__backlog_slug__exact=backlog_list) | Q(
                backlog_parent__backlog_slug__isnull=True)
        else:

            filters1 = filters1 & Q(backlog_parent__backlog_slug__exact=backlog_list)

    if request.POST["business_value_list"] == "":
        pass
    else:
        business_value_list = request.POST["business_value_list"]

        if business_value_list == "none":
            filters2 = filters2 & Q(BV_ID__business_value_slug__exact=business_value_list) | Q(
                BV_ID__business_value_slug__isnull=True)
        else:

            filters2 = filters2 & Q(BV_ID__business_value_slug__exact=business_value_list)

    if request.POST["user_status_list"] == "":
        pass
    else:
        user_status_list = request.POST["user_status_list"]

        if user_status_list == "none":
            filters3 = filters3 & Q(job_story_status__user_status_slug__exact=user_status_list) | Q(
                job_story_status__user_status_slug__isnull=True)
        else:
            filters3 = filters3 & Q(job_story_status__user_status_slug__exact=user_status_list)


    if request.POST["user_type_list"] == "":
        pass
    else:
        user_type_list = request.POST["user_type_list"]

        if user_type_list == "none":
            filters4 = filters4 & Q(UST_ID__user_type_slug__exact=user_type_list) | Q(
                UST_ID__user_type_slug__isnull=True)
        else:
            filters4 = filters4 & Q(UST_ID__user_type_slug__exact=user_type_list)


    if AR_JOB_STORY.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).exists():
        data = AR_JOB_STORY.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).order_by("-id").filter(~Q(title='None'))
        with open(file_name, mode='w') as data_file:
            file_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([ "title","story_tri_part_text","acceptance_criteria","ac_readability_score","conversation","backlog_parent","convo_readability_score","autoscoring_on","archive_indicator","readiness_quality_score","story_points","job_story_status","User_story_type","ar_user","owner","created_by","created_dt","updated_dt","updated_by","organization_name","attachments"])
            for rows in data:
                set_attachment_url = ''
                if job_story_file_attachment.objects.filter(job_story=rows).exists():
                    get_attachment = job_story_file_attachment.objects.filter(job_story=rows)
                    for item in get_attachment:
                        if item.attachment:
                            set_attachment_url  +=str(item.attachment.url)+"&"
                file_writer.writerow([str(rows.title), str(rows.story_tri_part_text),str(rows.acceptance_criteria),str(rows.ac_readability_score),str(rows.conversation),str(rows.backlog_parent),str(rows.convo_readability_score),str(rows.autoscoring_on),str(rows.archive_indicator),str(rows.readiness_quality_score),str(rows.story_points),str(rows.job_story_status),str(rows.UST_ID),str(rows.ar_user),str(rows.owner),str(rows.created_by),str(rows.created_dt),str(rows.updated_dt),str(rows.updated_by),str(org_ins),str(set_attachment_url)])
    return True

