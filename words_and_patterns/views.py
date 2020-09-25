from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from agileproject import settings
from django.contrib import messages
from manage_backlogs.models import AR_BACKLOG
from manage_epic_capability.models import AR_EPIC_CAPABILITY

from manage_role.models import ArRole
from manage_goals.models import ArManageGoals
from manage_benefits.models import ArManageBenefits

from manage_jobmot_set.models import ArJobmotSet
from manage_joboutc_set.models import ArJoboutcSet
from manage_jobsit_set.models import ArJobsitSet

from manage_testact_set.models import ArTestactSet
from manage_testcond_set.models import ArTestcondSet
from manage_testoutc_set.models import ArTestoutcSet


from test_story_view.models import AR_TEST_STORY
from manage_product.models import AR_product
from .models import Ar_Category

from account.models import Ar_user,AR_organization,ArShowcolumns,ArUserProfilePermission,Notification
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.template.defaulttags import register
from django.db.models import Q
from dashboard.views import get_package_limit


import xlsxwriter
import pathlib
import os
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date
from django.http import HttpResponse,JsonResponse
from data_import_export.models import export_data_info
from  data_import_export.export_data.data_export_ar_scenario  import get_ar_scenario_data,get_ar_scenario_data_CSV,get_ar_scenario_data_CSV2
# Create your views here.


@login_required
def index(request):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    Product_data = AR_product.objects.filter(ORG_ID=org_ins).order_by("product_slug")
    category_data = Ar_Category.objects.all()
    filters1 = Q(ORG_ID=org_ins)
    filters2 = Q(ORG_id=org_ins)
    product_token = ""
    category_token = ""



    if 'category' not in request.GET and 'product-parent' not in request.GET:
        pass
    else:
        if 'category' not in request.GET:
            msg_data = "Please select category."
            messages.error(request, msg_data)
        if 'product-parent' not in request.GET:
            msg_data = "Please select product."
            messages.error(request, msg_data)


    if 'product-parent' in request.GET:
        if request.GET['product-parent'] is not None:
            if request.GET['product-parent'] == "none":
                filters1 = filters1 & Q(product_parent__product_slug__exact=request.GET['product-parent']) | Q(
                    product_parent__product_slug__isnull=True)
                filters2 = filters2 & Q(product_parent__product_slug__exact=request.GET['product-parent']) | Q(
                    product_parent__product_slug__isnull=True)
            else:
                filters1 = filters1 & Q(product_parent__product_slug__exact=request.GET['product-parent'])
                filters2 = filters2 & Q(product_parent__product_slug__exact=request.GET['product-parent'])
            product_token = request.GET['product-parent']
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++

            result2 = ""
            if AR_TEST_STORY.objects.filter(filters2).exists():
                all_test_story_get = AR_TEST_STORY.objects.filter(filters2).order_by("-id")
                for data_test in all_test_story_get:
                    result2 = result2 + "[" + data_test.story_tri_part_text + "]"

            if AR_BACKLOG.objects.filter(filters1).exists():
                all_backlog_get = AR_BACKLOG.objects.filter(filters1).order_by("-id")


                result = ""
                result1 = ""

                for data_back in all_backlog_get:
                    for data in data_back.story_by_backlog.all():
                        result = result + "[" + data.story_tri_part_text + "]"
                    for data in data_back.job_story_by_backlog.all():
                        result1 = result1 + "[" + data.story_tri_part_text + "]"



                if 'category' in request.GET:
                    if request.GET['category'] is not None:
                        category_token = request.GET['category']
                        if request.GET['category'] == "role":
                            role_data = ArRole.objects.filter(ORG_ID=org_ins).order_by("-id")
                            # return HttpResponse(str(result))

                            dicts = {key.title: result.count(str(key.title)) for key in role_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Role"

                        if request.GET['category'] == "goal":
                            goal_data = ArManageGoals.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.Goal_title: result.count(str(key.Goal_title)) for key in goal_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Goal"

                        if request.GET['category'] == "benefit":
                            benefit_data = ArManageBenefits.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.Benefits_title: result.count(str(key.Benefits_title)) for key in benefit_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Benefit"

                        if request.GET['category'] == "job-situation":
                            job_sit_data = ArJobsitSet.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.member_product_list: result1.count(str(key.member_product_list)) for key in job_sit_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Job Situation"

                        if request.GET['category'] == "job-motivation":
                            job_mot_data = ArJobmotSet.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.member_product_list: result1.count(str(key.member_product_list)) for key in job_mot_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Job Motivation"


                        if request.GET['category'] == "job-outcome":
                            job_outc_data = ArJoboutcSet.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.member_product_list: result1.count(str(key.member_product_list)) for key in job_outc_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Job Outcome"






                        if request.GET['category'] == "test-condition":
                            test_cond_data = ArTestcondSet.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.member_product_list: result2.count(str(key.member_product_list)) for key in test_cond_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Test Condition"

                        if request.GET['category'] == "test-action":
                            test_act_data = ArTestactSet.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.member_product_list: result2.count(str(key.member_product_list)) for key in test_act_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Test Action"

                        if request.GET['category'] == "test-outcome":
                            job_outc_data = ArTestoutcSet.objects.filter(ORG_ID=org_ins).order_by("-id")
                            dicts = {key.member_product_list: result2.count(str(key.member_product_list)) for key in job_outc_data}
                            val = ""
                            for k in dicts.keys():
                                for x in range(int(dicts[k])):
                                    val = val + str(k) + " "
                            category_name="Test Outcome"


                        return render(request, 'admin/manage_word_patterns/index.html',
                                      {'text':val,'category_token':category_token,'category_name':category_name,'dicts': dicts, 'category_data': category_data, 'product_token': product_token,
                                       'Product_data': Product_data, 'date': datetime.now(),
                                       'user_name': request.session['user_name'], 'BASE_URL': settings.BASE_URL})

                    else:
                        msg_data = "Please select category."
                        messages.error(request, msg_data)
        else:
            msg_data = "Please select product."
            messages.error(request, msg_data)




    return render(request, 'admin/manage_word_patterns/index.html', {'category_token':category_token,'category_data':category_data, 'product_token':product_token,'Product_data':Product_data,'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL})



