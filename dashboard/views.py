from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User,auth
from django.http import JsonResponse
from agileproject import settings
from datetime import date
from account.models import AR_organization,csvFilesUplodaded,Notification,Ar_user
from manage_product.models import AR_product,AR_team
from manage_backlogs.models import AR_BACKLOG,AR_BACKLOG_STATUS
from user_story_view.models import AR_USER_STORY,AR_US_STATUS,AR_US_TYPE

from job_story_view.models import AR_JOB_STORY
from test_story_view.models import AR_TEST_STORY
from ar_scenario.models import AR_SCENARIO

from business_value.models import AR_BUSINESS_VALUE

from user_story_points.models import ArUserStoryPoints
from manage_iterations.models import ArIterations
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from django.utils.encoding import force_bytes,force_text
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
import csv, io
import dateutil.parser
from django.db.models import Q
from subscription.models import MembershipRequest,Subscription,MembershipHistory,Payment
from django.template.defaulttags import register


# Create your views here.






def get_user_name(request):
    ar_user_set = get_object_or_404(Ar_user, pk=request.session['user_id'])
    return HttpResponse(ar_user_set.user_name)

def read_csv_file_for_iteration(request,file_id):
    file_id = file_id
    if csvFilesUplodaded.objects.filter(id=file_id).exists():
        get_files = get_object_or_404(csvFilesUplodaded, pk=file_id)
        if get_files.ORG_ID.id != request.session['org_id']:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Not_related")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
            # print(message)
        else:
            msg_data_2 = ""
            csv_file = get_files.attachments
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            get_data = csv.reader(io_string, delimiter=',', quotechar="|")
            get_data2 = ""
            allready_exists = []
            file_name = get_data
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            updateded_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            ar_user_set = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            # print("sjdhbcfdhv")
            try:
                for item in file_name:
                    if item[0] != "":
                        # print("0:"+item[0]+"----1:"+item[1]+"----2:"+item[2]+"----3:"+item[3]+"----4:"+item[4]+"----5:"+item[5]+"----6:"+item[6]+"----7:"+item[7]+"----8:"+item[8]+"----9:"+item[9]+"----10:"+item[10]+"----11:"+item[11]+"----12:"+item[12]+"----13:"+item[13]+"----14:"+item[14])
                        if ArIterations.objects.filter(IterationName=item[0]).filter(ORG_ID=org_ins).exists():
                            allready_exists.append(item[0])
                        else:
                            # =========owner Start
                            owner = get_object_or_404(Ar_user, pk=request.session['user_id'])
                            if item[1] != "":
                                try:
                                    owner_id = int(item[1])
                                    if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, pk=owner_id)
                                except ValueError:
                                    if Ar_user.objects.filter(user_name=item[1]).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, user_name=item[1], org_id=org_ins)
                            # =========owner End

                            # =========product Start
                            product_set_dsp = None
                            product_set = None
                            if item[5] != "":
                                try:
                                    product_id = int(item[5])

                                    # print(AR_product.objects.filter(id=product_id).filter(ORG_ID=org_ins).exists())
                                    if AR_product.objects.filter(id=product_id).filter(ORG_ID=org_ins).exists():
                                        product_set_dsp = get_object_or_404(AR_product, pk=product_id,ORG_ID=org_ins)
                                except ValueError:
                                    if AR_product.objects.filter(Product_name=item[5]).filter(ORG_ID=org_ins).exists():
                                        product_set_dsp = get_object_or_404(AR_product, Product_name=item[5], ORG_ID=org_ins)
                            # =========product End

                            # =========backlog Start
                            backlog_set = None
                            if product_set_dsp != None:
                                if item[6] != "":
                                    try:
                                        backlog_id = int(item[6])
                                        if AR_BACKLOG.objects.filter(id=backlog_id).filter(ORG_ID=org_ins).filter(product_parent=product_set_dsp).exists():
                                            backlog_set = get_object_or_404(AR_BACKLOG, pk=backlog_id)
                                    except ValueError:
                                        if AR_BACKLOG.objects.filter(title=item[6]).filter(ORG_ID=org_ins).filter(product_parent=product_set_dsp).exists():
                                            backlog_set = get_object_or_404(AR_BACKLOG, title=item[6],ORG_ID=org_ins,product_parent=product_set_dsp)
                            # =========backlog End


                            userstory_set = None
                            if backlog_set != None:
                                userstory_set = None
                            # =========UserStory End
                            # print(item[5])
                            # print(item[6])

                            # =========Team Start

                            set_team = None

                            if item[8] != "":
                                try:
                                    team_id = int(item[8])
                                    if AR_team.objects.filter(id=team_id).filter(ORG_id=org_ins).exists():
                                        set_team = get_object_or_404(AR_team, pk=team_id)
                                except ValueError:
                                    if AR_team.objects.filter(Team_name=item[8]).filter(ORG_id=org_ins).exists():
                                        set_team = get_object_or_404(AR_team, title=item[8], ORG_id=org_ins)
                            print("team")
                            print(set_team)
                            # =========Team END

                            StartDate = item[2]
                            EndDate = item[3]
                            if StartDate == "":
                                StartDate = date.today()
                            else:
                                # StartDate = dateutil.parser.parse(StartDate)
                                StartDate =  datetime.strptime(StartDate, "%m/%d/%Y")
                            if EndDate == '':
                                EndDate = date.today()
                            else:
                                # EndDate = dateutil.parser.parse(EndDate)
                                EndDate = datetime.strptime(EndDate, "%m/%d/%Y")
                            print("-------")
                            print(StartDate)
                            print(EndDate)
                            print("---------")
                            IterationScore = 0
                            IterationSize = 0

                            # ============== create_by update_by start
                            if item[11] != "":
                                if Ar_user.objects.filter(id=item[11]).filter(org_id=org_ins).exists():
                                    created_by_ins = get_object_or_404(Ar_user, pk=item[11])
                                if Ar_user.objects.filter(user_name=item[11]).filter(org_id=org_ins).exists():
                                    created_by_ins = get_object_or_404(Ar_user, user_name=item[11], org_id=org_ins)
                            if item[13] != "":
                                if Ar_user.objects.filter(id=item[13]).filter(org_id=org_ins).exists():
                                    updateded_by_ins = get_object_or_404(Ar_user, pk=item[13])
                                if Ar_user.objects.filter(user_name=item[13]).filter(org_id=org_ins).exists():
                                    updateded_by_ins = get_object_or_404(Ar_user, user_name=item[13], org_id=org_ins)

                            # =========UserStory Start
                            user_stury_set = None

                            user_stury_set = None
                            if backlog_set != None:
                                if item[7] != "":
                                    story_id_in_list = item[7].split("|")
                                    try:
                                        story_id = story_id_in_list[0]
                                        if AR_USER_STORY.objects.filter(id__in=story_id_in_list).filter(
                                                backlog_parent=backlog_set).filter(ORG_id=org_ins).exists():
                                            user_stury_set = AR_USER_STORY.objects.filter(
                                                id__in=story_id_in_list).filter(backlog_parent=backlog_set).filter(
                                                ORG_id=org_ins)
                                    except:
                                        if AR_USER_STORY.objects.filter(title__in=story_id_in_list).filter(
                                                backlog_parent=backlog_set).filter(ORG_id=org_ins).exists():
                                            user_stury_set = AR_USER_STORY.objects.filter(
                                                title__in=story_id_in_list).filter(backlog_parent=backlog_set).filter(
                                                ORG_id=org_ins)


                                    # =========UserStory END
                            add_iteration = ArIterations(IterationName=item[0],owner=owner,StartDate=StartDate,EndDate=EndDate,Description=item[4],Product=product_set_dsp,Backlog=backlog_set,Team=set_team,IterationScore=IterationScore,IterationSize=IterationSize,ORG_ID=org_ins,create_by=created_by_ins,update_by=updateded_by_ins)
                            add_iteration.save()
                            create_itera_id = "AR_ITER_" + str(add_iteration.id)
                            ArIterations.objects.filter(id=add_iteration.id).update(IterationId=create_itera_id)
                            if user_stury_set != None:
                                add_iteration.UserStory.set(user_stury_set)

                            msg = get_object_or_404(Notification, page_name="Manage Iteration", notification_key="Add")
                            msg_data_2 = msg.notification_desc
                allready_exists = ','.join([str(elem) for elem in allready_exists])
                if allready_exists != "":
                    msg = get_object_or_404(Notification, page_name="Manage Iteration", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, "'"+allready_exists + "' , " + msg_data)
            except:
                msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
                msg_data = msg.notification_desc
                messages.error(request, msg_data)

                # messages.error(request, "Something was wrong maybe yours.CSV file is not proper please check your CSV file formate.")
    messages.info(request, msg_data_2)
    return HttpResponse("True")


def read_csv_file_for_user_story(request,file_id):
    file_id = file_id
    print(file_id)
    if csvFilesUplodaded.objects.filter(id=file_id).exists():
        get_files = get_object_or_404(csvFilesUplodaded, pk=file_id)
        if get_files.ORG_ID.id != request.session['org_id']:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Not_related")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        else:
            msg_data_2 = ""
            csv_file = get_files.attachments
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            get_data = csv.reader(io_string, delimiter=',', quotechar="|")
            get_data2 = ""
            file_name = get_data
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            updateded_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            ar_user_set = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            allready_exists = []
            try:
                for item in file_name:

                    get_status = get_package_limit(request.session['org_id'],"User_Stories")
                    if get_status:
                        if AR_USER_STORY.objects.filter(title=item[0]).filter(ORG_id=org_ins).exists():
                            allready_exists.append(item[0])
                        else:
                            num_in_str= str(item[3])
                            # print(item[9])
                            # print(type(num_in_str))
                            # print(type(int(num_in_str)))
                            print("0:"+item[0]+"--1:"+item[1]+"--2:"+item[2]+"--3:"+item[3]+"--4:"+item[4]+"--5:"+item[5]+"--6:"+item[6]+"--7:"+item[7]+"--8:"+item[8]+"--9:"+item[9]+"--10:"+item[10]+"--11:"+item[11]+"--12:"+item[12]+"--13:"+item[13]+"--14:"+item[14]+"--15:"+item[15]+"--16:"+item[16]+"--17:"+item[17]+"--18:"+item[18])
                            if item[3] == "":
                                item[3] = 0
                            if item[6] == "":
                                item[6] = 0
                            if item[9] == "":
                                item[9] = 0

                            # ============== create_by update_by start
                            if item[15] != "":
                                try:
                                    created_by_ins_id = int(item[15])
                                    if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                        created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[15]).filter(org_id=org_ins).exists():
                                        created_by_ins = get_object_or_404(Ar_user, user_name=item[15], org_id=org_ins)
                            if item[18] != "":
                                try:
                                    updateded_by_ins_id = int(item[18])
                                    if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                        updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[18]).filter(org_id=org_ins).exists():
                                        updateded_by_ins = get_object_or_404(Ar_user, user_name=item[18], org_id=org_ins)

                            #============== create_by update_by end
                            # ============BACKLOG PERENT START
                            if item[5] == "":
                                backog_perent_set = None
                            else:
                                backog_perent_set = None
                                try:
                                    bl_id = int(item[5])
                                    if AR_BACKLOG.objects.filter(id=bl_id).filter(ORG_ID=org_ins).exists():
                                        backog_perent_set = get_object_or_404(AR_BACKLOG, pk=bl_id)
                                except:
                                    if AR_BACKLOG.objects.filter(title=item[5]).filter(ORG_ID=org_ins).exists():
                                        backog_perent_set = get_object_or_404(AR_BACKLOG, title=item[5], ORG_ID=org_ins)
                            # ============BACKLOG PERENT END
                            if item[7] == "1":
                                autoscoring_on =True
                            else:
                                autoscoring_on = False

                            if item[8] == "1":
                                archive_indicator = True
                            else:
                                archive_indicator = False


                            if item[10] == "":
                                story_points_set = None
                            else:
                                story_points_set = None
                                try:
                                    story_points_set_id = int(item[10])
                                    if ArUserStoryPoints.objects.filter(id=story_points_set_id).filter(ORG_ID=org_ins).exists():
                                        story_points_set = get_object_or_404(ArUserStoryPoints, pk=story_points_set_id)
                                except:
                                    if ArUserStoryPoints.objects.filter(Point_Key=item[10]).filter(ORG_ID=org_ins).exists():
                                        story_points_set = get_object_or_404(ArUserStoryPoints, Point_Key=item[10], ORG_ID=org_ins)

                            # ============user_story_status START

                            if item[11] == "":
                                user_story_status_set = None
                            else:
                                user_story_status_set = None
                                try:
                                    item_id = int(item[11])
                                    if AR_US_STATUS.objects.filter(id=item_id).exists():
                                        user_story_status_set = get_object_or_404(AR_US_STATUS, pk=item_id)
                                except:
                                    if AR_US_STATUS.objects.filter(status_key=item[11]).exists():
                                        user_story_status_set = get_object_or_404(AR_US_STATUS, status_key=item[11])
                            # ============user_story_status END


                            # ============UST_ID START

                            if item[12] == "":
                                UST_ID_set = None
                            else:
                                UST_ID_set = None
                                try:
                                    UST_ID_id =  int(item[12])
                                    if AR_US_TYPE.objects.filter(id=UST_ID_id).exists():
                                        UST_ID_set = get_object_or_404(AR_US_TYPE, pk=UST_ID_id)
                                except:
                                    if AR_US_TYPE.objects.filter(type_key=item[12]).exists():
                                        UST_ID_set = get_object_or_404(AR_US_TYPE, type_key=item[12])
                            # ============UST_ID END
                            # =========ar_user Start
                            if item[13] != "":
                                try:
                                    ar_user_id = int(item[13])
                                    if Ar_user.objects.filter(id=ar_user_id).filter(org_id=org_ins).exists():
                                        ar_user_set = get_object_or_404(Ar_user, pk=ar_user_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[13]).filter(org_id=org_ins).exists():
                                        ar_user_set = get_object_or_404(Ar_user, user_name=item[13], org_id=org_ins)
                            # =========ar_user END

                            # =========owner Start
                            owner = get_object_or_404(Ar_user, pk=request.session['user_id'])
                            if item[14] != "":
                                try:
                                    owner_id = int(item[14])
                                    if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, pk=owner_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[14]).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, user_name=item[14], org_id=org_ins)
                            # =========owner End

                            # set string to int start
                            ac_readability_score = 0
                            if item[3] != "":
                                try:
                                    ac_readability_score = int(item[3])
                                except:
                                    ac_readability_score = 0

                            convo_readability_score = 0
                            if item[6] != "":
                                try:
                                    convo_readability_score = int(item[6])
                                except:
                                    convo_readability_score = 0

                            readiness_quality_score = 0
                            if item[9] != "":
                                try:
                                    readiness_quality_score = int(item[9])
                                except:
                                    readiness_quality_score = 0
                            # set string to int start

                            userStory = AR_USER_STORY(title=item[0],story_tri_part_text=item[1],acceptance_criteria=item[2],ac_readability_score=ac_readability_score,conversation=item[4],backlog_parent=backog_perent_set,convo_readability_score=convo_readability_score,autoscoring_on=autoscoring_on,archive_indicator=archive_indicator,readiness_quality_score=readiness_quality_score,story_points=story_points_set,user_story_status=user_story_status_set,ORG_id=org_ins,UST_ID=UST_ID_set,ar_user=ar_user_set,owner=owner,created_by=created_by_ins,updated_by=updateded_by_ins)
                            userStory.save()
                            msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Add")
                            msg_data_2 = msg.notification_desc
                    else:
                        msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                        msg_data = msg.notification_desc
                        messages.error(request, msg_data)  
                allready_exists = ','.join([str(elem) for elem in allready_exists])
                if allready_exists != "":
                    msg = get_object_or_404(Notification, page_name="User Story View", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, "'"+allready_exists + "' , " + msg_data)
            except:
                msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
                msg_data = msg.notification_desc
                messages.error(request, msg_data)

                # messages.error(request,"Something was wrong maybe yours.CSV file is not proper please check your CSV file formate.")
    messages.info(request, msg_data_2)
    return HttpResponse(True)
# ----------------------------------------------------------------
def read_csv_file_for_job_story(request,file_id):
    file_id = file_id
    print(file_id)
    if csvFilesUplodaded.objects.filter(id=file_id).exists():
        get_files = get_object_or_404(csvFilesUplodaded, pk=file_id)
        if get_files.ORG_ID.id != request.session['org_id']:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Not_related")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        else:
            msg_data_2 = ""
            csv_file = get_files.attachments
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            get_data = csv.reader(io_string, delimiter=',', quotechar="|")
            get_data2 = ""
            file_name = get_data
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            updateded_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            ar_user_set = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            allready_exists = []
            try:
                for item in file_name:

                    get_status = get_package_limit(request.session['org_id'],"Job_Stories")
                    if get_status:
                        if AR_JOB_STORY.objects.filter(title=item[0]).filter(ORG_id=org_ins).exists():
                            allready_exists.append(item[0])
                        else:
                            num_in_str= str(item[3])
                            # print(item[9])
                            # print(type(num_in_str))
                            # print(type(int(num_in_str)))
                            print("0:"+item[0]+"--1:"+item[1]+"--2:"+item[2]+"--3:"+item[3]+"--4:"+item[4]+"--5:"+item[5]+"--6:"+item[6]+"--7:"+item[7]+"--8:"+item[8]+"--9:"+item[9]+"--10:"+item[10]+"--11:"+item[11]+"--12:"+item[12]+"--13:"+item[13]+"--14:"+item[14]+"--15:"+item[15]+"--16:"+item[16]+"--17:"+item[17]+"--18:"+item[18])
                            if item[3] == "":
                                item[3] = 0
                            if item[6] == "":
                                item[6] = 0
                            if item[9] == "":
                                item[9] = 0

                            # ============== create_by update_by start
                            if item[15] != "":
                                try:
                                    created_by_ins_id = int(item[15])
                                    if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                        created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[15]).filter(org_id=org_ins).exists():
                                        created_by_ins = get_object_or_404(Ar_user, user_name=item[15], org_id=org_ins)
                            if item[18] != "":
                                try:
                                    updateded_by_ins_id = int(item[18])
                                    if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                        updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[18]).filter(org_id=org_ins).exists():
                                        updateded_by_ins = get_object_or_404(Ar_user, user_name=item[18], org_id=org_ins)

                            #============== create_by update_by end
                            # ============BACKLOG PERENT START
                            if item[5] == "":
                                backog_perent_set = None
                            else:
                                backog_perent_set = None
                                try:
                                    bl_id = int(item[5])
                                    if AR_BACKLOG.objects.filter(id=bl_id).filter(ORG_ID=org_ins).exists():
                                        backog_perent_set = get_object_or_404(AR_BACKLOG, pk=bl_id)
                                except:
                                    if AR_BACKLOG.objects.filter(title=item[5]).filter(ORG_ID=org_ins).exists():
                                        backog_perent_set = get_object_or_404(AR_BACKLOG, title=item[5], ORG_ID=org_ins)
                            # ============BACKLOG PERENT END
                            # ============BUSINESS VALUE START
                            if item[20] == "":
                                business_value_set = None
                            else:
                                business_value_set = None
                                try:
                                    bv_id = int(item[20])
                                    if AR_BUSINESS_VALUE.objects.filter(id=bv_id).filter(ORG_ID=org_ins).exists():
                                        business_value_set = get_object_or_404(AR_BUSINESS_VALUE, pk=bv_id)
                                except:
                                    if AR_BUSINESS_VALUE.objects.filter(bus_value_txt_code=item[20]).filter(ORG_ID=org_ins).exists():
                                        business_value_set = get_object_or_404(AR_BUSINESS_VALUE, bus_value_txt_code=item[20], ORG_ID=org_ins)
                            # ============BACKLOG PERENT END
                            if item[7] == "1":
                                autoscoring_on =True
                            else:
                                autoscoring_on = False

                            if item[8] == "1":
                                archive_indicator = True
                            else:
                                archive_indicator = False


                            if item[10] == "":
                                story_points_set = None
                            else:
                                story_points_set = None
                                try:
                                    story_points_set_id = int(item[10])
                                    if ArUserStoryPoints.objects.filter(id=story_points_set_id).filter(ORG_ID=org_ins).exists():
                                        story_points_set = get_object_or_404(ArUserStoryPoints, pk=story_points_set_id)
                                except:
                                    if ArUserStoryPoints.objects.filter(Point_Key=item[10]).filter(ORG_ID=org_ins).exists():
                                        story_points_set = get_object_or_404(ArUserStoryPoints, Point_Key=item[10], ORG_ID=org_ins)

                            # ============user_story_status START

                            if item[11] == "":
                                job_story_status_set = None
                            else:
                                job_story_status_set = None
                                try:
                                    item_id = int(item[11])
                                    if AR_US_STATUS.objects.filter(id=item_id).exists():
                                        job_story_status_set = get_object_or_404(AR_US_STATUS, pk=item_id)
                                except:
                                    if AR_US_STATUS.objects.filter(status_key=item[11]).exists():
                                        job_story_status_set = get_object_or_404(AR_US_STATUS, status_key=item[11])
                            # ============user_story_status END


                            # ============UST_ID START

                            if item[12] == "":
                                UST_ID_set = None
                            else:
                                UST_ID_set = None
                                try:
                                    UST_ID_id =  int(item[12])
                                    if AR_US_TYPE.objects.filter(id=UST_ID_id).exists():
                                        UST_ID_set = get_object_or_404(AR_US_TYPE, pk=UST_ID_id)
                                except:
                                    if AR_US_TYPE.objects.filter(type_key=item[12]).exists():
                                        UST_ID_set = get_object_or_404(AR_US_TYPE, type_key=item[12])
                            # ============UST_ID END
                            # =========ar_user Start
                            if item[13] != "":
                                try:
                                    ar_user_id = int(item[13])
                                    if Ar_user.objects.filter(id=ar_user_id).filter(org_id=org_ins).exists():
                                        ar_user_set = get_object_or_404(Ar_user, pk=ar_user_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[13]).filter(org_id=org_ins).exists():
                                        ar_user_set = get_object_or_404(Ar_user, user_name=item[13], org_id=org_ins)
                            # =========ar_user END

                            # =========owner Start
                            owner = get_object_or_404(Ar_user, pk=request.session['user_id'])
                            if item[14] != "":
                                try:
                                    owner_id = int(item[14])
                                    if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, pk=owner_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[14]).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, user_name=item[14], org_id=org_ins)
                            # =========owner End

                            # set string to int start
                            ac_readability_score = 0
                            if item[3] != "":
                                try:
                                    ac_readability_score = int(item[3])
                                except:
                                    ac_readability_score = 0

                            convo_readability_score = 0
                            if item[6] != "":
                                try:
                                    convo_readability_score = int(item[6])
                                except:
                                    convo_readability_score = 0

                            readiness_quality_score = 0
                            if item[9] != "":
                                try:
                                    readiness_quality_score = int(item[9])
                                except:
                                    readiness_quality_score = 0
                            # set string to int start

                            userStory = AR_JOB_STORY(title=item[0],story_tri_part_text=item[1],acceptance_criteria=item[2],ac_readability_score=ac_readability_score,conversation=item[4],backlog_parent=backog_perent_set,BV_ID=business_value_set,convo_readability_score=convo_readability_score,autoscoring_on=autoscoring_on,archive_indicator=archive_indicator,readiness_quality_score=readiness_quality_score,story_points=story_points_set,job_story_status=job_story_status_set,ORG_id=org_ins,UST_ID=UST_ID_set,ar_user=ar_user_set,owner=owner,created_by=created_by_ins,updated_by=updateded_by_ins)
                            userStory.save()
                            msg = get_object_or_404(Notification, page_name="Job Story View", notification_key="Add")
                            msg_data_2 = msg.notification_desc
                    else:
                        msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                        msg_data = msg.notification_desc
                        messages.error(request, msg_data)
                allready_exists = ','.join([str(elem) for elem in allready_exists])
                if allready_exists != "":
                    msg = get_object_or_404(Notification, page_name="Job Story View", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, "'"+allready_exists + "' , " + msg_data)
            except:
                msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
                msg_data = msg.notification_desc
                messages.error(request, msg_data)

                # messages.error(request,"Something was wrong maybe yours.CSV file is not proper please check your CSV file formate.")
    messages.info(request, msg_data_2)
    return HttpResponse(True)
# ---------------------------------------------------------------------------------------------------# ----------------------------------------------------------------
def read_csv_file_for_test_story(request,file_id):
    file_id = file_id
    print(file_id)
    if csvFilesUplodaded.objects.filter(id=file_id).exists():
        get_files = get_object_or_404(csvFilesUplodaded, pk=file_id)
        if get_files.ORG_ID.id != request.session['org_id']:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Not_related")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        else:
            msg_data_2 = ""
            csv_file = get_files.attachments
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            get_data = csv.reader(io_string, delimiter=',', quotechar="|")
            get_data2 = ""
            file_name = get_data
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            updateded_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            ar_user_set = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            allready_exists = []
            try:
                for item in file_name:

                    get_status = get_package_limit(request.session['org_id'],"Test_Stories")
                    if get_status:
                        if AR_TEST_STORY.objects.filter(title=item[0]).filter(ORG_id=org_ins).exists():
                            allready_exists.append(item[0])
                        else:
                            num_in_str= str(item[3])
                            # print(item[9])
                            # print(type(num_in_str))
                            # print(type(int(num_in_str)))
                            print("0:"+item[0]+"--1:"+item[1]+"--2:"+item[2]+"--3:"+item[3]+"--4:"+item[4]+"--5:"+item[5]+"--6:"+item[6]+"--7:"+item[7]+"--8:"+item[8]+"--9:"+item[9]+"--10:"+item[10]+"--11:"+item[11]+"--12:"+item[12]+"--13:"+item[13]+"--14:"+item[14]+"--15:"+item[15]+"--16:"+item[16]+"--17:"+item[17]+"--18:"+item[18])
                            if item[3] == "":
                                item[3] = 0
                            if item[7] == "":
                                item[7] = 0
                            if item[10] == "":
                                item[10] = 0

                            # ============== create_by update_by start
                            if item[16] != "":
                                try:
                                    created_by_ins_id = int(item[16])
                                    if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                        created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[16]).filter(org_id=org_ins).exists():
                                        created_by_ins = get_object_or_404(Ar_user, user_name=item[16], org_id=org_ins)
                            if item[19] != "":
                                try:
                                    updateded_by_ins_id = int(item[19])
                                    if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                        updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[19]).filter(org_id=org_ins).exists():
                                        updateded_by_ins = get_object_or_404(Ar_user, user_name=item[19], org_id=org_ins)

                            #============== create_by update_by end
                            # ============PRODUCT PERENT START
                            if item[5] == "":
                                product_perent_set = None
                            else:
                                product_perent_set = None
                                try:
                                    bl_id = int(item[5])
                                    if AR_product.objects.filter(id=bl_id).filter(ORG_ID=org_ins).exists():
                                        product_perent_set = get_object_or_404(AR_product, pk=bl_id)
                                except:
                                    if AR_product.objects.filter(Product_name=item[5]).filter(ORG_ID=org_ins).exists():
                                        product_perent_set = get_object_or_404(AR_product, Product_name=item[5], ORG_ID=org_ins)
                            # ============BACKLOG PERENT END
                            # ============scenario PERENT START
                            if item[6] == "":
                                scenario_perent_set = None
                            else:
                                scenario_perent_set = None
                                try:
                                    bl_id = int(item[6])
                                    if AR_SCENARIO.objects.filter(id=bl_id).filter(ORG_ID=org_ins).exists():
                                        scenario_perent_set = get_object_or_404(AR_product, pk=bl_id)
                                except:
                                    if AR_SCENARIO.objects.filter(scenario_name=item[6]).filter(ORG_ID=org_ins).exists():
                                        scenario_perent_set = get_object_or_404(AR_product, scenario_name=item[6], ORG_ID=org_ins)
                            # ============BACKLOG PERENT END
                            # ============BUSINESS VALUE START
                            if item[21] == "":
                                business_value_set = None
                            else:
                                business_value_set = None
                                try:
                                    bv_id = int(item[21])
                                    if AR_BUSINESS_VALUE.objects.filter(id=bv_id).filter(ORG_ID=org_ins).exists():
                                        business_value_set = get_object_or_404(AR_BUSINESS_VALUE, pk=bv_id)
                                except:
                                    if AR_BUSINESS_VALUE.objects.filter(bus_value_txt_code=item[21]).filter(ORG_ID=org_ins).exists():
                                        business_value_set = get_object_or_404(AR_BUSINESS_VALUE, bus_value_txt_code=item[21], ORG_ID=org_ins)
                            # ============BACKLOG PERENT END
                            if item[8] == "1":
                                autoscoring_on =True
                            else:
                                autoscoring_on = False

                            if item[9] == "1":
                                archive_indicator = True
                            else:
                                archive_indicator = False


                            if item[11] == "":
                                story_points_set = None
                            else:
                                story_points_set = None
                                try:
                                    story_points_set_id = int(item[11])
                                    if ArUserStoryPoints.objects.filter(id=story_points_set_id).filter(ORG_ID=org_ins).exists():
                                        story_points_set = get_object_or_404(ArUserStoryPoints, pk=story_points_set_id)
                                except:
                                    if ArUserStoryPoints.objects.filter(Point_Key=item[11]).filter(ORG_ID=org_ins).exists():
                                        story_points_set = get_object_or_404(ArUserStoryPoints, Point_Key=item[11], ORG_ID=org_ins)

                            # ============user_story_status START

                            if item[12] == "":
                                test_story_status_set = None
                            else:
                                test_story_status_set = None
                                try:
                                    item_id = int(item[12])
                                    if AR_US_STATUS.objects.filter(id=item_id).exists():
                                        test_story_status_set = get_object_or_404(AR_US_STATUS, pk=item_id)
                                except:
                                    if AR_US_STATUS.objects.filter(status_key=item[12]).exists():
                                        test_story_status_set = get_object_or_404(AR_US_STATUS, status_key=item[12])
                            # ============user_story_status END


                            # ============UST_ID START

                            if item[13] == "":
                                UST_ID_set = None
                            else:
                                UST_ID_set = None
                                try:
                                    UST_ID_id =  int(item[13])
                                    if AR_US_TYPE.objects.filter(id=UST_ID_id).exists():
                                        UST_ID_set = get_object_or_404(AR_US_TYPE, pk=UST_ID_id)
                                except:
                                    if AR_US_TYPE.objects.filter(type_key=item[13]).exists():
                                        UST_ID_set = get_object_or_404(AR_US_TYPE, type_key=item[13])
                            # ============UST_ID END
                            # =========ar_user Start
                            if item[14] != "":
                                try:
                                    ar_user_id = int(item[14])
                                    if Ar_user.objects.filter(id=ar_user_id).filter(org_id=org_ins).exists():
                                        ar_user_set = get_object_or_404(Ar_user, pk=ar_user_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[14]).filter(org_id=org_ins).exists():
                                        ar_user_set = get_object_or_404(Ar_user, user_name=item[14], org_id=org_ins)
                            # =========ar_user END

                            # =========owner Start
                            owner = get_object_or_404(Ar_user, pk=request.session['user_id'])
                            if item[15] != "":
                                try:
                                    owner_id = int(item[15])
                                    if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, pk=owner_id)
                                except:
                                    if Ar_user.objects.filter(user_name=item[15]).filter(org_id=org_ins).exists():
                                        owner = get_object_or_404(Ar_user, user_name=item[15], org_id=org_ins)
                            # =========owner End

                            # set string to int start
                            ac_readability_score = 0
                            if item[3] != "":
                                try:
                                    ac_readability_score = int(item[3])
                                except:
                                    ac_readability_score = 0

                            convo_readability_score = 0
                            if item[7] != "":
                                try:
                                    convo_readability_score = int(item[7])
                                except:
                                    convo_readability_score = 0

                            readiness_quality_score = 0
                            if item[10] != "":
                                try:
                                    readiness_quality_score = int(item[10])
                                except:
                                    readiness_quality_score = 0
                            # set string to int start

                            userStory = AR_TEST_STORY(title=item[0],story_tri_part_text=item[1],acceptance_criteria=item[2],ac_readability_score=ac_readability_score,conversation=item[4],product_parent=product_perent_set,scenario_parent=scenario_perent_set,BV_ID=business_value_set,convo_readability_score=convo_readability_score,autoscoring_on=autoscoring_on,archive_indicator=archive_indicator,readiness_quality_score=readiness_quality_score,story_points=story_points_set,test_story_status=test_story_status_set,ORG_id=org_ins,UST_ID=UST_ID_set,ar_user=ar_user_set,owner=owner,created_by=created_by_ins,updated_by=updateded_by_ins)
                            userStory.save()
                            msg = get_object_or_404(Notification, page_name="Test Story View", notification_key="Add")
                            msg_data_2 = msg.notification_desc
                    else:
                        msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                        msg_data = msg.notification_desc
                        messages.error(request, msg_data)
                allready_exists = ','.join([str(elem) for elem in allready_exists])
                if allready_exists != "":
                    msg = get_object_or_404(Notification, page_name="Test Story View", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, "'"+allready_exists + "' , " + msg_data)
            except:
                msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
                msg_data = msg.notification_desc
                messages.error(request, msg_data)

                # messages.error(request,"Something was wrong maybe yours.CSV file is not proper please check your CSV file formate.")
    messages.info(request, msg_data_2)
    return HttpResponse(True)

# ---------------------------------------------------------------------------------------------------
def read_csv_files(request,file_id):
    file_id = file_id

    message = "work fine"
    if csvFilesUplodaded.objects.filter(id=file_id).exists():
        get_files = get_object_or_404(csvFilesUplodaded,pk=file_id)
        if get_files.ORG_ID.id != request.session['org_id']:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Not_related")
            message = msg.notification_desc
            # messages.error(request, msg_data)

            # message = "This CSV file is not related to your organization."
        else:
            msg_data_2 = ""
            csv_file = get_files.attachments
            data_set = csv_file.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            get_data = csv.reader(io_string, delimiter=',', quotechar="|")
            get_data2 = ""
            file_name = get_data
            get_names = ""
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            updateded_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            already_exists = []
            try:
                for item in file_name:
                    get_status = get_package_limit(request.session['org_id'],"Product")
                    if get_status:
                        # ======================== CODE FOR PRODUCT START ============================
                        if get_files.csvUseFor == 'AR_product':
                            # item[0]  product name
                            # item[1]  product description
                            # item[2]  Business_unit
                            # item[3]  US_quality_threshold
                            # item[4]  Createed_by
                            # item[5]  created_date
                            # item[6]  Updateded_by
                            # item[7]  Updated_date

                            if item[0] != '':
                                if AR_product.objects.filter(Product_name=item[0]).filter(ORG_ID=org_ins).exists():
                                    already_exists.append(item[0])
                                    msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Exists")
                                    msg_data = msg.notification_desc
                                else:
                                    try:
                                        created_by_ins_id = int(item[4])
                                        if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                            created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                                    except:
                                        if Ar_user.objects.filter(user_name=item[4]).filter(org_id=org_ins).exists():
                                            created_by_ins = get_object_or_404(Ar_user, user_name=item[4],org_id=org_ins)
                                    try:
                                        updateded_by_ins_id = int(item[6])
                                        if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                            updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                                    except:
                                        if Ar_user.objects.filter(user_name=item[6]).filter(org_id=org_ins).exists():
                                            updateded_by_ins = get_object_or_404(Ar_user, user_name=item[6],org_id=org_ins)

                                    US_quality_threshold = 0
                                    # print(item[3])
                                    # print(type(item[3]))
                                    if item[3] != "":
                                        try:
                                            US_quality_threshold = int(item[3])
                                        except:
                                            US_quality_threshold = 0
                                    data = AR_product(Product_name=item[0], Product_description=item[1], Business_unit=item[2],US_quality_threshold=US_quality_threshold,ORG_ID=org_ins,create_by=created_by_ins, update_by=updateded_by_ins)
                                    data.save()
                                    msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Add")
                                    msg_data_2 = msg.notification_desc
                        # ======================== CODE FOR PRODUCT END ============================

                        # ======================== CODE FOR BACKLOG START ============================
                        if get_files.csvUseFor == 'AR_BACKLOG':
                            # item[0]  backlog title
                            # item[1]  owner
                            # item[2]  Team list
                            # item[3]  product_paren
                            # item[4]  BL_STATUS
                            # item[5]  created_by
                            # item[6]  created_dt
                            # item[7]  Updated_by
                            # item[8]  Updated_date
                            # product_paren = ""
                            if item[0] != '':
                                if AR_BACKLOG.objects.filter(title=item[0]).filter(ORG_ID=org_ins).exists():
                                    already_exists.append(item[0])
                                    msg = get_object_or_404(Notification, page_name="Manage Backlog", notification_key="Exists")
                                    msg_data = msg.notification_desc
                                    # messages.error(request, msg_data)
                                else:
                                    owner = get_object_or_404(Ar_user, pk=request.session['user_id'])
                                    if item[1] != "":
                                        try:
                                            owner_id = int(item[1])
                                            if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                                owner = get_object_or_404(Ar_user, pk=owner_id)
                                        except:
                                            if Ar_user.objects.filter(user_name=item[1]).filter(org_id=org_ins).exists():
                                                owner = get_object_or_404(Ar_user, user_name=item[1],org_id=org_ins)
                                    if item[3] == "":
                                        product_paren = None
                                    else:
                                        product_paren = None
                                        #==== GET PRODUCT INSTANCE
                                        try:
                                            product_paren_id = int(item[3])
                                            if AR_product.objects.filter(id=product_paren_id).filter(ORG_ID=org_ins).exists():
                                                product_paren = get_object_or_404(AR_product, pk=product_paren_id)
                                        except:
                                            if AR_product.objects.filter(Product_name=item[3]).filter(ORG_ID=org_ins).exists():
                                                product_paren = get_object_or_404(AR_product, Product_name=item[3],ORG_ID=org_ins)

                                    # ==== GET BACKLOG STATUS INSTANCE
                                    if item[4] == "":
                                        bl_status = None
                                    else:
                                        try:
                                            bl_status_id = int(item[4])
                                            if AR_BACKLOG_STATUS.objects.filter(id=bl_status_id).exists():
                                                bl_status = get_object_or_404(AR_BACKLOG_STATUS, pk=bl_status_id)
                                        except:
                                            if AR_BACKLOG_STATUS.objects.filter(bl_status_key=item[4]).exists():
                                                bl_status = get_object_or_404(AR_BACKLOG_STATUS, bl_status_key=item[4])

                                    try:
                                        created_by_ins_id = int(item[5])
                                        if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                            created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                                    except:
                                        if Ar_user.objects.filter(user_name=item[5]).filter(org_id=org_ins).exists():
                                            created_by_ins = get_object_or_404(Ar_user, user_name=item[5], org_id=org_ins)
                                    try:
                                        updateded_by_ins_id = int(item[7])
                                        if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                            updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                                    except:
                                        if Ar_user.objects.filter(user_name=item[7]).filter(org_id=org_ins).exists():
                                            updateded_by_ins = get_object_or_404(Ar_user, user_name=item[7], org_id=org_ins)
                                    backlog_score = 0
                                    Backlog_size = 0

                                    if item[2] == "":
                                        set_team = None
                                    else:
                                        team_in_list = item[2].split("|")
                                        try:
                                            team_one_in_int = int(team_in_list[0])
                                            set_team = AR_team.objects.filter(id__in=team_in_list).filter(ORG_id=org_ins)
                                        except:
                                            set_team = AR_team.objects.filter(Team_name__in=team_in_list).filter(ORG_id=org_ins)
                                    data_set = AR_BACKLOG(title=item[0],backlog_score=backlog_score,Backlog_size=Backlog_size,owner=owner,product_parent=product_paren,BL_STATUS=bl_status,ORG_ID=org_ins,created_by=created_by_ins,updated_by=updateded_by_ins)
                                    data_set.save()
                                    if set_team != None:
                                        data_set.team_list.set(set_team)
                                    msg = get_object_or_404(Notification, page_name="Manage Backlog", notification_key="Add")
                                    msg_data_2 = msg.notification_desc
                    else:
                        msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                        msg_data = msg.notification_desc
                        messages.error(request, msg_data)
                    # ======================== CODE FOR BACKLOG END ============================

                already_exists = ','.join([str(elem) for elem in already_exists])
                if already_exists != "":
                    messages.error(request, "'"+already_exists+"' "+msg_data)
                messages.info(request, msg_data_2)
            except:
                msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
                msg_data = msg.notification_desc
                messages.error(request, msg_data)

                # messages.error(request,"Something was wrong maybe yours.CSV file is not proper please check your CSV file formate.")
            return HttpResponse(get_names)
    else:
        message = "Data not found"
    return HttpResponse(message)

@csrf_exempt
def add_csv_files(request):
    set_statue = ""
    csv_id = ""
    if request.method == "POST":
        table_name = request.POST['modal_name']


        # msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
        # msg_data = table_name
        # messages.info(request, msg_data)


        return_url = request.POST['return_url']
        csv_file = request.FILES.get('attachments', False)
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)

            # messages.error(request, 'THIS IS NOT A CSV FILE')
            set_statue = urlsafe_base64_encode(force_bytes("error"))
        else:
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            data = csvFilesUplodaded(attachments=csv_file,csvUseFor=table_name,ORG_ID=org_ins,created_by=created_by_ins,updated_by=created_by_ins)
            try:
                data.save()
                return_url_set = return_url.split("-")
                return_url_set_string = ''


                # msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
                # msg_data = msg.notification_desc
                # messages.info(request, msg_data)


                # messages.info(request, "CSV Uploded successfully !")
                set_statue = urlsafe_base64_encode(force_bytes("done"))
                csv_id = urlsafe_base64_encode(force_bytes(data.id))
                if table_name == "AR_USER_STORY":
                    read_csv_file_for_user_story(request,data.id)

                #     ----------------------------------------------------
                if table_name == "AR_JOB_STORY":
                    read_csv_file_for_job_story(request,data.id)
                if table_name == "AR_TEST_STORY":
                    read_csv_file_for_test_story(request,data.id)
                #     --------------------------------------------------
                if table_name == "ArIterations":
                    read_csv_file_for_iteration(request,data.id)
                if table_name == "AR_product" or table_name == "AR_BACKLOG":
                    read_csv_files(request,data.id)
                return redirect(settings.BASE_URL + return_url)
                # return redirect(settings.BASE_URL + 'user-story-view/' + set_statue + "/" + set_statue+"/"+csv_id)
            except IntegrityError:
                msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
                msg_data = msg.notification_desc
                messages.error(request, msg_data)

                # messages.error(request, "Some thing was wrong !")
                set_statue = urlsafe_base64_encode(force_bytes("error"))
    # return redirect(settings.BASE_URL + 'user-story-view/'+set_statue+"/"+set_statue)
    return redirect(settings.BASE_URL + return_url)


@login_required
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    if 'org_id' in request.session:
        del request.session['org_id']
    if 'user_name' in request.session:
        del request.session['user_name']
    auth.logout(request)
    return redirect(settings.BASE_URL)


@register.filter
def get_transaction_id(id):
    get_package_info = get_object_or_404(MembershipHistory, id=id)
    # get_payment = Payment.objects.get(payment_for=get_package_info)
    return get_package_info

@login_required
def index(request):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])

    user_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
    team = AR_team.objects.filter(ORG_id=org_ins).filter(~Q(Team_name = 'None')).count()
    team_data = AR_team.objects.filter(ORG_id=org_ins).filter(~Q(Team_name = 'None'))
    product = AR_product.objects.filter(ORG_ID=org_ins).filter(~Q(Product_name = 'None')).count()
    product_data = AR_product.objects.filter(ORG_ID=org_ins).filter(~Q(Product_name = 'None'))
    backlog = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(~Q(title = 'None')).count()
    backlog_data = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(~Q(title = 'None'))
    user_storyes = AR_USER_STORY.objects.filter(ORG_id=org_ins).filter(~Q(title = 'None')).count()
    user_storyes_data = AR_USER_STORY.objects.filter(ORG_id=org_ins).filter(~Q(title = 'None'))
    itearations = ArIterations.objects.filter(ORG_ID=org_ins).count()
    itearations_data = ArIterations.objects.filter(ORG_ID=org_ins)

    scenario = AR_SCENARIO.objects.filter(ORG_ID=org_ins).count()
    scenario_data = AR_SCENARIO.objects.filter(ORG_ID=org_ins)


    today = datetime.today()
    get_package_info = {} 


           
    all_users = Ar_user.objects.filter(org_id=org_ins).filter(~Q(data_Type = 'Dommy Data')).count()
    all_teams = AR_team.objects.filter(ORG_id=org_ins).filter(~Q(Team_name = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    all_product = AR_product.objects.filter(ORG_ID=org_ins).filter(~Q(Product_name = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    all_backlog = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    all_user_story = AR_USER_STORY.objects.filter(ORG_id=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    get_all_data_cuount = {
     "all_users":all_users,
     "all_product":all_product,
     "all_backlog":all_backlog,
     "all_user_story":all_user_story,
     "all_teams":all_teams
    } 
    all_emebership = {}

            
    return render(request,"admin/dashboard/index.html",{'scenario_data':scenario_data,'scenario':scenario,'user_ins':user_ins,'itearations_data':itearations_data,'user_storyes_data':user_storyes_data,'backlog_data':backlog_data,
                                                        'product_data':product_data,'team_data':team_data,'date':datetime.now(),'itearations':itearations,
                                                        'user_storyes':user_storyes,'team':team,'product':product,'backlog':backlog,'user_name':request.session['user_name'],
                                                        "BASE_URL":settings.BASE_URL,"get_package_info":get_package_info,"get_all_data_cuount":get_all_data_cuount,"all_emebership":all_emebership})


def my_subscription(request):
    user_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    if MembershipHistory.objects.filter(Organization=org_ins).filter(Active=True).exists():
        get_package_info = get_object_or_404(MembershipHistory, Active=True,Organization=org_ins)
    else:
        get_package_info = {}    
    all_users = Ar_user.objects.filter(org_id=org_ins).filter(~Q(data_Type = 'Dommy Data')).filter(~Q(user_type = 'Root')).count()
    all_teams = AR_team.objects.filter(ORG_id=org_ins).filter(~Q(Team_name = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    all_product = AR_product.objects.filter(ORG_ID=org_ins).filter(~Q(Product_name = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    all_backlog = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    all_user_story = AR_USER_STORY.objects.filter(ORG_id=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
    get_all_data_cuount = {
     "all_users":all_users,
     "all_product":all_product,
     "all_backlog":all_backlog,
     "all_user_story":all_user_story,
     "all_teams":all_teams
    } 
    if MembershipHistory.objects.filter(Organization=org_ins).exists():
        all_emebership = MembershipHistory.objects.filter(Organization=org_ins).order_by("-id")
    else:
        all_emebership = {}  
    return render(request,"admin/dashboard/my_membership.html",{'user_ins':user_ins,'user_name':request.session['user_name'],"BASE_URL":settings.BASE_URL,"get_package_info":get_package_info,"get_all_data_cuount":get_all_data_cuount,"all_emebership":all_emebership})

def get_package_limit(org_id,check_for):
    status = False
    org_ins = get_object_or_404(AR_organization,id=org_id)
    
    if MembershipHistory.objects.filter(Organization=org_ins).filter(Active=True).filter(end_date__gte=datetime.today()).exists():
        get_package = get_object_or_404(MembershipHistory,Organization=org_ins,Active=True,end_date__gte=datetime.today())
        #  ---------------------------CHECK USER START---------------------------------
        if check_for == "users":
            data_get = Ar_user.objects.filter(org_id=org_ins).filter(~Q(data_Type = 'Dommy Data')).filter(~Q(user_type = 'Root')).count()
            if get_package.Invite_user == 0:
                status = True
            else:
                if data_get < get_package.Invite_user:
                    status = True
        #  ---------------------------CHECK USER END---------------------------------      
        #  ---------------------------CHECK Teams START---------------------------------
        if check_for == "Teams":
            data_get = AR_team.objects.filter(ORG_id=org_ins).filter(~Q(Team_name = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
            if get_package.Team == 0:
                status = True
            else:
                if data_get < get_package.Team:
                    status = True
        #  ---------------------------CHECK Teams END---------------------------------      

        #  ---------------------------CHECK Product START---------------------------------
        if check_for == "Product":
            data_get = AR_product.objects.filter(ORG_ID=org_ins).filter(~Q(Product_name = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
            if get_package.Product == 0:
                status = True
            else:
                if data_get < get_package.Product:
                    status = True
        #  ---------------------------CHECK Product END---------------------------------       
        #  ---------------------------CHECK Backlogs START---------------------------------
        if check_for == "Backlogs":
            data_get = AR_BACKLOG.objects.filter(ORG_ID=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
            if get_package.Backlog_per_Product == 0:
                status = True
            else:
                if data_get < get_package.Backlog_per_Product:
                    status = True
        #  ---------------------------CHECK Backlogs END---------------------------------    
        #  ---------------------------CHECK User_Stories START---------------------------------
        if check_for == "User_Stories":
            data_get = AR_USER_STORY.objects.filter(ORG_id=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
            if get_package.User_story == 0:
                status = True
            else:
                if data_get < get_package.User_story:
                    status = True
        #  ---------------------------CHECK User_Stories END---------------------------------
        #  ---------------------------CHECK Job_Stories START---------------------------------
        if check_for == "Job_Stories":
            data_get = AR_JOB_STORY.objects.filter(ORG_id=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
            if get_package.Job_story == 0:
                status = True
            else:
                if data_get < get_package.Job_story:
                    status = True
        #  ---------------------------CHECK Job_Stories END---------------------------------
        #  ---------------------------CHECK Test_Stories START---------------------------------
        if check_for == "Test_Stories":
            data_get = AR_TEST_STORY.objects.filter(ORG_id=org_ins).filter(~Q(title = 'None')).filter(~Q(data_Type = 'Dommy Data')).count()
            if get_package.Test_story == 0:
                status = True
            else:
                if data_get < get_package.Test_story:
                    status = True
        #  ---------------------------CHECK Test_Stories END---------------------------------
        # "True meens user can add data"
    return status

