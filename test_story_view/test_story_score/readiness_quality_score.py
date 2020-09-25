from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from test_story_view.forms import AR_TEST_STORY_Form
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text

from account.models import Ar_user,AR_organization,ArShowcolumns,csvFilesUplodaded,Notification,ArUserStoryScoringPoints,ArJobStoryScoringPoints,ArTestStoryScoringPoints
from account.forms import csvFilesUplodadedForm
from test_story_view.models import AR_TEST_STORY

from test_story_view.set_test_story_acceptance_criteria_and_conver_algo import flesch_reading_ease

from manage_product.models import AR_product,AR_team
from django.contrib import messages
from datetime import datetime


# from manage_role.models import ArRole
# from manage_benefits.models import ArManageBenefits
# from manage_goals.models import ArManageGoals


from manage_testcond_set.models import ArTestcondSet
from manage_testact_set.models import ArTestactSet
from manage_testoutc_set.models import ArTestoutcSet


from manage_jobsit_set.models import ArJobsitSet
from manage_joboutc_set.models import ArJoboutcSet
from manage_jobmot_set.models import ArJobmotSet
# Role = jobsit , Goals = jobmot, benefit = joboutc

# Role = Test Condition , Goals = test action, benefit = Test outcome


from manage_backlogs.models import AR_BACKLOG


import csv, io
from manage_product import views as product_view
from manage_product import views as product_view




def quelity_score(check_map):
    check_map = check_map.lower()
    if ArTestStoryScoringPoints.objects.filter(Score_key='Testoutc_Tag').exists():
        testoutc_tag = ArTestStoryScoringPoints.objects.get(Score_key='Testoutc_Tag')
        testoutc_key = testoutc_tag.Keyword
        testoutc_key = testoutc_key.lower()
        testoutc_data = list(testoutc_key.split(","))
        testoutc_val = 0
        for testoutc_str in testoutc_data:
            if testoutc_str in check_map:
                testoutc_val = testoutc_val + 1
    else:
        testoutc_val = 0
    if ArTestStoryScoringPoints.objects.filter(Score_key='Testact_Tag').exists():
        testact_tag = ArTestStoryScoringPoints.objects.get(Score_key='Testact_Tag')
        testact_key = testact_tag.Keyword
        testact_key = testact_key.lower()
        testact_data = list(testact_key.split(","))
        testact_val = 0
        for testact_str in testact_data:
            if testact_str in check_map:
                testact_val = testact_val + 1
    else:
        testact_val = 0
    if ArTestStoryScoringPoints.objects.filter(Score_key='Testcond_Tag').exists():
        testcond_tag = ArTestStoryScoringPoints.objects.get(Score_key='Testcond_Tag')
        testcond_key = testcond_tag.Keyword
        testcond_key = testcond_key.lower()
        testcond_data = list(testcond_key.split(","))
        testcond_val = 0
        for testcond_str in testcond_data:
            if testcond_str in check_map:
                testcond_val = testcond_val + 1
    else:
        testcond_val = 0
    if ArTestStoryScoringPoints.objects.filter(Score_key='Testoutc_Text').exists():
        testoutc_text = ArTestStoryScoringPoints.objects.get(Score_key='Testoutc_Text')
        testoutc_text_key = testoutc_text.Keyword
        testoutc_text_key = testoutc_text_key.lower()
        testoutc_text_data = list(testoutc_text_key.split(","))
        testoutc_text_val = 0
        for testoutc_text_str in testoutc_text_data:
            if testoutc_text_str in check_map:
                testoutc_text_val = testoutc_text_val + 1
    else:
        testoutc_text_val = 0
    if ArTestStoryScoringPoints.objects.filter(Score_key='Testact_Text').exists():
        testact_text = ArTestStoryScoringPoints.objects.get(Score_key='Testact_Text')
        testact_text_key = testact_text.Keyword
        testact_text_key = testact_text_key.lower()
        testact_text_data = list(testact_text_key.split(","))
        testact_text_val = 0
        for testact_text_str in testact_text_data:
            if testact_text_str in check_map:
                testact_text_val = testact_text_val + 1
    else:
        testact_text_val = 0
    if ArTestStoryScoringPoints.objects.filter(Score_key='Testcond_Text').exists():
        testcond_text = ArTestStoryScoringPoints.objects.get(Score_key='Testcond_Text')
        testcond_text_key = testcond_text.Keyword
        testcond_text_key = testcond_text_key.lower()
        testcond_text_data = list(testcond_text_key.split(","))
        testcond_text_val = 0
        for testcond_text_str in testcond_text_data:
            if testcond_text_str in check_map:
                testcond_text_val = testcond_text_val + 1
    else:
        testcond_text_val = 0
    # 33333333333333333333333333333333333333333333333333333333
    testoutc_text_data = ArTestoutcSet.objects.all()
    testoutc_text_full_val = 0
    for testoutc_text_str in testoutc_text_data:
        testoutc_text_data = testoutc_text_str.member_product_list
        testoutc_text_data = testoutc_text_data.lower()
        if testoutc_text_data in check_map:
            testoutc_text_full_val = testoutc_text_full_val + 1

    testact_text_data = ArTestactSet.objects.all()
    testact_text_full_val = 0
    for testact_text_str in testact_text_data:
        testact_text_data = testact_text_str.member_product_list
        testact_text_data = testact_text_data.lower()
        if testact_text_data in check_map:
            testact_text_full_val = testact_text_full_val + 1

    testcond_text_data = ArTestcondSet.objects.all()
    testcond_text_full_val = 0
    for testcond_text_str in testcond_text_data:
        testcond_text_data = testcond_text_str.member_product_list
        testcond_text_data = testcond_text_data.lower()
        if testcond_text_data in check_map:
            testcond_text_full_val = testcond_text_full_val + 1

    # 33333333333333333333333333333333333333333333333333333333

    if ArTestStoryScoringPoints.objects.filter(Score_key='Conjunction Set').exists():
        conjunction_set = ArTestStoryScoringPoints.objects.get(Score_key='Conjunction Set')
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
    if testoutc_text_val == 0:
        testoutc_text_scr = 1
    else:
        testoutc_text_scr = 5

    if testact_text_val == 0:
        testact_text_scr = 2
    else:
        testact_text_scr = 10

    if testcond_text_val == 0:
        testcond_text_scr = 2
    else:
        testcond_text_scr = 10

    if testoutc_val == 0:
        testoutc_scr = 0
    else:
        testoutc_scr = 10
    if testact_val == 0:
        testact_scr = 0
    else:
        testact_scr = 15
    if testcond_val == 0:
        testcond_scr = 0
    else:
        testcond_scr = 15
    # =====================================
    if testcond_text_full_val == 0:
        testcond_text_full_val_scr = 0
    else:
        testcond_text_full_val_scr = 10
    if testact_text_full_val == 0:
        testact_text_full_val_scr = 0
    else:
        testact_text_full_val_scr = 10
    if testoutc_text_full_val == 0:
        testoutc_text_full_val_scr = 0
    else:
        testoutc_text_full_val_scr = 5
    total_scr = testcond_text_full_val_scr + testact_text_full_val_scr + testoutc_text_full_val_scr + conjunction_set_scr + testoutc_text_scr + testact_text_scr + testcond_text_scr + testoutc_scr + testact_scr + testcond_scr
    return [total_scr,conjunction_set_val]