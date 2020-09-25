import io,csv
from django.shortcuts import get_object_or_404
from datetime import datetime
from account.models import Ar_user,Notification
from data_import_export.models import import_files_data
from manage_product.models import AR_product,AR_team
from django.contrib.auth.models import User
from user_story_view.models import AR_USER_STORY
import string
from datetime import date
from manage_backlogs.models import AR_BACKLOG
import random
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from agileproject import settings
from user_story_view.models import AR_USER_STORY
import dateutil.parser
from manage_iterations.models import ArIterations

from django.contrib import messages

def read_ArIterations_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
    file2 = open(file_name_txt, "w+")
    csv_file = file_ins.files
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    get_data = csv.reader(io_string, delimiter=',', quotechar="|")
    created_by_ins = get_object_or_404(Ar_user, pk=user_id)
    updateded_by_ins = get_object_or_404(Ar_user, pk=user_id)
    ar_user_set = get_object_or_404(Ar_user, pk=user_id)
    file_name = get_data


    total_data = 0
    import_data = 0
    empty_data = 0
    exists_data = 0
    other_error = 0

    i=2
    try:
        for item in file_name:
            # print(len(item))
            # print("0:"+item[0]+"====1:"+item[1]+"====2:"+item[2]+"====3:"+item[3]+"====4:"+item[4]+"====5:"+item[5]+"====6:"+item[6]+"====7:"+item[7]+"====8:"+item[8])
            # print("===")
            if item[0] == "":
                empty_data += 1
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : iteration is empty. : " + str(datetime.now()) + "\r\n")
            else:
                if ArIterations.objects.filter(IterationName=item[0]).filter(ORG_ID=org_ins).exists():
                    exists_data += 1
                    msg = get_object_or_404(Notification, page_name="Manage Iteration", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : " + str(msg_data) + " : " + str(datetime.now()) + "\r\n")
                else:
                    # =========owner Start
                    owner = get_object_or_404(Ar_user, pk=user_id)
                    if item[1] != "":
                        try:
                            owner_id = int(item[1])
                            if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                owner = get_object_or_404(Ar_user, pk=owner_id)
                        except ValueError:
                            if Ar_user.objects.filter(user_name=item[1]).filter(org_id=org_ins).exists():
                                owner = get_object_or_404(Ar_user, user_name=item[1], org_id=org_ins)
                    # =========owner End

                    # start - end date START
                    StartDate = item[2]
                    EndDate = item[3]
                    if StartDate == "":
                        StartDate = date.today()

                    if EndDate == '':
                        EndDate = date.today()

                    # start - end date End

                    # =========product Start
                    product_set_dsp = None
                    product_set = None
                    if item[5] != "":
                        try:
                            product_id = int(item[5])
                            # print(AR_product.objects.filter(id=product_id).filter(ORG_ID=org_ins).exists())
                            if AR_product.objects.filter(id=product_id).filter(ORG_ID=org_ins).exists():
                                product_set_dsp = get_object_or_404(AR_product, pk=product_id, ORG_ID=org_ins)
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
                                    backlog_set = get_object_or_404(AR_BACKLOG, title=item[6], ORG_ID=org_ins,product_parent=product_set_dsp)
                    # =========backlog End

                    # user Story START
                    user_stury_set = None
                    if backlog_set != None:
                        if item[7] != "":
                            story_id_in_list = item[7].split("|")
                            try:
                                story_id = story_id_in_list[0]
                                if AR_USER_STORY.objects.filter(id__in=story_id_in_list).filter(backlog_parent=backlog_set).filter(ORG_id=org_ins).exists():
                                    user_stury_set = AR_USER_STORY.objects.filter(id__in=story_id_in_list).filter(backlog_parent=backlog_set).filter(ORG_id=org_ins)
                            except:
                                if AR_USER_STORY.objects.filter(title__in=story_id_in_list).filter(backlog_parent=backlog_set).filter(ORG_id=org_ins).exists():
                                    user_stury_set = AR_USER_STORY.objects.filter(title__in=story_id_in_list).filter(backlog_parent=backlog_set).filter(ORG_id=org_ins)
                    # user Story END

                    # get Team START
                    set_team = None

                    if item[8] != "":
                        try:
                            team_id = int(item[8])
                            if AR_team.objects.filter(id=team_id).filter(ORG_id=org_ins).exists():
                                set_team = get_object_or_404(AR_team, pk=team_id)
                        except ValueError:
                            if AR_team.objects.filter(Team_name=item[8]).filter(ORG_id=org_ins).exists():
                                set_team = get_object_or_404(AR_team, Team_name=item[8], ORG_id=org_ins)
                    # get Team END
                    # ============== create_by update_by start
                    if item[11] != "":
                        try:
                            created_by_ins_id = int(item[11])
                            if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[11]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[11], org_id=org_ins)
                    if item[13] != "":
                        try:
                            updateded_by_ins_id = int(item[13])
                            if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[13]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[13], org_id=org_ins)
                    # ============== create_by update_by end

                    # CREATE_DT UPDATE_DT START
                    created_dt = item[12]
                    updated_dt = datetime.now()
                    created_dt = datetime.now()
                    # if created_dt == "":
                    #     created_dt = datetime.now()
                    # updated_dt = item[14]
                    # if updated_dt == "":
                    #     updated_dt = datetime.now()
                    print(created_dt)
                    print(updated_dt)
                    # CREATE_DT UPDATE_DT END
                    IterationScore = 0
                    IterationSize = 0
                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"
                    add_iteration = ArIterations(IterationName=item[0],data_Type=set_dummy_data, owner=owner, StartDate=StartDate, EndDate=EndDate,
                                         Description=item[4], Product=product_set_dsp, Backlog=backlog_set, Team=set_team,
                                         IterationScore=IterationScore, IterationSize=IterationSize, ORG_ID=org_ins,
                                         create_by=created_by_ins, update_by=updateded_by_ins)
                    try:
                        add_iteration.save()
                        create_itera_id = "AR_ITER_" + str(add_iteration.id)
                        ArIterations.objects.filter(id=add_iteration.id).update(IterationId=create_itera_id)
                        if user_stury_set != None:
                            add_iteration.UserStory.set(user_stury_set)
                        print(StartDate)
                        msg = get_object_or_404(Notification, page_name="Manage Iteration", notification_key="Add")
                        msg_data_2 = msg.notification_desc
                        file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : Iteration add successfully. : " + str(datetime.now()) + "\r\n")
                        import_data += 1
                    except Exception as e:
                        other_error += 1
                        msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
                        msg_data = msg.notification_desc
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")


            i += 1
            total_data += 1
    except Exception as e:
        other_error += 1
        msg = get_object_or_404(Notification, page_name="Import_file", notification_key="Invalid_file")
        msg_data = msg.notification_desc
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : (Ar) : " + str(datetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    empty_mess = ""
    exists_message = ""
    if empty_data > 0:
        empty_mess = str(empty_data) + " Iterations title is empty.,,"
    if exists_data > 0:
        exists_message = str(exists_data) + " Iterations already exists."

    file_data_mess = str(total_data) + " total Iterations .,," + str(import_data) + " Iterations  import.,," + empty_mess + exists_message + str(other_error) + " other error"


    # -------------------------------------------------
    if set_data_type== "default" :
        pass
    else:
        if import_data == 0 :
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="import_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        else:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
    # -------------------------------------------------

    import_files_data.objects.filter(id=file_ins.id).update(error_log=file_name_txt_in_array[1],file_data=file_data_mess)
    return True