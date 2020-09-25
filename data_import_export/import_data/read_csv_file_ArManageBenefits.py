import io,csv
from django.shortcuts import get_object_or_404
from manage_benefits.models import ArManageBenefits
from datetime import datetime
from account.models import Ar_user,Notification
from data_import_export.models import import_files_data
from django.contrib.auth.models import User
import string
import random
from agileproject import settings

from django.contrib import messages


def read_ArManageBenefits_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
    file2 = open(file_name_txt, "w+")
    csv_file = file_ins.files
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    get_data = csv.reader(io_string, delimiter=',', quotechar="|")
    created_by_ins = get_object_or_404(Ar_user, pk=user_id)
    updateded_by_ins = get_object_or_404(Ar_user, pk=user_id)
    file_name = get_data

    total_data = 0
    import_data = 0
    empty_data = 0
    exists_data = 0
    other_error = 0

    i=2
    try:
        for item in file_name:
            if item[1] == "":
                empty_data += 1
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : Benefits title is empty. : " + str(datetime.now()) + "\r\n")
            else:
                if ArManageBenefits.objects.filter(Benefits_title=item[1]).filter(ORG_ID=org_ins).exists():
                    exists_data += 1
                    msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(msg_data)+" : " + str(datetime.now()) + "\r\n")
                else:
                    # test = ""
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
                    # ger instasnce of create_by and update_by user END
                    # GET DATE START
                    created_dt = datetime.now()
                    updated_dt = datetime.now()
                    # created_dt = item[5]
                    # if created_dt == "":
                    #     created_dt = datetime.now()
                    #
                    # updated_dt = item[7]
                    # if updated_dt == "":
                    #     updated_dt = datetime.now()
                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"
                    add_ArManageBenefits = ArManageBenefits(Benefits_title=item[1], data_Type=set_dummy_data,Benefits_description=item[2], Use_in=item[3], ORG_ID=org_ins, created_by=created_by_ins,created_dt=created_dt, updated_by=updateded_by_ins, updated_dt=updated_dt)
                    try:
                        add_ArManageBenefits.save()
                        create_benefite_id = "AR_BENEFITE_" + str(add_ArManageBenefits.id)
                        ArManageBenefits.objects.filter(id=add_ArManageBenefits.id).update(Benefits_id=create_benefite_id)
                        file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : '" + item[1] + "' Benefits add successfully : " + str(datetime.now()) + "\r\n")
                        import_data += 1
                    except Exception as e:
                        other_error += 1
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")
            i += 1
            total_data += 1
    except Exception as e:
        other_error += 1
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " :  "+str(e)+"  (Ar) : " + str(datetime.now()) + "\r\n")

    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    empty_mess = ""
    exists_message = ""
    if empty_data > 0:
        empty_mess = str(empty_data) + " Benefits title is empty.,,"
    if exists_data > 0:
        exists_message = str(exists_data) + " Benefits already exists."

    file_data_mess = str(total_data) + " total Benefits .,," + str(import_data) + " Benefits  import.,," + empty_mess + exists_message + str(other_error) + " other error"

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
