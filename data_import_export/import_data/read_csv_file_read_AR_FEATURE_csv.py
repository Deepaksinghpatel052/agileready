import io,csv
from django.shortcuts import get_object_or_404
from datetime import datetime
from account.models import Ar_user,Notification
from data_import_export.models import import_files_data
from django.contrib.auth.models import User
from user_story_view.models import AR_USER_STORY
import string
import random
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from agileproject import settings

from django.contrib import messages




def read_AR_FEATURE_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
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
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : epic capability is empty. : " + str(datetime.now()) + "\r\n")
            else:
                if AR_FEATURE.objects.filter(Feature_key=item[0]).filter(ORG_ID=org_ins).exists():
                    exists_data += 1
                    msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : " + str(msg_data) + " : " + str(datetime.now()) + "\r\n")
                else:
                    # GET apic capability START
                    get_ar_feacher = None
                    if item[2] != "":
                        try:
                            capi_id = int(item[2])
                            if AR_EPIC_CAPABILITY.objects.filter(id=bl_id).filter(ORG_ID=org_ins).exists():
                                get_ar_feacher = get_object_or_404(AR_EPIC_CAPABILITY, pk=capi_id)
                        except:
                            if AR_EPIC_CAPABILITY.objects.filter(Cepic_key=item[2]).filter(ORG_ID=org_ins).exists():
                                get_ar_feacher = get_object_or_404(AR_EPIC_CAPABILITY, Cepic_key=item[2], ORG_ID=org_ins)
                    # print(get_ar_feacher)
                    # GET apic capability END

                    # ============== create_by update_by start
                    if item[4] != "":
                        try:
                            created_by_ins_id = int(item[4])
                            if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[4]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[4], org_id=org_ins)
                    if item[6] != "":
                        try:
                            updateded_by_ins_id = int(item[6])
                            if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[6]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[6], org_id=org_ins)
                    # ============== create_by update_by end

                    # CREATE_DT UPDATE_DT START
                    created_dt = datetime.now()
                    updated_dt = datetime.now()
                    # created_dt = item[5]
                    # if created_dt == "":
                    #     created_dt = datetime.now()
                    # updated_dt = item[7]
                    # if updated_dt == "":
                    #     updated_dt = datetime.now()
                    # print(created_dt)
                    # print(updated_dt)
                    # CREATE_DT UPDATE_DT END

                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"
                    ADD_AR_FEATURE = AR_FEATURE(Feature_key=item[0],data_Type=set_dummy_data,Feature_desc=item[1],CE_ID=get_ar_feacher,ORG_ID=org_ins,create_by=created_by_ins,create_dt=created_dt,update_by=updateded_by_ins,update_dt=created_dt)

                    try:
                        ADD_AR_FEATURE.save()
                        # =========UserStory Start
                        user_stury_set = None
                        if item[4] != "":
                            story_id_in_list = item[4].split("|")
                            try:
                                get_story_id = int(story_id_in_list[0])
                                if AR_USER_STORY.objects.filter(id__in=story_id_in_list).filter(ORG_id=org_ins).exists():
                                    user_stury_set = AR_USER_STORY.objects.filter(id__in=story_id_in_list).filter(
                                        ORG_id=org_ins)
                            except:
                                if AR_USER_STORY.objects.filter(title__in=story_id_in_list).filter(ORG_id=org_ins).exists():
                                    user_stury_set = AR_USER_STORY.objects.filter(title__in=story_id_in_list).filter(
                                        ORG_id=org_ins)
                        if user_stury_set != None:
                            ADD_AR_FEATURE.User_story.set(user_stury_set)
                        msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Add")
                        msg_data = msg.notification_desc
                        file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : " + str(msg_data) + " : " + str(datetime.now()) + "\r\n")
                        import_data += 1
                        # =========UserStory End
                    except Exception as e:
                        other_error += 1
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")

            i += 1
            total_data += 1
    except Exception as e:
        other_error += 1
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(
            i) + " : "+str(e)+"  : " + str(datetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    empty_mess = ""
    exists_message = ""
    if empty_data > 0:
        empty_mess = str(empty_data) + " backlog title is empty.,,"
    if exists_data > 0:
        exists_message = str(exists_data) + " backlog already exists."

    file_data_mess = str(total_data) + " total feature.,," + str(import_data) + " feature import.,," + empty_mess + exists_message + str(other_error) + " other error"

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