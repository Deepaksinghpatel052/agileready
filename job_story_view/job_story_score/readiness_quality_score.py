from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from job_story_view.forms import Ar_Job_Story_Form
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text

from account.models import Ar_user,AR_organization,ArShowcolumns,csvFilesUplodaded,Notification,ArUserStoryScoringPoints,ArJobStoryScoringPoints
from account.forms import csvFilesUplodadedForm
from job_story_view.models import AR_JOB_STORY

from job_story_view.set_job_story_acceptance_criteria_and_conver_algo import flesch_reading_ease

from manage_product.models import AR_product,AR_team
from django.contrib import messages
from datetime import datetime


# from manage_role.models import ArRole
# from manage_benefits.models import ArManageBenefits
# from manage_goals.models import ArManageGoals


from manage_jobsit_set.models import ArJobsitSet
from manage_joboutc_set.models import ArJoboutcSet
from manage_jobmot_set.models import ArJobmotSet
# Role = jobsit , Goals = jobmot, benefit = joboutc


from manage_backlogs.models import AR_BACKLOG
import csv, io
from manage_product import views as product_view
from manage_product import views as product_view




def quelity_score(check_map):
    check_map = check_map.lower()
    if ArJobStoryScoringPoints.objects.filter(Score_key='Joboutc_Tag').exists():
        joboutc_tag = ArJobStoryScoringPoints.objects.get(Score_key='Joboutc_Tag')
        joboutc_key = joboutc_tag.Keyword
        joboutc_key = joboutc_key.lower()
        joboutc_data = list(joboutc_key.split(","))
        joboutc_val = 0
        for joboutc_str in joboutc_data:
            if joboutc_str in check_map:
                joboutc_val = joboutc_val + 1
    else:
        joboutc_val = 0
    if ArJobStoryScoringPoints.objects.filter(Score_key='Jobmot_Tag').exists():
        jobmot_tag = ArJobStoryScoringPoints.objects.get(Score_key='Jobmot_Tag')
        jobmot_key = jobmot_tag.Keyword
        jobmot_key = jobmot_key.lower()
        jobmot_data = list(jobmot_key.split(","))
        jobmot_val = 0
        for jobmot_str in jobmot_data:
            if jobmot_str in check_map:
                jobmot_val = jobmot_val + 1
    else:
        jobmot_val = 0
    if ArJobStoryScoringPoints.objects.filter(Score_key='Jobsit_Tag').exists():
        jobsit_tag = ArJobStoryScoringPoints.objects.get(Score_key='Jobsit_Tag')
        jobsit_key = jobsit_tag.Keyword
        jobsit_key = jobsit_key.lower()
        jobsit_data = list(jobsit_key.split(","))
        jobsit_val = 0
        for jobsit_str in jobsit_data:
            if jobsit_str in check_map:
                jobsit_val = jobsit_val + 1
    else:
        jobsit_val = 0
    if ArJobStoryScoringPoints.objects.filter(Score_key='Joboutc_Text').exists():
        joboutc_text = ArJobStoryScoringPoints.objects.get(Score_key='Joboutc_Text')
        joboutc_text_key = joboutc_text.Keyword
        joboutc_text_key = joboutc_text_key.lower()
        joboutc_text_data = list(joboutc_text_key.split(","))
        joboutc_text_val = 0
        for joboutc_text_str in joboutc_text_data:
            if joboutc_text_str in check_map:
                joboutc_text_val = joboutc_text_val + 1
    else:
        joboutc_text_val = 0
    if ArJobStoryScoringPoints.objects.filter(Score_key='Jobmot_Text').exists():
        jobmot_text = ArJobStoryScoringPoints.objects.get(Score_key='Jobmot_Text')
        jobmot_text_key = jobmot_text.Keyword
        jobmot_text_key = jobmot_text_key.lower()
        jobmot_text_data = list(jobmot_text_key.split(","))
        jobmot_text_val = 0
        for jobmot_text_str in jobmot_text_data:
            if jobmot_text_str in check_map:
                jobmot_text_val = jobmot_text_val + 1
    else:
        jobmot_text_val = 0
    if ArJobStoryScoringPoints.objects.filter(Score_key='Jobsit_Text').exists():
        jobsit_text = ArJobStoryScoringPoints.objects.get(Score_key='Jobsit_Text')
        jobsit_text_key = jobsit_text.Keyword
        jobsit_text_key = jobsit_text_key.lower()
        jobsit_text_data = list(jobsit_text_key.split(","))
        jobsit_text_val = 0
        for jobsit_text_str in jobsit_text_data:
            if jobsit_text_str in check_map:
                jobsit_text_val = jobsit_text_val + 1
    else:
        jobsit_text_val = 0
    # 33333333333333333333333333333333333333333333333333333333
    joboutc_text_data = ArJoboutcSet.objects.all()
    joboutc_text_full_val = 0
    for joboutc_text_str in joboutc_text_data:
        joboutc_text_data = joboutc_text_str.member_product_list
        joboutc_text_data = joboutc_text_data.lower()
        if joboutc_text_data in check_map:
            joboutc_text_full_val = joboutc_text_full_val + 1

    jobmot_text_data = ArJobmotSet.objects.all()
    jobmot_text_full_val = 0
    for jobmot_text_str in jobmot_text_data:
        jobmot_text_data = jobmot_text_str.member_product_list
        jobmot_text_data = jobmot_text_data.lower()
        if jobmot_text_data in check_map:
            jobmot_text_full_val = jobmot_text_full_val + 1

    jobsit_text_data = ArJobsitSet.objects.all()
    jobsit_text_full_val = 0
    for jobsit_text_str in jobsit_text_data:
        jobsit_text_data = jobsit_text_str.member_product_list
        jobsit_text_data = jobsit_text_data.lower()
        if jobsit_text_data in check_map:
            jobsit_text_full_val = jobsit_text_full_val + 1

    # 33333333333333333333333333333333333333333333333333333333

    if ArJobStoryScoringPoints.objects.filter(Score_key='Conjunction Set').exists():
        conjunction_set = ArJobStoryScoringPoints.objects.get(Score_key='Conjunction Set')
        conjunction_set_key = conjunction_set.Keyword
        conjunction_set_key = conjunction_set_key.lower()
        conjunction_set_data = list(conjunction_set_key.split(","))
        conjunction_set_val = 0
        for conjunction_set_str in conjunction_set_data:
            if conjunction_set_str in check_map:
                conjunction_set_val = conjunction_set_val + 1
        if conjunction_set_val == 0:
            conjunction_set_scr = 10
        elif conjunction_set_val == 1 or conjunction_set_val == 2:
            conjunction_set_scr = 5
        else:
            conjunction_set_scr = 1
    else:
        conjunction_set_scr = 0
        conjunction_set_val = 0
    if joboutc_text_val == 0:
        joboutc_text_scr = 1
    else:
        joboutc_text_scr = 5

    if jobmot_text_val == 0:
        jobmot_text_scr = 2
    else:
        jobmot_text_scr = 10

    if jobsit_text_val == 0:
        jobsit_text_scr = 2
    else:
        jobsit_text_scr = 10

    if joboutc_val == 0:
        joboutc_scr = 0
    else:
        joboutc_scr = 10
    if jobmot_val == 0:
        jobmot_scr = 0
    else:
        jobmot_scr = 15
    if jobsit_val == 0:
        jobsit_scr = 0
    else:
        jobsit_scr = 15
    # =====================================
    if jobsit_text_full_val == 0:
        jobsit_text_full_val_scr = 0
    else:
        jobsit_text_full_val_scr = 10
    if jobmot_text_full_val == 0:
        jobmot_text_full_val_scr = 0
    else:
        jobmot_text_full_val_scr = 10
    if joboutc_text_full_val == 0:
        joboutc_text_full_val_scr = 0
    else:
        joboutc_text_full_val_scr = 5
    total_scr = jobsit_text_full_val_scr + jobmot_text_full_val_scr + joboutc_text_full_val_scr + conjunction_set_scr + joboutc_text_scr + jobmot_text_scr + jobsit_text_scr + joboutc_scr + jobmot_scr + jobsit_scr
    return [total_scr,conjunction_set_val]