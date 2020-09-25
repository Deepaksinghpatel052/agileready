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

from manage_features.models import AR_FEATURE
from business_value.models import AR_BUSINESS_VALUE


from test_story_view.models import AR_TEST_STORY
from manage_product.models import AR_product
# from .models import Ar_Category

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
    # -------------------------------------
    filters1 = Q(ORG_ID=org_ins)
    filters2 = Q(ORG_ID=org_ins)
    business_value_token = ""
    product_token = ""
    val = ""
    dicts = ""
    # -----------------------------------------------------------------------
    if 'product-parent' in request.GET:
        if request.GET['product-parent'] is not None:
            if request.GET['product-parent'] == "none":
                product_ins = get_object_or_404(AR_product, product_slug=request.GET['product-parent'], ORG_ID=org_ins)
                filters2 = filters2 & Q(CE_ID__PROJECT_ID=product_ins) | Q(CE_ID__PROJECT_ID__isnull=True)
            else:
                product_ins = get_object_or_404(AR_product, product_slug=request.GET['product-parent'], ORG_ID=org_ins)
                filters2 = filters2 & Q(CE_ID__PROJECT_ID=product_ins)
        product_token = request.GET['product-parent']
    # -----------------------------------------------------------------------
    if 'business-value' in request.GET:
        if request.GET['business-value'] is not None:
            if request.GET['business-value'] == "none":
                filters2 = filters2 & Q(BV_ID__business_value_slug__exact=request.GET['business-value']) | Q(
                    BV_ID__business_value_slug__isnull=True)
            else:
                filters2 = filters2 & Q(BV_ID__business_value_slug__exact=request.GET['business-value'])
            business_value_token = request.GET['business-value']
    # ---------------------------------------------------------------------------
    feature_data = AR_FEATURE.objects.filter(filters2).order_by("-id").filter(~Q(Feature_key = 'None'))
    product_data = AR_product.objects.filter(ORG_ID=org_ins).order_by("product_slug")
    business_value_list = AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_ins).order_by("business_value_slug")
    result=""

    # -----------------------------------------------------------
    FBV = Q(id=0)
    for data in feature_data:
        FBV = FBV | Q(id=data.BV_ID_id)
    filters1 =  FBV

    # -----------------------------------------------------------

    for data in feature_data:
        result = result + "[" + str(data.BV_ID) + "]"
        business_value_data = AR_BUSINESS_VALUE.objects.filter(filters1).order_by("-id")
        dicts = {key.bus_value_txt_code: result.count(str(key.bus_value_txt_code)) for key in business_value_data}
        for k in dicts.keys():
            for x in range(int(dicts[k])):
                val = val + str(k) + " "
        # return HttpResponse(filters1)
    return render(request, 'admin/feature_value/index.html',
                  {'product_token':product_token,'product_data':product_data,'business_value_list':business_value_list,'business_value_token':business_value_token,'feature_data':feature_data,'text':val,'dicts': dicts,
                    'date': datetime.now(),
                   'user_name': request.session['user_name'], 'BASE_URL': settings.BASE_URL})