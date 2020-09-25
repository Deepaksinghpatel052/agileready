from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from agileproject import settings
from django.http import HttpResponse,JsonResponse
from manage_product.models import AR_team
from manage_product.models import AR_product
from account.models import AR_organization,Ar_user,Notification,csvFilesUplodaded
from django.contrib import messages
from manage_backlogs.models import AR_BACKLOG
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from user_story_points.models import ArUserStoryPoints
from user_story_view.models import AR_USER_STORY
from manage_iterations.models import ArIterations
from manage_role.models import ArRole
from manage_goals.models import ArManageGoals
from manage_benefits.models import ArManageBenefits
from .models import import_files_data,demo_data_csv_template
from manage_product import views as product_view

import xlsxwriter
from datetime import date
from django.views.decorators.csrf import csrf_exempt

from .forms import ImportFilesDataForm
from .models import export_data_info
from manage_product.templatetags import team_data
import pathlib
import csv
import os
import zipfile
from io import StringIO, BytesIO
from  data_import_export.export_data.data_export_ar_user  import get_ar_user_data,get_ar_user_data_csv
from  data_import_export.export_data.data_export_ar_team  import get_ar_team_data,get_ar_team_data_CSV
from  data_import_export.export_data.data_export_ar_product  import get_ar_product_data,get_ar_product_data_CSV
from  data_import_export.export_data.data_export_ar_backlog  import get_ar_backlog_data,get_ar_backlog_data_CSV

from  data_import_export.export_data.data_export_ar_scenario  import get_ar_scenario_data,get_ar_scenario_data_CSV
from ar_scenario.models import AR_SCENARIO

from  data_import_export.export_data.data_export_ar_epic_capability  import get_ar_epic_capability_data,get_ar_epic_capability_data_CSV
from  data_import_export.export_data.data_export_AR_FEATURE  import get_ar_AR_FEATURE_data,get_ar_AR_FEATURE_data_CSV
from  data_import_export.export_data.data_export_ArUserStoryPoints  import get_ar_ArUserStoryPoints_data,get_ar_ArUserStoryPoints_data_CSV
from  data_import_export.export_data.data_export_AR_USER_STORY  import get_AR_USER_STORY_data,get_AR_USER_STORY_data_CSV
from  data_import_export.export_data.data_export_ArIterations  import get_ArIterations_data,get_ArIterations_data_CSV
from  data_import_export.export_data.data_export_ArRole  import get_ArRole_data,get_ArRole_data_CSV
from  data_import_export.export_data.data_export_ArManageGoals  import get_ArManageGoals_data,get_ArManageGoals_data_CSV
from  data_import_export.export_data.data_export_ArManageBenefits  import get_ArManageBenefits_data,get_ArManageBenefits_data_CSV

from data_import_export.import_data.read_csv_file_ar_user import read_ar_user_csv,read_ar_user_csv_text
from data_import_export.import_data.read_csv_file_ar_team import read_ar_team_csv
from data_import_export.import_data.read_csv_file_ar_product import read_ar_product_csv
from data_import_export.import_data.read_csv_file_ar_backlogs import read_ar_backlogs_csv
from data_import_export.import_data.read_csv_file_ar_epic_capability import read_ar_epic_capability_csv
from data_import_export.import_data.read_csv_file_ArRole import read_ArRole_csv
from data_import_export.import_data.read_csv_file_ArManageGoals import read_ArManageGoals_csv
from data_import_export.import_data.read_csv_file_ArManageBenefits import read_ArManageBenefits_csv
from data_import_export.import_data.read_csv_file_ArUserStoryPoints import read_ArUserStoryPoints_csv
from data_import_export.import_data.read_csv_file_read_AR_USER_STORY_csv import read_AR_USER_STORY_csv,read_AR_USER_STORY_csv_test
from data_import_export.import_data.read_csv_file_read_AR_FEATURE_csv import read_AR_FEATURE_csv
from data_import_export.import_data.read_csv_file_read_ArIterations import read_ArIterations_csv
import os
from django.template.defaulttags import register




@csrf_exempt
def get_demo_csv(request):
    status = "0"
    data = ""
    if request.method == "POST":
        csv_for = request.POST["csv_for"]
        if demo_data_csv_template.objects.filter(file_name=csv_for).exists():
            get_data = demo_data_csv_template.objects.get(file_name=csv_for)
            data = get_data.files.url
            status = "1"
    return JsonResponse({"status":csv_for , "data":data})

@register.inclusion_tag('admin/data_import_export/result_data.html')
def get_string_to_table(data_string, *args, **kwargs):
    data_string_in_list = []
    if data_string != "":
        data_string_in_list = data_string.split(",,")
    return {'data_string_in_list': data_string_in_list}


def test_csv_file(request):

    return HttpResponse("test function")


def read_csv_file(request,get_file_list,org_id,user_id,set_data_type,set_dummy_data=""):
    list= get_file_list
    # test(list)
    org_ins = get_object_or_404(AR_organization, id=org_id)
    org_name = org_ins.organization_name.split(" ")

    for val in list:
        file_ins = get_object_or_404(import_files_data, id=val)
        # create error text file code start -------------------
        today_date = date.today()
        org = org_name[0]+"_" + "ORG"
        date_folder = str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year)
        direct_url = 'media/implode_data/errors/' + org
        directry_path_check = pathlib.Path(direct_url)
        if directry_path_check.exists():
            direct_url = direct_url + "/" + date_folder
            directry_path_check = pathlib.Path(direct_url)
            if directry_path_check.exists():
                direct_url = direct_url
            else:
                filet_path = os.mkdir(direct_url)
                direct_url = direct_url
        else:
            filet_path = os.mkdir('media/implode_data/errors/' + org)
            direct_url = 'media/implode_data/errors/' + org + "/" + date_folder
            filet_path = os.mkdir(direct_url)
            direct_url = direct_url
        file_name_text = direct_url + "/" + file_ins.file_name + '.txt'
        file_path = file_ins.files.url
        file_name = file_ins.file_name

        if file_name == "AR_USER":
            print("AR_USER")
            read_ar_user_csv_text(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)

        if file_name == "AR_TEAM":
            print("AR_TEAM")
            read_ar_team_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)

        if file_name == "AR_PRODUCT":
            print("AR_PRODUCT")
            print("------------------------")
            read_ar_product_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
            print("------------------------")
        if file_name == "AR_BACKLOG":
            print("AR_BACKLOG")
            read_ar_backlogs_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
        #
        if file_name == "AR_EPIC_CAPABILITY":
            print("AR_EPIC_CAPABILITY")
            read_ar_epic_capability_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
        #
        if file_name == "AR_ROLE":
            print("AR_ROLE")
            read_ArRole_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)

        if file_name == "AR_GOALS":
            print("AR_GOALS")
            read_ArManageGoals_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
        #
        if file_name == "AR_BENEFITS":
            print("AR_BENEFITS")
            print(file_ins.id)
            read_ArManageBenefits_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
        #
        if file_name == "AR_USER_STORY_POINTS":
            print("AR_USER_STORY_POINTS")
            read_ArUserStoryPoints_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)

        if file_name == "AR_USER_STORY":
            print("AR_USER_STORY")
            read_AR_USER_STORY_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
        # -----------------------------------------------------------------------------------------
        if file_name == "AR_JOB_STORY":
            print("AR_JOB_STORY")
            read_AR_USER_STORY_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
        if file_name == "AR_TEST_STORY":
            print("AR_TEST_STORY")
            read_AR_USER_STORY_csv(request,set_data_type,file_ins,org_ins,file_name, file_name_text,user_id,set_dummy_data)
        #     ------------------------------------------------------------------
        if file_name == "AR_FEATURE":
            print("AR_FEATURE")
            read_AR_FEATURE_csv(request,set_data_type,file_ins, org_ins, file_name, file_name_text, user_id,set_dummy_data)
        if file_name == "AR_ITERATIONS":
            print("AR_ITERATIONS")
            read_ArIterations_csv(request,set_data_type,file_ins, org_ins, file_name, file_name_text, user_id,set_dummy_data)
    return HttpResponse("test function")


# Create your views here.
def export_data(request):
    if product_view.check_permition(request, 'Manage Export Data', 0):
        export_data_status = product_view.check_permition(request, 'Manage Export Data', 1)
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        user = {}
        team = {}
        product = {}
        backlog = {}
        capability = {}
        features = {}
        user_storyes_point = {}
        user_storyes = {}
        iteration = {}
        roles = {}
        goles = {}
        Benefits = {}
        if Ar_user.objects.filter(org_id=org_ins).exists():
            user = Ar_user.objects.filter(org_id=org_ins)
        if AR_team.objects.filter(ORG_id=org_ins).exists():
            team = AR_team.objects.filter(ORG_id=org_ins)
        if AR_product.objects.filter(ORG_ID=org_ins).exists():
            product = AR_product.objects.filter(ORG_ID=org_ins)
        if AR_BACKLOG.objects.filter(ORG_ID=org_ins).exists():
            backlog = AR_BACKLOG.objects.filter(ORG_ID=org_ins)
        if AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).exists():
            capability = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins)
        if AR_FEATURE.objects.filter(ORG_ID=org_ins).exists():
            features = AR_FEATURE.objects.filter(ORG_ID=org_ins)
        if ArUserStoryPoints.objects.filter(ORG_ID=org_ins).exists():
            user_storyes_point = ArUserStoryPoints.objects.filter(ORG_ID=org_ins)
        if AR_USER_STORY.objects.filter(ORG_id=org_ins).exists():
            user_storyes = AR_USER_STORY.objects.filter(ORG_id=org_ins)
        if ArIterations.objects.filter(ORG_ID=org_ins).exists():
            iteration = ArIterations.objects.filter(ORG_ID=org_ins)
        if ArRole.objects.filter(ORG_ID=org_ins).exists():
             roles = ArRole.objects.filter(ORG_ID=org_ins)
        if ArRole.objects.filter(ORG_ID=org_ins).exists():
             roles = ArRole.objects.filter(ORG_ID=org_ins)
        if ArManageGoals.objects.filter(ORG_ID=org_ins).exists():
            goles = ArManageGoals.objects.filter(ORG_ID=org_ins)
        if ArManageBenefits.objects.filter(ORG_ID=org_ins).exists():
            Benefits = ArManageBenefits.objects.filter(ORG_ID=org_ins)
        page_data = [len(user),len(team),len(product),len(backlog),len(capability),len(features),len(user_storyes_point),len(user_storyes),len(iteration),len(roles),len(goles),len(Benefits)
        ]
        page_data_count = {"user":len(user), "team":len(team), "product":len(product),"backlog":len(backlog),"capability":len(capability), "features":len(features),
                     "user_storyes_point":len(user_storyes_point), "user_storyes":len(user_storyes), "iteration":len(iteration), "roles":len(roles), "goles":len(goles), "Benefits":len(Benefits)
                           }
        users_in_array = {0:"user",1:"produu"}

        i = 0
        get_max_length = 0
        print(user[0].user_name)

        for i in page_data:
            if i > get_max_length:
                get_max_length = i
        i = 0
        all_data = []
        for k in range(0,get_max_length):
            row_data = []
            if i < len(user):
                row_data.append(user[i].user_name)
            else:
                row_data.append("")
            if i < len(team):
                row_data.append(team[i].Team_name)
            else:
                row_data.append("")
            if i < len(product):
                row_data.append(product[i].Product_name)
            else:
                row_data.append("")
            if i < len(backlog):
                row_data.append(backlog[i].title)
            else:
                row_data.append("")
            if i < len(capability):
                row_data.append(capability[i].Cepic_key)
            else:
                row_data.append("")
            if i < len(features):
                row_data.append(features[i].Feature_key)
            else:
                row_data.append("")
            if i < len(user_storyes_point):
                row_data.append(user_storyes_point[i].Point_Key)
            else:
                row_data.append("")
            if i < len(user_storyes):
                row_data.append(user_storyes[i].title)
            else:
                row_data.append("")
            if i < len(iteration):
                row_data.append(iteration[i].IterationName)
            else:
                row_data.append("")
            if i < len(roles):
                row_data.append(roles[i].title)
            else:
                row_data.append("")
            if i < len(goles):
                row_data.append(goles[i].Goal_title)
            else:
                row_data.append("")
            if i < len(Benefits):
                row_data.append(Benefits[i].Benefits_title)
            else:
                row_data.append("")
            all_data.append(row_data)
            i += 1
        return render(request, 'admin/data_import_export/export.html', { 'export_data_status':export_data_status, "page_data_count":page_data_count,"all_data":all_data, "page_data":page_data,"get_max_length":get_max_length,"team":team,"BASE_URL": settings.BASE_URL,'user_name':request.session['user_name']})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized",notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})




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
                get_result = create_csv(org_ins,org_name[0], items)
                get_file_name += ",,"+str(get_result)
            else:
                worksheet = workbook.add_worksheet(items)
                if items == "AR_USER":
                    get_ar_user_data(org_ins,worksheet)
                if items == "AR_TEAM":
                    get_ar_team_data(org_ins,worksheet)
                if items == "AR_PRODUCT":
                    get_ar_product_data(org_ins,worksheet)
                if items == "AR_BACKLOG":
                    get_ar_backlog_data(org_ins,worksheet)

                if items == "AR_SCENARIO":
                    get_ar_scenario_data(org_ins, worksheet)

                if items == "AR_EPIC_CAPABILITY":
                    get_ar_epic_capability_data(org_ins,worksheet)
                if items == "AR_FEATURE":
                    get_ar_AR_FEATURE_data(org_ins, worksheet)
                if items == "AR_USER_STORY_POINTS":
                    get_ar_ArUserStoryPoints_data(org_ins, worksheet)
                if items == "AR_USER_STORY":
                    get_AR_USER_STORY_data(org_ins, worksheet)
                if items == "AR_ITERATIONS":
                    get_ArIterations_data(org_ins, worksheet)
                if items == "AR_ROLE":
                    get_ArRole_data(org_ins, worksheet)
                if items == "AR_GOALS":
                    get_ArManageGoals_data(org_ins, worksheet)
                if items == "AR_BENEFITS":
                    get_ArManageBenefits_data(org_ins, worksheet)
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
        table_list = ["AR_USER", "AR_TEAM", "AR_PRODUCT", "AR_BACKLOG","AR_SCENARIO", "AR_EPIC_CAPABILITY", "AR_FEATURE",
                      "AR_USER_STORY_POINTS", "AR_USER_STORY", "AR_ITERATIONS", "AR_ROLE", "AR_GOALS",
                      "AR_BENEFITS"]
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
                if items == "AR_USER":
                    get_ar_user_data(org_ins, worksheet)
                if items == "AR_TEAM":
                    get_ar_team_data(org_ins, worksheet)
                if items == "AR_PRODUCT":
                    get_ar_product_data(org_ins, worksheet)
                if items == "AR_BACKLOG":
                    get_ar_backlog_data(org_ins, worksheet)

                #     -----------------------------------------------
                if items == "AR_SCENARIO":
                    get_ar_scenario_data(org_ins,worksheet)
                #     =============================================

                if items == "AR_EPIC_CAPABILITY":
                    get_ar_epic_capability_data(org_ins, worksheet)
                if items == "AR_FEATURE":
                    get_ar_AR_FEATURE_data(org_ins, worksheet)
                if items == "AR_USER_STORY_POINTS":
                    get_ar_ArUserStoryPoints_data(org_ins, worksheet)
                if items == "AR_USER_STORY":
                    get_AR_USER_STORY_data(org_ins, worksheet)
                if items == "AR_ITERATIONS":
                    get_ArIterations_data(org_ins, worksheet)
                if items == "AR_ROLE":
                    get_ArRole_data(org_ins, worksheet)
                if items == "AR_GOALS":
                    get_ArManageGoals_data(org_ins, worksheet)
                if items == "AR_BENEFITS":
                    get_ArManageBenefits_data(org_ins, worksheet)
        workbook.close()
        export = export_data_info(folder_name=org_ins.organization_name, files_name=get_file_name)
        export.save()
    # return redirect(settings.BASE_URL+"data-exchange/export-data")
    return JsonResponse({"status":"Done","id":export.id})


def create_csv(org_ins,org_name, items):
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
    if items == "AR_USER":
        get_ar_user_data_csv(org_ins, file_name)


    if items == "AR_TEAM":
        get_ar_team_data_CSV(org_ins, file_name)

    if items == "AR_PRODUCT":
        get_ar_product_data_CSV(org_ins, file_name)

    if items == "AR_BACKLOG":
        get_ar_backlog_data_CSV(org_ins, file_name)

    #     -----------------------------------------------
    if items == "AR_SCENARIO":
        get_ar_scenario_data_CSV(org_ins, file_name)
    #     =============================================

    if items == "AR_EPIC_CAPABILITY":
        get_ar_epic_capability_data_CSV(org_ins, file_name)

    if items == "AR_FEATURE":
        get_ar_AR_FEATURE_data_CSV(org_ins, file_name)

    if items == "AR_USER_STORY_POINTS":
        get_ar_ArUserStoryPoints_data_CSV(org_ins, file_name)

    if items == "AR_USER_STORY":
        get_AR_USER_STORY_data_CSV(org_ins, file_name)

    if items == "AR_ITERATIONS":
        get_ArIterations_data_CSV(org_ins, file_name)
    if items == "AR_ROLE":
        get_ArRole_data_CSV(org_ins, file_name)

    if items == "AR_GOALS":
        get_ArManageGoals_data_CSV(org_ins, file_name)

    if items == "AR_BENEFITS":
        get_ArManageBenefits_data_CSV(org_ins, file_name)

    return file_name


def file_download(request,id):
    get_files = export_data_info.objects.get(id=id)
    files_name = get_files.files_name.split(",,")
    filenames = []
    i = 0
    for file in files_name:
        if i > 0:
            filenames.append(file)
        i += 1
    print(filenames)
    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
    org_name = org_ins.organization_name.split(" ")
    today_date = date.today()
    zip_subdir = str(org_name[0])+"_ORG_"+str(today_date.day) + "_" + str(today_date.month) + "_" + str(today_date.year)
    zip_filename = "%s.zip" % zip_subdir
    buffer = BytesIO()
    zf = zipfile.ZipFile(buffer, "w")
    for fpath in filenames:
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)
        zf.write(fpath, zip_path)
    zf.close()
    resp = HttpResponse(buffer.getvalue(), content_type = "application/pdf")
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    return resp


def add_csv_files(request):
    upload_file = request.FILES.getlist('files')
    print(upload_file)
    # check_file_type = True
    #---------------------------   check file type & name start -------------------------------#
    for file in upload_file:
        print(file)
        print()
        if not file.name.endswith('.csv'):
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
            # check_file_type = False
            return redirect(settings.BASE_URL + "data-exchange/import-data")
        list_of_filename = ('AR_BACKLOG', 'AR_EPIC_CAPABILITY', 'AR_FEATURE', 'AR_PRODUCT', 'AR_TEAM', 'AR_USER','AR_USER_STORY', 'AR_ITERATIONS', 'AR_BENEFITS', 'AR_GOALS', 'AR_ROLE','AR_USER_STORY_POINTS','AR_JOB_STORY','AR_TEST_STORY',)
        file_name_val = str(file).split(".")

        if file_name_val[0] not in list_of_filename:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid Name")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
            return redirect(settings.BASE_URL + "data-exchange/import-data")
        print(file_name_val)
    #---------------------------   check file type & name stop -------------------------------#
    #---------------------------   File Save start -------------------------------#
    file_ids = []
    file_save_status = True
    for file in upload_file:
        # instance for user and organizations start -----------
        created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        # instance for user and organizations stop -----------
        file_name_val = str(file).split(".")

        # set priyorty START
        pry = 0
        if file_name_val[0] == "AR_USER":
            pry = 1
        if file_name_val[0] == "AR_TEAM":
            pry = 2
        if file_name_val[0] == "AR_PRODUCT":
            pry = 3
        if file_name_val[0] == "AR_BACKLOG":
            pry = 4
        if file_name_val[0] == "AR_EPIC_CAPABILITY":
            pry = 5
        if file_name_val[0] == "AR_ROLE":
            pry = 6
        if file_name_val[0] == "AR_GOALS":
            pry = 7
        if file_name_val[0] == "AR_BENEFITS":
            pry = 8
        if file_name_val[0] == "AR_USER_STORY_POINTS":
            pry = 9
        if file_name_val[0] == "AR_USER_STORY":
            pry = 10
        if file_name_val[0] == "AR_FEATURE":
            pry = 11
        if file_name_val[0] == "AR_ITERATIONS":
            pry = 12
        if file_name_val[0] == "AR_JOB_STORY":
            pry = 13
        if file_name_val[0] == "AR_TEST_STORY":
            pry = 14

        # set priyorty END



        data = import_files_data(files=file, file_name=file_name_val[0], ORG_ID=org_ins, created_by=created_by_ins,priority=pry)
        # print(data.id)
        try:
            data.save()
            file_ids.append(data.id)
            # msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
            # msg_data = msg.notification_desc
            # messages.info(request, msg_data)
        except IntegrityError:
            file_save_status = False
            # msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
            # msg_data = msg.notification_desc
            # messages.error(request, msg_data)
            set_statue = urlsafe_base64_encode(force_bytes("error"))
            # ---------------------------   File Save stop -------------------------------#
            # return redirect(settings.BASE_URL + "data-exchange/import-data")
    num = 0
    if file_save_status :
        print(file_ids)
        get_all_files = import_files_data.objects.filter(id__in=file_ids).order_by("priority")
        get_file_ids = []

        for items in get_all_files:
            get_file_ids.append(items.id)
        read_csv_file(request,get_file_ids, request.session['org_id'], request.session['user_id'],'')


        # msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
        # msg_data = msg.notification_desc
        # messages.info(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    # return HttpResponse(get_file_ids)

    return redirect(settings.BASE_URL + "data-exchange/import-data")


def import_data(request):
    if product_view.check_permition(request, 'Manage Import Data', 0):
        import_data_status = product_view.check_permition(request, 'Manage Import Data', 1)
        ImportFilesDataFormUse = ImportFilesDataForm()
        org_id = request.session['org_id']
        org_ins = get_object_or_404(AR_organization, id=org_id)
        if import_files_data.objects.filter(ORG_ID=org_ins).exists():
            get_data = import_files_data.objects.filter(ORG_ID=org_ins).order_by("-id")
        else:
            get_data = {}

        get_dommy_data = demo_data_csv_template.objects.order_by("priority")
        return render(request, 'admin/data_import_export/import.html', {'user_name':request.session['user_name'],'get_dommy_data':get_dommy_data,'import_data_status':import_data_status,'get_data':get_data,'ImportFilesDataFormUse':ImportFilesDataFormUse,"BASE_URL": settings.BASE_URL,'user_name':request.session['user_name']})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized",notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})





def download(request,id):
    get_files = import_files_data.objects.get(id=id)
    error_log= settings.BASE_URL+"media" + str(get_files.error_log)


    response = HttpResponse(open("media" + str(get_files.error_log), 'rb').read())
    response['Content-Type'] = 'text/plain'
    response['Content-Disposition'] = 'attachment; filename=Import Errors.txt'
    return response
