from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .forms import Ar_User_Story_Form
from .filters import UserStoryViewFilter
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text
from account.models import Ar_user,AR_organization,ArShowcolumns,csvFilesUplodaded,Notification,ArUserStoryScoringPoints
from account.forms import csvFilesUplodadedForm
from .models import AR_USER_STORY,file_attachment,AR_US_STATUS,AR_US_TYPE,Help_Text
from .set_user_story_acceptance_criteria_and_conver_algo import flesch_reading_ease,flesch_reading_ease_conversations
from manage_product.models import AR_product,AR_team
from django.contrib import messages
from datetime import datetime
from manage_role.models import ArRole
from manage_benefits.models import ArManageBenefits
from manage_goals.models import ArManageGoals
from manage_backlogs.models import AR_BACKLOG
# -----------------------------------------------------
from business_value.models import AR_BUSINESS_VALUE

from agileproject.serializers import Help_Text_Serializer


# -----------------------------------------------------
import csv, io, os
from manage_product import views as product_view
from manage_product import views as product_view
from user_story_view.user_story_score.readiness_quality_score import quelity_score
from django.db.models import Q
from dashboard.views import get_package_limit

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

import xlsxwriter
import pathlib
import os
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime,date
from django.http import HttpResponse,JsonResponse
from data_import_export.models import export_data_info

from  data_import_export.export_data.data_export_AR_USER_STORY  import get_AR_USER_STORY_data,get_AR_USER_STORY_data_CSV,get_AR_USER_STORY_data_CSV2


# Create your views here.

def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        data =  quelity_score(check_map)
        return JsonResponse({'check_project': data[0], 'conjunction_set_val': data[1]})
    return JsonResponse({'check_project': 0, 'conjunction_set_val':0})

def BacklogGoodnessScore(request,backlog_id=0,product_id=0):
    # set backlog number START
    if backlog_id != 0:
        get_backlog_instance = get_object_or_404(AR_BACKLOG,pk=backlog_id)
        get_total_user_story_score = 0
        get_total_user_story = 0
        get_bacolog_size = 0
        all_user_storyes = AR_USER_STORY.objects.filter(backlog_parent=get_backlog_instance)

        get_total_user_story = all_user_storyes.count()
        for data in all_user_storyes:
            get_total_user_story_score  += data.readiness_quality_score
            if data.story_points != None:
                get_bacolog_size += data.story_points.Point_score
        if get_total_user_story > 0:
            get_total_user_story_score = get_total_user_story_score/get_total_user_story
        get_backlog_instance.backlog_score = get_total_user_story_score
        get_backlog_instance.Backlog_size = get_bacolog_size
        get_backlog_instance.save()
        # set backlog number END
    #=============================== SET SCORE FOR BRODUCT START ================
    if product_id == 0:
        get_product_instance = get_object_or_404(AR_product,pk=get_backlog_instance.product_parent.id)
    else:
        get_product_instance = get_object_or_404(AR_product, pk=product_id)

    get_all_backlog = AR_BACKLOG.objects.filter(product_parent=get_product_instance)
    product_size = 0
    product_score = 0
    total_backlog_count = get_all_backlog.count()
    for bl_data in get_all_backlog:
        product_size += bl_data.Backlog_size
        product_score += bl_data.backlog_score
    if total_backlog_count > 0:
        product_score = product_score/total_backlog_count
    get_product_instance.Product_size = product_size
    get_product_instance.Product_score = product_score
    get_product_instance.save()
    # =============================== SET SCORE FOR BRODUCT END ================
    return HttpResponse("True")


@csrf_exempt
def get_file_data(request):
    id = force_text(urlsafe_base64_decode(request.POST["csv_id"]))
    file_name = ""
    if csvFilesUplodaded.objects.filter(id=id).exists():
        get_file = csvFilesUplodaded.objects.get(id=id)
        if get_file.ORG_ID.id != request.session['org_id']:
            messages.error(request, 'This CSV file is not related to your organization.')
        file_name = get_file.attachments
        data_set = file_name.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)
        get_data = csv.reader(io_string, delimiter=',', quotechar="|")
        file_name =  get_data
    else:
        messages.error(request, 'File id is invald')
    return render(request, 'admin/user_story_view/file_data.html',{'date':datetime.now(),'id':id,"file_name":file_name})

def add_csv_files(request):
    if request.method == "POST":
        csv_file = request.FILES['attachments']
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')
            set_statue = urlsafe_base64_encode(force_bytes("error"))
        else:
            csvFilesUplodadedForm_get = csvFilesUplodadedForm(request.POST, request.FILES)
            if csvFilesUplodadedForm_get.is_valid():
                data = csvFilesUplodadedForm_get.save(commit=False)
                created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
                org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
                data.csvUseFor = "Ar User Story"
                data.created_by = created_by_ins
                data.updated_by = created_by_ins
                data.ORG_ID = org_ins
                try:
                    data.save()
                    messages.info(request, "User Story CSV Uploded successfully !")
                    set_statue = urlsafe_base64_encode(force_bytes("done"))
                    csv_id = urlsafe_base64_encode(force_bytes(data.id))
                    return redirect(settings.BASE_URL + 'user-story-view')
                except IntegrityError:
                    messages.error(request, "Some thing was wrong !")
                    set_statue = urlsafe_base64_encode(force_bytes("error"))
            else:
                messages.error(request, csvFilesUplodadedForm_get.errors)
    return redirect(settings.BASE_URL + 'user-story-view')




# Create your views here.
def index(request,set_statue="",set_statue_2="",csv_id=""):
    if product_view.check_permition(request, 'User Story View', 0):


        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])

        filters1 = Q(ORG_id=org_ins )
        filters2 = Q(ORG_id=org_ins )
        filters3 = Q(ORG_id=org_ins )
        filters4 = Q(ORG_id=org_ins )
        # filters = Q(ORG_id=org_ins )

        business_value_token = ""
        backlog_token= ""
        user_type_token= ""
        user_status_token= ""

        if 'backlog-parent' in request.GET:
            if request.GET['backlog-parent'] is not None:
                if request.GET['backlog-parent'] == "none":
                    filters1 = filters1 & Q(backlog_parent__backlog_slug__exact=request.GET['backlog-parent']) | Q(backlog_parent__backlog_slug__isnull=True)
                else:

                    filters1 = filters1 & Q(backlog_parent__backlog_slug__exact=request.GET['backlog-parent'])
                backlog_token = request.GET['backlog-parent']

        if 'business-value' in request.GET:
            if request.GET['business-value'] is not None:
                if request.GET['business-value'] == "none":
                    filters2 = filters2 & Q(BV_ID__business_value_slug__exact=request.GET['business-value']) | Q(BV_ID__business_value_slug__isnull=True)
                else:
                    filters2 = filters2 & Q(BV_ID__business_value_slug__exact=request.GET['business-value'])
                business_value_token = request.GET['business-value']

        if 'user-status' in request.GET:
            if request.GET['user-status'] is not None:
                if request.GET['user-status'] == "none":
                    filters3 = filters3 & Q(user_story_status__user_status_slug__exact=request.GET['user-status']) | Q(user_story_status__user_status_slug__isnull=True)
                else:
                    filters3 = filters3 & Q(user_story_status__user_status_slug__exact=request.GET['user-status'])
                user_status_token = request.GET['user-status']

        if 'user-type' in request.GET:
            if request.GET['user-type'] is not None:
                if request.GET['user-type'] == "none":
                    filters4 = filters4 & Q(UST_ID__user_type_slug__exact=request.GET['user-type']) | Q(UST_ID__user_type_slug__isnull=True)
                else:
                    filters4 = filters4 & Q(UST_ID__user_type_slug__exact=request.GET['user-type'])
                user_type_token = request.GET['user-type']



        if AR_USER_STORY.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).exists():
            get_user_story = AR_USER_STORY.objects.filter(filters1).filter(filters2).filter(filters3).filter(filters4).order_by("-id").filter(~Q(title = 'None'))
        else:
            get_user_story = {}


        if ArShowcolumns.objects.filter(Table_name='AR_USER_STORY').filter(user_id=request.session['user_id']).exists():
            show_column = ArShowcolumns.objects.filter(Table_name='AR_USER_STORY').filter(user_id=request.session['user_id'])
            get_show_column = show_column[0].columnName.split(",")
        else:
            get_show_column = {}
        all_column_list = {
            "backlog_parent": "Backlog Parent",
            "BV_ID": "Business Value",
            "owner":"Owner",
            "title":"Title",
            "story_tri_part_text":"Story Tri Part Text",
            "acceptance_criteria":"Acceptance Criteria",
            "ac_readability_score":"Ac Readability Score",
            "conversation":"Conversation",
            "convo_readability_score":"Convo Readability Score",
            "attachments":"Attachments",
            "autoscoring_on":"Autoscoring On",
            "archive_indicator":"Archive Indicator",
            "readiness_quality_score":"Readiness Quality Score",
            "story_points":"Story Points",
            "user_story_status":"User Story Status",
            "ORG_id":"ORG Name",
            "UST_ID":"User Story Type",
            "ar_user":"Ar User",
            "created_by":"Created By",
            "created_dt":"Created Date",
            "updated_by":"Updated_By",
            "updated_dt":"Updated Date"
        }
        csvFilesUplodadedForm_get = csvFilesUplodadedForm()
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Copy_Story")
        Copy_Story_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Copy_Request")
        Copy_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Rearrange_Request")
        Rearrange_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        user_story_view_status = product_view.check_permition(request, 'User Story View', 1)





        user_stroy_list = AR_USER_STORY.objects.filter(ORG_id=org_ins).order_by("-id").filter(~Q(title = 'None'))
        user_stroy_filter = UserStoryViewFilter(request.GET, queryset=user_stroy_list)

        # -----------------------------------------
        backlog_data = AR_BACKLOG.objects.filter(ORG_ID=org_ins).order_by("backlog_slug")
        business_value_data = AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_ins).order_by("business_value_slug")
        user_status_data = AR_US_STATUS.objects.all().order_by("user_status_slug")
        user_type_data = AR_US_TYPE.objects.all().order_by("user_type_slug")



        # -----------------------------------------

        return render(request, 'admin/user_story_view/index.html',{'user_type_token':user_type_token,'user_status_token':user_status_token,'business_value_token':business_value_token,'backlog_token':backlog_token,'user_type_data':user_type_data,'user_status_data':user_status_data,'business_value_data':business_value_data,'backlog_data':backlog_data,'user_stroy_filter':user_stroy_filter,'user_story_view_status':user_story_view_status,'Copy_Story_msg':Copy_Story_msg,'Copy_Request_msg':Copy_Request_msg,'Rearrange_Request_msg':Rearrange_Request_msg,'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'date':datetime.now(),'csv_id':csv_id,'set_statue':set_statue,'set_statue_2':set_statue_2,'csvFilesUplodadedForm':csvFilesUplodadedForm_get,'all_column_list':all_column_list,'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL,'get_user_story':get_user_story,"get_show_column":get_show_column})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

# ---------------------------------------------
def filter(request,backlog_token,business_value_token,user_status_token,user_type_token,set_statue="",set_statue_2="",csv_id=""):



    if product_view.check_permition(request, 'User Story View', 0):
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])


        # ------------------------------------------------------------------
        backlog_token = backlog_token.replace("+", " ")
        business_value_token = business_value_token.replace("+", " ")
        user_status_token = user_status_token.replace("+", " ")
        user_type_token = user_type_token.replace("+", " ")



        if backlog_token == "all_backlog":
            backlog_token_name = backlog_token
            Q1 = Q(backlog_parent__in=AR_BACKLOG.objects.filter(ORG_ID=org_ins))
        else:
            filter_backlog_ins = get_object_or_404(AR_BACKLOG, id=backlog_token, ORG_ID=org_ins)
            backlog_token_name = filter_backlog_ins.title
            Q1=  Q(backlog_parent=filter_backlog_ins)

        if business_value_token == "all_business_value":
            business_value_token_name = business_value_token
            Q2 = Q(BV_ID__in=AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_ins))
        else:
            filter_team_ins = get_object_or_404(AR_BUSINESS_VALUE, id=business_value_token, ORG_ID=org_ins)
            business_value_token_name = filter_team_ins.bus_value_txt_code
            Q2 = Q(BV_ID=filter_team_ins)

        if user_status_token == "all_user_status":
            user_status_token_name = user_status_token
            Q3 = Q(user_story_status__in=AR_US_STATUS.objects.all())
        else:
            filter_user_status_ins = get_object_or_404(AR_US_STATUS, id=user_status_token)
            user_status_token_name = filter_user_status_ins.status_key
            Q3=  Q(user_story_status=filter_user_status_ins)

        if user_type_token == "all_user_type":
            user_type_token_name = user_type_token
            Q4 = Q(UST_ID__in=AR_US_TYPE.objects.all())
        else:
            filter_user_type_ins = get_object_or_404(AR_US_TYPE, id=user_type_token)
            user_type_token_name = filter_user_type_ins.type_key
            Q4 = Q(UST_ID=filter_user_type_ins)



        if AR_USER_STORY.objects.filter(ORG_id=org_ins).exists():
            get_user_story = AR_USER_STORY.objects.filter(ORG_id=org_ins).filter(Q1).filter(Q2).filter(Q3).filter(Q4).order_by("-id").filter(~Q(title = 'None'))
        else:
            get_user_story = {}
        # =======================================================


        if ArShowcolumns.objects.filter(Table_name='AR_USER_STORY').filter(user_id=request.session['user_id']).exists():
            show_column = ArShowcolumns.objects.filter(Table_name='AR_USER_STORY').filter(user_id=request.session['user_id'])
            get_show_column = show_column[0].columnName.split(",")
        else:
            get_show_column = {}
        all_column_list = {
            "backlog_parent": "Backlog Parent",
            "BV_ID": "Business Value",
            "owner":"Owner",
            "title":"Title",
            "story_tri_part_text":"Story Tri Part Text",
            "acceptance_criteria":"Acceptance Criteria",
            "ac_readability_score":"Ac Readability Score",
            "conversation":"Conversation",
            "convo_readability_score":"Convo Readability Score",
            "attachments":"Attachments",
            "autoscoring_on":"Autoscoring On",
            "archive_indicator":"Archive Indicator",
            "readiness_quality_score":"Readiness Quality Score",
            "story_points":"Story Points",
            "user_story_status":"User Story Status",
            "ORG_id":"ORG Name",
            "UST_ID":"User Story Type",
            "ar_user":"Ar User",
            "created_by":"Created By",
            "created_dt":"Created Date",
            "updated_by":"Updated_By",
            "updated_dt":"Updated Date"
        }
        csvFilesUplodadedForm_get = csvFilesUplodadedForm()
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Copy_Story")
        Copy_Story_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Copy_Request")
        Copy_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Rearrange_Request")
        Rearrange_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        user_story_view_status = product_view.check_permition(request, 'User Story View', 1)

        user_stroy_list = AR_USER_STORY.objects.filter(ORG_id=org_ins).order_by("-id").filter(~Q(title = 'None'))
        user_stroy_filter = UserStoryViewFilter(request.GET, queryset=user_stroy_list)

        # -----------------------------------------
        backlog_data = AR_BACKLOG.objects.filter(ORG_ID=org_ins)
        business_value_data = AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_ins)
        user_status_data = AR_US_STATUS.objects.all()
        user_type_data = AR_US_TYPE.objects.all()
        # -----------------------------------------

        return render(request, 'admin/user_story_view/index.html',{'user_type_token':user_type_token_name,'user_status_token':user_status_token_name,'business_value_token':business_value_token_name,'backlog_token':backlog_token_name,'user_type_data':user_type_data,'user_status_data':user_status_data,'business_value_data':business_value_data,'backlog_data':backlog_data,'user_stroy_filter':user_stroy_filter,'user_story_view_status':user_story_view_status,'Copy_Story_msg':Copy_Story_msg,'Copy_Request_msg':Copy_Request_msg,'Rearrange_Request_msg':Rearrange_Request_msg,'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'date':datetime.now(),'csv_id':csv_id,'set_statue':set_statue,'set_statue_2':set_statue_2,'csvFilesUplodadedForm':csvFilesUplodadedForm_get,'all_column_list':all_column_list,'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL,'get_user_story':get_user_story,"get_show_column":get_show_column})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

# ---------------------------------------------
def add_user_story_view(request):
    if product_view.check_permition(request, 'User Story View', 1):
        user_id = request.session['user_id']
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        Ar_Manage_Benefits = ArManageBenefits.objects.filter(ORG_ID=org_ins)

        Ar_Manage_Goals = ArManageGoals.objects.filter(ORG_ID=org_ins)
        Ar_Role = ArRole.objects.filter(ORG_ID=org_ins)
        if request.method == "POST":
            str_part = request.POST["str_part"]
            ar_user_story_form = Ar_User_Story_Form(user_id,request.session['org_id'], request.POST, request.FILES)

            if ar_user_story_form.is_valid():

                title = ar_user_story_form.cleaned_data.get('title')
                backlog_parent = ar_user_story_form.cleaned_data.get('backlog_parent')
                story_tri_part_text = ar_user_story_form.cleaned_data.get('story_tri_part_text')
                if str_part != "":
                    story_tri_part_text = str_part
                if AR_USER_STORY.objects.filter(title=title).filter(ORG_id=request.session['org_id']).exists():
                    msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request,title +" , " + msg_data)
                else:
                    # backlog = AR_BACKLOG.objects.get(title=backlog_parent)
                    # if backlog.children_us_list == "":
                    #     child_us_list = title
                    # else:
                    #     child_us_list = backlog.children_us_list + " | " + title
                    # AR_BACKLOG.objects.filter(title=backlog_parent).update(children_us_list=child_us_list)


                    data = ar_user_story_form.save(commit=False)
                    created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
                    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
                    data.story_tri_part_text = story_tri_part_text
                    data.ORG_id = org_ins
                    data.created_by = created_by_ins
                    data.updated_by = created_by_ins
                    try:
                        get_status = get_package_limit(request.session['org_id'],"User_Stories")
                        if get_status:
                            data.save()

                            # data = request.FILES.getlist('attachments')
                            # for a in data:
                            #
                            data123 = request.FILES.getlist('attachments')  # or self.files['image'] in your form
                            valu=""
                            for a in data123:

                                path = default_storage.save('attachments/' + str(a), ContentFile(a.read()))
                                os.path.join(settings.MEDIA_ROOT, path)

                            #     # valu = valu + " " +str(a)
                            #     data.attachments = 'attachments/' + str(a)

                                activitydata = file_attachment(name=str(a), attachment='attachments/' + str(a),
                                                                        user_story=data)
                                activitydata.save()



                            # BacklogGoodnessScore(request,request.POST["backlog_parent"])
                            msg = get_object_or_404(Notification, page_name="User Story View",notification_key="Add")
                            msg_data = msg.notification_desc
                            messages.info(request, msg_data)


                        else:
                            msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                            msg_data = msg.notification_desc
                            messages.error(request, msg_data)

                            return redirect(settings.BASE_URL + 'user-story-view/add-new')


                        return redirect(settings.BASE_URL + 'user-story-view')
                    except():
                    # except IntegrityError:
                        messages.error(request, "Some thing was wrong !")
                        return redirect(settings.BASE_URL + 'user-story-view/add-new')
                return redirect(settings.BASE_URL+"user-story-view")
            else:
                messages.error(request,  ar_user_story_form.errors)
                return redirect(settings.BASE_URL + 'user-story-view/add-new')
        else:
            val=request.session['org_id']
            # return HttpResponse(org_ins)
            ar_user_story_form = Ar_User_Story_Form(user_id,org_ins)

            help_text = Help_Text.objects.all()


        return render(request, 'admin/user_story_view/add-user-story.html',{'help_text':help_text,'Ar_Manage_Benefits':Ar_Manage_Benefits,'Ar_Manage_Goals':Ar_Manage_Goals,'Ar_Role':Ar_Role,'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL,"ar_user_story_form":ar_user_story_form})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


def edit_user_story_view(request,id):
    if product_view.check_permition(request, 'User Story View', 1):
        user_id1 = request.session['user_id']
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        Ar_Manage_Benefits = ArManageBenefits.objects.filter(ORG_ID=request.session['org_id'])
        Ar_Manage_Goals = ArManageGoals.objects.filter(ORG_ID=request.session['org_id'])
        Ar_Role = ArRole.objects.filter(ORG_ID=request.session['org_id'])
        ar_user_story_form = AR_USER_STORY.objects.get(id=id)
        user_id=ar_user_story_form.id
        org_info = AR_organization.objects.filter(id=request.session['org_id'])

        get_instance = get_object_or_404(AR_USER_STORY, pk=id)
        attachment_data = file_attachment.objects.filter(user_story=get_instance)
        attachment_data_count = file_attachment.objects.filter(user_story=get_instance).count()
        Remove_Request_msg = "Do you want to remove this attachment ?"
        Remove_done_msg = "Attachment removed successfully."
        Not_Remove_msg = "Attachment not removed."
        if request.method == "POST":
            str_part = request.POST["str_part"]
            ar_user_story_form = Ar_User_Story_Form(user_id1, org_ins, data=(request.POST or None),files=(request.FILES or None),instance = ar_user_story_form)
            if ar_user_story_form.is_valid():
                story_tri_part_text = ar_user_story_form.cleaned_data.get('story_tri_part_text')
                if str_part != "":
                    story_tri_part_text = str_part
                else:
                    story_tri_part_text = story_tri_part_text

                data = ar_user_story_form.save(commit=False)
                created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
                data.updated_by = created_by_ins

                data.story_tri_part_text = story_tri_part_text
                data.updated_dt = datetime.now()

                # data123 = request.FILES.getlist('attachments')  # or self.files['image'] in your form
                # valu=""
                # for a in data123:
                #     # valu = valu + " " +str(a)
                #     data.attachments = 'attachments/' + str(a)

                try:
                    get_old_instance = get_object_or_404(AR_USER_STORY,pk=id)
                    data.save()

                    get_instance = get_object_or_404(AR_USER_STORY, pk=id)
                    # file_attachment.objects.filter(user_story=get_instance).delete()

                    data123 = request.FILES.getlist('attachments')  # or self.files['image'] in your form

                    for a in data123:
                        path = default_storage.save('attachments/' + str(a), ContentFile(a.read()))
                        os.path.join(settings.MEDIA_ROOT, path)

                        activitydata = file_attachment(name=str(a), attachment='attachments/' + str(a),
                                                       user_story=data)
                        activitydata.save()

                    # data = request.FILES.getlist('attachments')
                    # for a in data:
                    #     path = default_storage.save('attachments/'+ str(a) , ContentFile(a.read()))
                    #     os.path.join(settings.MEDIA_ROOT, path)



                    # data.save_m2m()

                    # BacklogGoodnessScore(request, request.POST["backlog_parent"])    # SET numbers for new instance
                    # BacklogGoodnessScore(request, get_old_instance.backlog_parent.id) # SET numbers for old instance
                    msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                    return redirect(settings.BASE_URL + 'user-story-view')
                except():
                # except IntegrityError:
                    messages.error(request, "Some thing was wrong !")
                return redirect(settings.BASE_URL + 'user-story-view')
            else:
                messages.error(request,  ar_user_story_form.errors)
        else:
            ar_user_story_form = Ar_User_Story_Form(user_id1, org_ins,instance=ar_user_story_form)

        return render(request, 'admin/user_story_view/edit-user-story.html',{'Not_Remove_msg':Not_Remove_msg,'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'attachment_data_count':attachment_data_count,'attachment_data':attachment_data,'Ar_Role':Ar_Role,'Ar_Manage_Goals':Ar_Manage_Goals,'Ar_Manage_Benefits':Ar_Manage_Benefits,'date':datetime.now(),'user_name':request.session['user_name'],'user_id':user_id,'ar_user_story_form':ar_user_story_form,'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


def remove_story_file(request,id):
    get_instance = get_object_or_404(file_attachment, pk=id)
    user_story = get_instance.user_story_id


    file_attachment.objects.filter(pk=id).delete()
    msg_data = "Attachment removed successfully."
    messages.info(request, msg_data)
    return redirect(settings.BASE_URL + 'user-story-view/edit-story/' + str(user_story))

# ------------------------------------------------------------------
def delete_user_story_view(request,id):
    if product_view.check_permition(request, 'User Story View', 1):
        try:
            get_instance = get_object_or_404(AR_USER_STORY,pk=id)
            AR_USER_STORY.objects.get(id=id).delete()
            # BacklogGoodnessScore(request, get_instance.backlog_parent.id)
            msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
            return redirect(settings.BASE_URL + 'user-story-view')
        # except(TypeError, OverflowError):
        except(TypeError, OverflowError):
            msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'user-story-view')

# ------------------------------------------------------------------


def select_user_story_view(request,ids):
    if product_view.check_permition(request, 'User Story View', 1):
        get_ids = ids.split(",")
        for id in get_ids:
            if AR_USER_STORY.objects.filter(id=id).exists():
                get_status = get_package_limit(request.session['org_id'],"User_Stories")
                if get_status:
                    get_data_object =  AR_USER_STORY.objects.get(pk=id)
                    get_data_object.pk = None
                    get_data_object.data_Type = "ORG Data"
                    get_data_object.save()

                    get_instance = get_object_or_404(AR_USER_STORY, pk=id)
                    # BacklogGoodnessScore(request, get_instance.backlog_parent.id)
                    messages.info(request, str(get_data_object.title)+" Copy created successfully !")
                else:
                    msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                    msg_data = msg.notification_desc
                    messages.error(request, msg_data)      
            else:
                messages.error(request, " '"+str(id)+"' this story does not exist !")
    else:
        msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'user-story-view')



def update_table_structure(request,columnnames):
    if  ArShowcolumns.objects.filter(Table_name='AR_USER_STORY').filter(user_id=request.session['user_id']).exists():
        save_column = ArShowcolumns.objects.filter(Table_name='AR_USER_STORY').filter(user_id=request.session['user_id']).update(columnName=columnnames)
    else:
        save_column = ArShowcolumns(Table_name='AR_USER_STORY',user_id=request.session['user_id'],columnName=columnnames,ORG_id=request.session['org_id'])
        save_column.save()
    msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Rearrange")
    msg_data = msg.notification_desc
    messages.info(request, msg_data)
    return redirect(settings.BASE_URL + 'user-story-view')





@csrf_exempt
def get_criteria_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        if check_map != "" :
            reading_ease = flesch_reading_ease(check_map)
            return JsonResponse({'data': int(reading_ease)})
        else:
            return JsonResponse({'data': 0})
    return JsonResponse({'data': 0})

@csrf_exempt
def get_conversations_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        if check_map != "" :
            reading_ease = flesch_reading_ease_conversations(check_map)
            return JsonResponse({'data': int(reading_ease)})
        else:
            return JsonResponse({'data': 0})
    return JsonResponse({'data': 0})




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
        get_file_name = ""
        if type == "xlsx":
            get_file_name += ",,"+file_path
        for items in table_list:
            if type == "CSV":
                get_result = create_csv(request,org_ins,org_name[0], items)
                get_file_name += ",,"+str(get_result)
            else:
                worksheet = workbook.add_worksheet(items)
                if items == "AR_USER_STORY":
                    get_AR_USER_STORY_data(org_ins,worksheet)

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
        table_list = ["AR_USER_STORY"]
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

                if items == "AR_USER_STORY":
                    get_AR_USER_STORY_data(org_ins, worksheet)

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

    if items == "AR_USER_STORY":
        get_AR_USER_STORY_data_CSV2(request,org_ins, file_name)

    return file_name




def get_help(request):
    if request.method == "POST":
        id = request.POST['id']
        # page_name = get_object_or_404(Help_Text, page_name=id)
        page_name = Help_Text.objects.filter(page_name=id)
        help_value = Help_Text_Serializer(page_name, many=True)
        #
        return JsonResponse({"data": help_value.data})
        # return JsonResponse({"data": id})
    else:
        return JsonResponse({"data": "ok"})

