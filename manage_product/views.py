from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from agileproject import settings
from .forms import ProductForm
from django.contrib import messages
from manage_backlogs.models import AR_BACKLOG
from manage_features.models import AR_FEATURE
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from account.models import Ar_user,AR_organization,ArShowcolumns,ArUserProfilePermission,Notification
from django.contrib.auth.decorators import login_required
from .models import AR_product,AR_team

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
from  data_import_export.export_data.data_export_ar_product  import get_ar_product_data,get_ar_product_data_CSV,get_ar_product_data_CSV2
# Create your views here.

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)



def check_permition(request,page_name_get,page_action_get):
    '''
    This function is use for check the user permission
    and it's tke some peramiters 4 peramiters
    1 'request' this is a statis and required
    2 'page_name' for which page you check that (String)
    3 'peramiters' type it's use the 0 OR 1 value 0 for view page and 1 for edit page (int)
     and this function is return true or false value for if user have the peramiters for that task then it's give true other it's give false
    '''
    status_set = True
    page_name = page_name_get   #'Product View'
    page_action = page_action_get    # 0 USE FOR VIEW ACTION AND 1 FOR EDIT SECTION
    # page_name_action = '1'
    get_current_user = Ar_user.objects.get(id=request.session['user_id'])
    if get_current_user.user_type == 'User':
        status_set = False
        get_user_info = get_object_or_404(Ar_user, pk=request.session['user_id'])
        set_profile_daat = get_user_info.profile_permission.all()
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        for items in set_profile_daat:
            print(items)
            if ArUserProfilePermission.objects.filter(activites=page_name,profile_key=items,ORG_ID=org_ins).exists():
                get_permition_data = ArUserProfilePermission.objects.get(activites=page_name,profile_key=items,ORG_ID=org_ins)
                if get_permition_data.editor:
                    status_set = True
                else:
                    status_set = False
                    if page_action == 0:
                        if get_permition_data.viewer:
                            status_set = True
                        else:
                            status_set = False
            else:
                status_set = False
            if status_set:
                break
    return status_set

@login_required
def productview(request):
    product_data = AR_product.objects.filter(ORG_ID=request.session['org_id'])
    return render(request, 'admin/product_view/index.html',{'date':datetime.now(),'product_data':product_data,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})

# Find common value from two array start
def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)
    intersection_set = set1.intersection(set2)
    intersection_list = list(intersection_set)
    return intersection_list
# Find common value from two array stop

@login_required
def index(request,set_statue="",set_statue_2="",csv_id=""):
    gat_url = request.get_full_path()
    get_status_of_permission = True
    if gat_url.find('manage-products') != -1:
        get_status_of_permission = check_permition(request, 'Manage Products', 0)
    else:
        get_status_of_permission = check_permition(request, 'Product View', 0)
    if get_status_of_permission:
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])

        # ======================================================

        filters1 = Q(ORG_ID=org_ins)
        filters2 = Q(ORG_ID=org_ins)
        filters3 = Q(ORG_ID=org_ins)
        filters4 = Q(ORG_ID=org_ins)
        filters_remove = ~Q(Product_name = 'None')

        backlog_token = ""
        team_token = ""
        epic_capability_token = ""
        feature_token = ""
        # ----------------------------------------- Team filter--------------------------------


        if 'team' in request.GET:
            if request.GET['team'] is not None:
                if request.GET['team'] == "none":
                    filter_team_ins = get_object_or_404(AR_team, team_slug=request.GET['team'], ORG_id=org_ins)
                    QTB = Q(team_list=filter_team_ins)
                    all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id").filter(~Q(title='None'))
                    result = []
                    for data_back in all_backlog_get:
                        result.append(data_back.product_parent.id)
                    final_result_team = result
                    # ----------------------------- -------------------------
                    filters1 = filters1 & Q(id__in=final_result_team) | Q(backlog_by_product__isnull=True) & Q(
                        ORG_ID=org_ins)

                else:

                    filter_team_ins = get_object_or_404(AR_team, team_slug=request.GET['team'], ORG_id=org_ins)
                    QTB = Q(team_list=filter_team_ins)
                    all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id").filter(~Q(title='None'))
                    result = []
                    for data_back in all_backlog_get:
                        result.append(data_back.product_parent.id)
                    final_result_team = result
                    # ----------------------------- -------------------------
                    filters1 = filters1 & Q(id__in=final_result_team)
                team_token = request.GET['team']

        # ----------------------------------------- Backlog filter--------------------------------
        if 'backlog' in request.GET:
            if request.GET['backlog'] is not None:
                if request.GET['backlog'] == "none":
                    all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(
                        backlog_slug=request.GET['backlog']).order_by("-id").filter(~Q(title='None'))
                    result = []
                    for data_back in all_backlog_get:
                        result.append(data_back.product_parent.id)
                    final_result_backlog = result
                    filters2 = filters2 & Q(id__in=final_result_backlog) | Q(backlog_by_product__isnull=True) & Q(
                        ORG_ID=org_ins)
                else:
                    all_backlog_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(backlog_slug=request.GET['backlog']).order_by("-id").filter(~Q(title='None'))
                    result = []
                    for data_back in all_backlog_get:
                        result.append(data_back.product_parent.id)
                    final_result_backlog = result
                    filters2 = filters2 & Q(id__in=final_result_backlog)
                backlog_token = request.GET['backlog']
        # ----------------------------------------- Epic filter--------------------------------
        if 'epic-capability' in request.GET:
            if request.GET['epic-capability'] is not None:
                if request.GET['epic-capability'] == "none":
                    all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(
                        epic_capability_slug=request.GET['epic-capability']).order_by("-id")
                    got = ""
                    for data_epic in all_epic_get:
                        result = []
                        got = ""
                        for val in data_epic.PROJECT_ID.all():
                            got = val.id
                            result.append(got)
                    final_result_epic = result

                    filters3 = filters3 & Q(id__in=final_result_epic) | Q(epic_capability_product__isnull=True) & Q(
                        ORG_ID=org_ins)
                else:

                    all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(epic_capability_slug=request.GET['epic-capability']).order_by("-id")
                    got = ""
                    for data_epic in all_epic_get:
                        result = []
                        got = ""
                        for val in data_epic.PROJECT_ID.all():
                            got = val.id
                            result.append(got)
                    final_result_epic = result

                    filters3 = filters3 & Q(id__in=final_result_epic)
                epic_capability_token = request.GET['epic-capability']

        # ----------------------------------------- Feature filter--------------------------------
        if 'feature' in request.GET:
            if request.GET['feature'] is not None:
                if request.GET['feature'] == "none":

                    filter_feature_ins = get_object_or_404(AR_FEATURE, feature_slug=request.GET['feature'],
                                                           ORG_ID=org_ins)
                    QTB = Q(epic_from_feature=filter_feature_ins)
                    all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id")
                    result = []
                    for data_epic in all_epic_get:
                        for val in data_epic.PROJECT_ID.all():
                            got = val.id
                            result.append(got)
                    final_result_feature = result

                    filters4 = filters4 & Q(id__in=final_result_feature) | Q(epic_capability_product__isnull=True) & Q(
                        ORG_ID=org_ins)
                else:
                    filter_feature_ins = get_object_or_404(AR_FEATURE, feature_slug=request.GET['feature'], ORG_ID=org_ins)
                    QTB = Q(epic_from_feature=filter_feature_ins)
                    all_epic_get = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).filter(QTB).order_by("-id")
                    result = []
                    for data_epic in all_epic_get:
                        for val in data_epic.PROJECT_ID.all():
                            got = val.id
                            result.append(got)
                    final_result_feature = result

                    filters4 = filters4 & Q(id__in=final_result_feature)
                feature_token = request.GET['feature']

        # ----------------------------------------- apply filter--------------------------------

        if AR_product.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).filter(filters_remove).exists():
            all_project_get = AR_product.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).order_by("-id").filter(filters_remove)
        else:
            all_project_get = {}

        # ======================================================



        if ArShowcolumns.objects.filter(Table_name='AR_PRODUCT').filter(user_id=request.session['user_id']).exists():
            show_column = ArShowcolumns.objects.filter(Table_name='AR_PRODUCT').filter(user_id=request.session['user_id'])
            get_show_column = show_column[0].columnName.split(",")
        else:
            get_show_column = {}
        all_column_list = {
            "Team_parent": "Teams",
            "Children_backlog_list": "Children Backlog List",
            "Children_scenario_list": "Children Scenario List",
            "Product_name":"Product Name",
            "Product_description":"Product Description",
            "Business_unit":"Business Unit",
            "Product_size":"Product Size",
            "Product_score":"Product Score",
            "US_quality_threshold":"Us Quality Threshold",
            "ORG_ID":"ORG Name",
            "create_by":"Created By",
            "create_dt":"Created Date",
            "update_by":"Updated By",
            "update_dt":"Updated Date",
            "capability":"Capability",
            "feature":"Feature",
                }
        msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Rearrange_Request")
        Rearrange_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        ar_backlog = AR_BACKLOG.objects.all()

        get_permition_for_edit = check_permition(request, 'Manage Products', 1)

        # ------------------------------------------------------------
        backlog_data = AR_BACKLOG.objects.filter(ORG_ID=org_ins).order_by("backlog_slug")
        team_data = AR_team.objects.filter(ORG_id=org_ins).order_by("team_slug")
        epic_capability_data = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).order_by("epic_capability_slug")
        feature_data = AR_FEATURE.objects.filter(ORG_ID=org_ins).order_by("feature_slug")
        # ------------------------------------------------------------


        return render(request, 'admin/manage_product/index.html', {'feature_token':feature_token,'epic_capability_token':epic_capability_token,'team_token':team_token,'backlog_token':backlog_token,'feature_data':feature_data,'epic_capability_data':epic_capability_data,'team_data':team_data,'backlog_data':backlog_data,'get_permition_for_edit':get_permition_for_edit,'ar_backlog':ar_backlog,'Rearrange_Request_msg':Rearrange_Request_msg,'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'all_project_get':all_project_get,'all_column_list':all_column_list,"get_show_column":get_show_column,'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL,"all_project_get":all_project_get})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})



# ---------------------------------------------
# ---------------------------------------------


@login_required
def add_product(request):
    if check_permition(request, 'Manage Products', 1):
        if request.method == 'POST':
            product_form = ProductForm(request.user,request.session['org_id'], request.POST)
            status = product_form.is_valid()
            if product_form.is_valid():
                Product_name = product_form.cleaned_data.get('Product_name')
                org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
                if AR_product.objects.filter(Product_name=Product_name).filter(ORG_ID=org_ins).exists():
                    msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, msg_data)
                else:
                    get_status = get_package_limit(request.session['org_id'],"Product")
                    if get_status:
                        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
                        ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                        product = product_form.save(commit=False)
                        product.ORG_ID = org_ins
                        product.create_by = ar_user_insta
                        product.update_by = ar_user_insta
                        product.save()
                        product_form.save_m2m()
                        msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                    else:
                        msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                        msg_data = msg.notification_desc
                        messages.error(request, msg_data)   
                    return redirect(settings.BASE_URL + "manage-products")
            else:
                messages.error(request, product_form.errors)
            return redirect(settings.BASE_URL + "manage-products/add-product")
        else:
            product_form = ProductForm(request.user,request.session['org_id'])
        return render(request, 'admin/manage_product/add_project.html', {'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL,'product_form':product_form})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})
@login_required
def remove_product(request,id):
    if check_permition(request, 'Manage Products', 1):
        try:
            project = get_object_or_404(AR_product, pk=id)
            project.delete()
            msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        except(TypeError, OverflowError):
            msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL+'manage-products')




@register.filter
def get_capability(id):
    capability_data = AR_EPIC_CAPABILITY.objects.filter(PROJECT_ID=id)
    epic_data_get = ""
    for data in capability_data:
        if epic_data_get != "":
            epic_data_get = epic_data_get + " | " + str(data)
        else:
            epic_data_get = str(data)
    return epic_data_get

@register.filter
def get_feature(id):
    capability_data = AR_EPIC_CAPABILITY.objects.filter(PROJECT_ID=id)
    epic_data_get = ""
    feature_data_get = ""
    for data in capability_data:
        if epic_data_get != "":
            epic_data_get = epic_data_get + " | " + str(data)
        else:
            epic_data_get = str(data)
        for val in data.epic_from_feature.all():

            if feature_data_get != "":
                feature_data_get = feature_data_get + " | " + str(val)
            else:
                feature_data_get = str(val)
    return feature_data_get


@login_required
def edit_product(request,id):
    if check_permition(request, 'Manage Products', 1):
        product_info = get_object_or_404(AR_product, pk=id)

        capability_data = AR_EPIC_CAPABILITY.objects.filter(PROJECT_ID=id)
        epic_data_get = ""
        feature_data_get= ""
        for data in capability_data:
            if epic_data_get != "":
                epic_data_get = epic_data_get + " | " + str(data)
            else:
                epic_data_get = str(data)
            for val in data.epic_from_feature.all():

                if feature_data_get != "":
                    feature_data_get = feature_data_get + " | " + str(val)
                else:
                    feature_data_get = str(val)

        # for data in capability_data:
        #     for val in data.backlog_team.all():
        #         product_name = product_data_get.split(" | ")
        #         if product_data_get != "":
        #             if str(val.product_parent) not in product_name:
        #                 product_data_get = product_data_get + " | " + str(val.product_parent)


        if request.method == 'POST':
            product_form = ProductForm(request.user, request.session['org_id'], request.POST,instance = product_info)
            if product_form.is_valid():
                product = product_form.save(commit=False)
                ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                product.update_dt = datetime.now()
                product.update_by = ar_user_insta
                product.save()
                product_form.save_m2m()
                msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Update")
                msg_data = msg.notification_desc
                messages.info(request, msg_data)
                return redirect(settings.BASE_URL + "manage-products")
            else:
                messages.error(request, product_form.error)
            return redirect(settings.BASE_URL + "manage-products")
        else:
            product_form = ProductForm(request.user, request.session['org_id'],instance=product_info)
        return render(request, 'admin/manage_product/edit_project.html',{'feature_data_get':feature_data_get,'epic_data_get':epic_data_get,'team_id': id,'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL, 'product_form': product_form})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


def update_table_structure(request,columnnames):
    if  ArShowcolumns.objects.filter(Table_name='AR_PRODUCT').filter(user_id=request.session['user_id']).exists():
        save_column = ArShowcolumns.objects.filter(Table_name='AR_PRODUCT').filter(user_id=request.session['user_id']).update(columnName=columnnames)
    else:
        save_column = ArShowcolumns(Table_name='AR_PRODUCT',user_id=request.session['user_id'],columnName=columnnames,ORG_id=request.session['org_id'])
        save_column.save()
    msg = get_object_or_404(Notification, page_name="View Products", notification_key="Rearrange")
    msg_data = msg.notification_desc
    messages.info(request, msg_data)
    return redirect(settings.BASE_URL + 'products-view')




# ---------------------------------- download start--------------------------------

@csrf_exempt
def get_data_from_database(request):


    if request.method == "POST":

        today_date = date.today()
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        org_name = org_ins.organization_name.split(" ")
        file_name = "We_agileready_database_backup_"+str(org_name[0])+"_"+ str(today_date.day)+"_"+ str(today_date.month) + "_" + str(today_date.year) +".xlsx"
        file_path = 'static/explode_data_files/xlsx/'+file_name
        # table_list = ["Ar_user", "AR_team", "AR_product", "AR_BACKLOG", "AR_EPIC_CAPABILITY", "AR_FEATURE", "ArUserStoryPoints", "AR_USER_STORY", "ArIterations", "ArRole", "ArManageGoals", "ArManageBenefits"]
        table_list = request.POST["tables"].split(",,")
        workbook = xlsxwriter.Workbook(file_path)
        type = request.POST["file_type"]

        # return JsonResponse({'backlog_list':backlog_list})
        get_file_name = ""
        if type == "xlsx":
            get_file_name += ",,"+file_path
        for items in table_list:
            if type == "CSV":
                get_result = create_csv(request,org_ins,org_name[0], items)
                get_file_name += ",,"+str(get_result)
            else:
                worksheet = workbook.add_worksheet(items)
                if items == "AR_PRODUCT":
                    get_ar_product_data(org_ins,worksheet)

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
        table_list = ["AR_PRODUCT"]
        workbook = xlsxwriter.Workbook(file_path)
        # type = request.POST["file_type"]
        type = 'xlsx'
        get_file_name = ""
        if type == "xlsx":
            get_file_name += ",," + file_path
        for items in table_list:
            if type == "CSV":
                get_result = create_csv(org_ins, org_name[0], items)
                get_file_name += ",," + str(get_result)
            else:
                worksheet = workbook.add_worksheet(items)
                if items == "AR_PRODUCT":
                    get_ar_product_data(org_ins, worksheet)

        workbook.close()
        export = export_data_info(folder_name=org_ins.organization_name, files_name=get_file_name)
        export.save()
    # return redirect(settings.BASE_URL+"data-exchange/export-data")
    return JsonResponse({"status":"Done","id":export.id})


def create_csv(request,org_ins,org_name, items):
    today_date = date.today()
    org = org_name+"_"+"ORG"
    date_folder = "Download_" + str(today_date.day)+"_"+ str(today_date.month) + "_" + str(today_date.year)
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

    if items == "AR_PRODUCT":
        get_ar_product_data_CSV2(request,org_ins, file_name)

    return file_name
