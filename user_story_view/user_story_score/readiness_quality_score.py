from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from user_story_view.forms import Ar_User_Story_Form
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text
from account.models import Ar_user,AR_organization,ArShowcolumns,csvFilesUplodaded,Notification,ArUserStoryScoringPoints
from account.forms import csvFilesUplodadedForm
from user_story_view.models import AR_USER_STORY
from user_story_view.set_user_story_acceptance_criteria_and_conver_algo import flesch_reading_ease
from manage_product.models import AR_product,AR_team
from django.contrib import messages
from datetime import datetime
from manage_role.models import ArRole
from manage_benefits.models import ArManageBenefits
from manage_goals.models import ArManageGoals
from manage_backlogs.models import AR_BACKLOG
import csv, io
from manage_product import views as product_view
from manage_product import views as product_view



def quelity_score(check_map):
    check_map = check_map.lower()
    if ArUserStoryScoringPoints.objects.filter(Score_key='Benefit_Tag').exists():
        benefit_tag = ArUserStoryScoringPoints.objects.get(Score_key='Benefit_Tag')
        benefit_key = benefit_tag.Keyword
        benefit_key = benefit_key.lower()
        benefit_data = list(benefit_key.split(","))
        benefit_val = 0
        for benefit_str in benefit_data:
            if benefit_str in check_map:
                benefit_val = benefit_val + 1
    else:
        benefit_val = 0
    if ArUserStoryScoringPoints.objects.filter(Score_key='Goal_Tag').exists():
        goal_tag = ArUserStoryScoringPoints.objects.get(Score_key='Goal_Tag')
        goal_key = goal_tag.Keyword
        goal_key = goal_key.lower()
        goal_data = list(goal_key.split(","))
        goal_val = 0
        for goal_str in goal_data:
            if goal_str in check_map:
                goal_val = goal_val + 1
    else:
        goal_val = 0
    if ArUserStoryScoringPoints.objects.filter(Score_key='Role_Tag').exists():
        role_tag = ArUserStoryScoringPoints.objects.get(Score_key='Role_Tag')
        role_key = role_tag.Keyword
        role_key = role_key.lower()
        role_data = list(role_key.split(","))
        role_val = 0
        for role_str in role_data:
            if role_str in check_map:
                role_val = role_val + 1
    else:
        role_val = 0
    if ArUserStoryScoringPoints.objects.filter(Score_key='Benefit_text').exists():
        benefit_text = ArUserStoryScoringPoints.objects.get(Score_key='Benefit_text')
        benefit_text_key = benefit_text.Keyword
        benefit_text_key = benefit_text_key.lower()
        benefit_text_data = list(benefit_text_key.split(","))
        benefit_text_val = 0
        for benefit_text_str in benefit_text_data:
            if benefit_text_str in check_map:
                benefit_text_val = benefit_text_val + 1
    else:
        benefit_text_val = 0
    if ArUserStoryScoringPoints.objects.filter(Score_key='Goal_text').exists():
        goal_text = ArUserStoryScoringPoints.objects.get(Score_key='Goal_text')
        goal_text_key = goal_text.Keyword
        goal_text_key = goal_text_key.lower()
        goal_text_data = list(goal_text_key.split(","))
        goal_text_val = 0
        for goal_text_str in goal_text_data:
            if goal_text_str in check_map:
                goal_text_val = goal_text_val + 1
    else:
        goal_text_val = 0
    if ArUserStoryScoringPoints.objects.filter(Score_key='Role_text').exists():
        role_text = ArUserStoryScoringPoints.objects.get(Score_key='Role_text')
        role_text_key = role_text.Keyword
        role_text_key = role_text_key.lower()
        role_text_data = list(role_text_key.split(","))
        role_text_val = 0
        for role_text_str in role_text_data:
            if role_text_str in check_map:
                role_text_val = role_text_val + 1
    else:
        role_text_val = 0
    # 33333333333333333333333333333333333333333333333333333333
    benefit_text_data = ArManageBenefits.objects.all()
    benefit_text_full_val = 0
    for benefit_text_str in benefit_text_data:
        benefit_text_data = benefit_text_str.Benefits_title
        benefit_text_data = benefit_text_data.lower()
        if benefit_text_data in check_map:
            benefit_text_full_val = benefit_text_full_val + 1

    goal_text_data = ArManageGoals.objects.all()
    goal_text_full_val = 0
    for goal_text_str in goal_text_data:
        goal_text_data = goal_text_str.Goal_title
        goal_text_data = goal_text_data.lower()
        if goal_text_data in check_map:
            goal_text_full_val = goal_text_full_val + 1

    role_text_data = ArRole.objects.all()
    role_text_full_val = 0
    for role_text_str in role_text_data:
        role_text_data = role_text_str.title
        role_text_data = role_text_data.lower()
        if role_text_data in check_map:
            role_text_full_val = role_text_full_val + 1

    # 33333333333333333333333333333333333333333333333333333333

    if ArUserStoryScoringPoints.objects.filter(Score_key='Benefit_Tag').exists():
        conjunction_set = ArUserStoryScoringPoints.objects.get(Score_key='Conjunction Set')
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
    if benefit_text_val == 0:
        benefit_text_scr = 1
    else:
        benefit_text_scr = 5

    if goal_text_val == 0:
        goal_text_scr = 2
    else:
        goal_text_scr = 10

    if role_text_val == 0:
        role_text_scr = 2
    else:
        role_text_scr = 10

    if benefit_val == 0:
        benefit_scr = 0
    else:
        benefit_scr = 10
    if goal_val == 0:
        goal_scr = 0
    else:
        goal_scr = 15
    if role_val == 0:
        role_scr = 0
    else:
        role_scr = 15
    # =====================================
    if role_text_full_val == 0:
        role_text_full_val_scr = 0
    else:
        role_text_full_val_scr = 10
    if goal_text_full_val == 0:
        goal_text_full_val_scr = 0
    else:
        goal_text_full_val_scr = 10
    if benefit_text_full_val == 0:
        benefit_text_full_val_scr = 0
    else:
        benefit_text_full_val_scr = 5
    total_scr = role_text_full_val_scr + goal_text_full_val_scr + benefit_text_full_val_scr + conjunction_set_scr + benefit_text_scr + goal_text_scr + role_text_scr + benefit_scr + goal_scr + role_scr
    return [total_scr,conjunction_set_val]