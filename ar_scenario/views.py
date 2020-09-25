from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from agileproject import settings
from .forms import ScenarioForm
from django.contrib import messages
from manage_backlogs.models import AR_BACKLOG
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from test_story_view.models import AR_TEST_STORY
from manage_product.models import AR_product

from .filters import ScenarioFilter

from account.models import Ar_user,AR_organization,ArShowcolumns,ArUserProfilePermission,Notification
from django.contrib.auth.decorators import login_required
from .models import AR_SCENARIO
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
    all_scenario = ""

    # ======================================================

    filters = Q(ORG_ID=org_ins)
    product_token = ""

    if 'product-parent' in request.GET:
        if request.GET['product-parent'] is not None:
            if request.GET['product-parent'] == "none":
                filters = filters & Q(product_id__product_slug__exact=request.GET['product-parent']) | Q(
                    product_id__product_slug__isnull=True)
            else:
                filters = filters & Q(product_id__product_slug__exact=request.GET['product-parent'])
            product_token = request.GET['product-parent']

    if AR_SCENARIO.objects.filter(filters).exists():
        all_scenario = AR_SCENARIO.objects.filter(filters).order_by("-id")
    else:
        all_scenario = {}

    # ======================================================



    if ArShowcolumns.objects.filter(Table_name='AR_SCENARIO').filter(user_id=request.session['user_id']).exists():
        show_column = ArShowcolumns.objects.filter(Table_name='AR_SCENARIO').filter(user_id=request.session['user_id'])
        get_show_column = show_column[0].columnName.split(",")
    else:
        get_show_column = {}

    all_column_list = {
        "scenario_name": "Scenario Name",
        "scenario_desc": "Scenario Description",
        "product_id": "Product Parent",
        "children_ts_list": "Test Story List",
        "scenario_size": "Scenario Size",
        "scenario_score": "Scenario Score",
        "created_by": "Created By",
        "created_dt": "Created Date",
        "updated_by": "Updated By",
        "updated_dt": "Updated Date",
        "ORG_ID": "Organization",

    }

    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Rearrange_Request")
    Rearrange_Request_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Not_Remove")
    Not_Remove_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Remove Request")
    Remove_Request_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Remove_Success")
    Remove_done_msg = msg.notification_desc

    Product_data = AR_product.objects.filter(ORG_ID=org_ins).order_by("product_slug")

    # user_list = AR_SCENARIO.objects.filter(ORG_ID=org_ins).order_by("-id")
    # user_filter = ScenarioFilter(request.GET, queryset=user_list)
    # return render(request, 'search/user_list.html', {'filter': user_filter})

    return render(request, 'admin/manage_scenario/index.html', { 'product_token':product_token,'Product_data':Product_data,"Rearrange_Request_msg": Rearrange_Request_msg,'get_show_column': get_show_column,'all_column_list': all_column_list,'all_scenario':all_scenario,'date':datetime.now(),'user_name':request.session['user_name'],'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'BASE_URL':settings.BASE_URL})




def filter(request,token):

    token = token.replace("+", " ")

    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    all_scenario = ""

    filter_product_ins = get_object_or_404(AR_product, id=token, ORG_ID=org_ins)
    product_token_name = filter_product_ins.Product_name
    if AR_SCENARIO.objects.filter(ORG_ID=org_ins).filter(product_id=filter_product_ins).exists():
        all_scenario = AR_SCENARIO.objects.filter(ORG_ID=org_ins).filter(product_id=filter_product_ins).order_by("-id")
    else:
        all_scenario = {}

    if ArShowcolumns.objects.filter(Table_name='AR_SCENARIO').filter(user_id=request.session['user_id']).exists():
        show_column = ArShowcolumns.objects.filter(Table_name='AR_SCENARIO').filter(user_id=request.session['user_id'])
        get_show_column = show_column[0].columnName.split(",")
    else:
        get_show_column = {}

    all_column_list = {
        "scenario_name": "Scenario Name",
        "scenario_desc": "Scenario Description",
        "product_id": "Product Parent",
        "children_ts_list": "Test Story List",
        "scenario_size": "Scenario Size",
        "scenario_score": "Scenario Score",
        "created_by": "Created By",
        "created_dt": "Created Date",
        "updated_by": "Updated By",
        "updated_dt": "Updated Date",
        "ORG_ID": "Organization",

    }

    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Rearrange_Request")
    Rearrange_Request_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Not_Remove")
    Not_Remove_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Remove Request")
    Remove_Request_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Remove_Success")
    Remove_done_msg = msg.notification_desc

    Product_data = AR_product.objects.filter(ORG_ID=org_ins)

    # user_list = AR_SCENARIO.objects.filter(ORG_ID=org_ins).order_by("-id")
    # user_filter = ScenarioFilter(request.GET, queryset=user_list)
    # return render(request, 'search/user_list.html', {'filter': user_filter})

    return render(request, 'admin/manage_scenario/index.html', {'token':product_token_name, 'Product_data':Product_data,"Rearrange_Request_msg": Rearrange_Request_msg,'get_show_column': get_show_column,'all_column_list': all_column_list,'all_scenario':all_scenario,'date':datetime.now(),'user_name':request.session['user_name'],'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'BASE_URL':settings.BASE_URL})



@login_required
def add_scenario(request):
    if request.method == 'POST':
        scenario_form = ScenarioForm(request.user,request.session['org_id'], request.POST)
        status = scenario_form.is_valid()
        if scenario_form.is_valid():
            Scenario_name = scenario_form.cleaned_data.get('scenario_name')
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            if AR_SCENARIO.objects.filter(scenario_name=Scenario_name).filter(ORG_ID=org_ins).exists():
                msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request, msg_data)
            else:
                org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
                ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                scenario = scenario_form.save(commit=False)
                scenario.ORG_ID = org_ins
                scenario.created_by = ar_user_insta
                scenario.updated_by = ar_user_insta
                scenario.save()
                msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Add")
                msg_data = msg.notification_desc
                messages.info(request, msg_data)
                return redirect(settings.BASE_URL + "manage-scenario")
        else:
            messages.error(request, product_form.errors)
        return redirect(settings.BASE_URL + "manage-scenario/add-scenario")
    else:
        scenario_form = ScenarioForm(request.user,request.session['org_id'])
    return render(request, 'admin/manage_scenario/add_scenario.html', {'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL,'scenario_form':scenario_form})


@login_required
def edit_scenario(request,id):
    scenario_info = get_object_or_404(AR_SCENARIO, pk=id)
    org_id_value = scenario_info.ORG_ID_id
    id_value = id
    if request.method == 'POST':
        scenario_form = ScenarioForm(request.user, request.session['org_id'], request.POST,instance = scenario_info)
        if scenario_form.is_valid():
            scenario = scenario_form.save(commit=False)
            ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
            scenario.update_dt = datetime.now()
            scenario.update_by = ar_user_insta
            scenario.save()
            # product_form.save_m2m()
            msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Update")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
            return redirect(settings.BASE_URL + "manage-scenario")
        else:
            messages.error(request, product_form.error)
        return redirect(settings.BASE_URL + "manage-scenario")
    else:
        scenario_form = ScenarioForm(request.user, request.session['org_id'],instance=scenario_info)
    return render(request, 'admin/manage_scenario/edit_scenario.html',{'date':datetime.now(),'id_value':id_value,'org_id_value':org_id_value,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL, 'scenario_form': scenario_form})


@login_required
def remove_scenario(request,id):
    try:
        get_instance = get_object_or_404(AR_SCENARIO,pk=id)
        get_instance.delete()
        msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Remove")
        msg_data = msg.notification_desc
        messages.info(request, msg_data)
    except(TypeError):
        msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Remove_error")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-scenario')



@login_required
def update_table_structure(request, columnnames):
    if ArShowcolumns.objects.filter(Table_name='AR_SCENARIO').filter(user_id=request.session['user_id']).exists():
        save_column = ArShowcolumns.objects.filter(Table_name='AR_SCENARIO').filter(
            user_id=request.session['user_id']).update(columnName=columnnames)
    else:
        save_column = ArShowcolumns(Table_name='AR_SCENARIO', user_id=request.session['user_id'],
                                    columnName=columnnames, ORG_id=request.session['org_id'])
        save_column.save()
    msg = get_object_or_404(Notification, page_name="Manage Scenario", notification_key="Rearrange")
    msg_data = msg.notification_desc
    messages.info(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-scenario')


# ---------------------------------- download start--------------------------------

@csrf_exempt
def get_data_from_database(request):
    if request.method == "POST":
        print("depak patel")
        today_date = date.today()
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        org_name = org_ins.organization_name.split(" ")
        file_name = "We_agileready_database_backup_"+str(org_name[0])+"_"+ str(today_date.day)+"_"+ str(today_date.month) + "_" + str(today_date.year) +".xlsx"
        file_path = 'static/explode_data_files/xlsx/'+file_name
        # table_list = ["Ar_user", "AR_team", "AR_product", "AR_BACKLOG", "AR_EPIC_CAPABILITY", "AR_FEATURE", "ArUserStoryPoints", "AR_USER_STORY", "ArIterations", "ArRole", "ArManageGoals", "ArManageBenefits"]
        table_list = request.POST["tables"].split(",,")
        workbook = xlsxwriter.Workbook(file_path)
        type = request.POST["file_type"]
        get_file_name = ""
        if type == "xlsx":
            get_file_name += ",,"+file_path
        for items in table_list:
            if type == "CSV":
                get_result = create_csv(request,org_ins,org_name[0], items)
                get_file_name += ",,"+str(get_result)
            else:
                worksheet = workbook.add_worksheet(items)
                if items == "AR_SCENARIO":
                    get_ar_scenario_data(org_ins, worksheet)
        workbook.close()
        export = export_data_info(folder_name=org_ins.organization_name,files_name=get_file_name)
        export.save()
    else:
        today_date = date.today()
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        org_name = org_ins.organization_name.split(" ")
        file_name = "We_agileready_database_backup_" + str(org_name[0]) + "_" + str(today_date.day) + "_" + str(
            today_date.month) + "_" + str(today_date.year) + ".xlsx"
        file_path = 'static/explode_data_files/xlsx/' + file_name
        table_list = ["AR_SCENARIO"]
        workbook = xlsxwriter.Workbook(file_path)
        # type = request.POST["file_type"]
        type = 'xlsx'
        get_file_name = ""
        if type == "xlsx":
            get_file_name += ",," + file_path
        for items in table_list:
            if type == "CSV":
                get_result = create_csv(request,org_ins, org_name[0], items)
                get_file_name += ",," + str(get_result)
            else:
                worksheet = workbook.add_worksheet(items)
                if items == "AR_SCENARIO":
                    get_ar_scenario_data(org_ins, worksheet)


        workbook.close()
        export = export_data_info(folder_name=org_ins.organization_name, files_name=get_file_name)
        export.save()
    # return redirect(settings.BASE_URL+"data-exchange/export-data")
    return JsonResponse({"status":"Done","id":export.id})


def create_csv(request,org_ins,org_name, items):
    today_date = date.today()
    org = org_name+"_"+"ORG"
    date_folder = str(today_date.day)+"_"+ str(today_date.month) + "_" + str(today_date.year)
    direct_url = 'static/explode_data_files/csv/'+ org
    directry_path_check = pathlib.Path(direct_url)

    if directry_path_check.exists():
        direct_url = direct_url+"/"+date_folder
        directry_path_check = pathlib.Path(direct_url)
        if directry_path_check.exists():
            direct_url = direct_url
        else:
            filet_path = os.mkdir(direct_url)
            direct_url = direct_url

    else:
        filet_path  = os.mkdir('static/explode_data_files/csv/'+ org)
        direct_url = 'static/explode_data_files/csv/'+ org+"/"+date_folder
        filet_path = os.mkdir(direct_url)
        direct_url = direct_url
    file_name = direct_url+"/"+items+".csv"

    if items == "AR_SCENARIO":
        get_ar_scenario_data_CSV2(request,org_ins, file_name)

    return file_name
