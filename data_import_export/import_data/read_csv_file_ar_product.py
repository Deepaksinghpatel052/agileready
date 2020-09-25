import io,csv
from django.shortcuts import render , HttpResponse,get_object_or_404
from account.models import Ar_user,AR_organization,AR_organization_status,Notification,ArHelpContect
from datetime import datetime
from data_import_export.models import import_files_data
from django.contrib.auth.models import User
from manage_product.models import AR_product
import string
import random
from agileproject import settings
from dashboard.views import get_package_limit


from django.contrib import messages


def read_ar_product_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
    file2 = open(file_name_txt, "w+")
    csv_file = file_ins.files
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    get_data = csv.reader(io_string, delimiter=',', quotechar="|")
    get_data2 = ""
    file_name = get_data
    created_by_ins = get_object_or_404(Ar_user, pk=user_id)
    updateded_by_ins = get_object_or_404(Ar_user, pk=user_id)

    total_data = 0
    import_data = 0
    empty_data = 0
    exists_data = 0
    other_error = 0

    i = 2

    try:
        for item in file_name:
            # print("===")
            # print("0:"+str(item[0])+"====1:"+str(item[1])+"====2:"+str(item[2])+"====3:"+str(item[3])+"====4:"+str(item[4])+"====5:"+str(item[5])+"====6:"+str(item[6])+"====7:"+str(item[7])+"8:"+str(item[8])+"====9:"+str(item[9])+"====10:"+str(item[10])+"====11:"+str(item[11])+"====12:"+str(item[12]))
            # print("===")
            if item[0] != "":
                if AR_product.objects.filter(Product_name=item[0]).filter(ORG_ID=org_ins).exists():
                    exists_data += 1
                    msg = get_object_or_404(Notification, page_name="Manage Products", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write(
                        "Error : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(
                            item[0]) + " : " + str(
                            msg_data) + " : " + str(datetime.now()) + "\r\n")
                else:
                    update_date = datetime.now()
                    create_date = datetime.now()

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

                    try:
                        US_quality_threshold_set = int(item[7])
                    except:
                        US_quality_threshold_set = 0

                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"     
                    product_create = AR_product(Product_name=item[0], Product_description=item[1],
                                                Business_unit=item[3],
                                                US_quality_threshold=US_quality_threshold_set, ORG_ID=org_ins,
                                                create_by=created_by_ins, create_dt=create_date,
                                                update_by=updateded_by_ins,
                                                update_dt=update_date,data_Type=set_dummy_data)
                    # product_create.save()
                    try:
                        get_status = get_package_limit(org_ins.id,"Product")
                        if set_dummy_data == "Dommy Data":
                              get_status =True

                        if get_status:
                            product_create.save()
                            import_data += 1
                            file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : Product add successfully. : " + str(datetime.now()) + "\r\n")
                        else:
                            msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(item[0]) + " : row no. : " + str(i) + " : " + str(item[0]) + " : Subscription limit expiry. : " + str(datetime.now()) + "\r\n")
                    except Exception as e:
                        other_error += 1
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(
                            i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")
            else:
                empty_data += 1
                file2.write(
                    "Error : " + str(file_name_value) + " : row no. : " + str(i) + " : product name is empty. : " + str(
                        datetime.now()) + "\r\n")
            i += 1
            total_data += 1
    except Exception as e:
        empty_data += 1
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(atetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")


    empty_mess = ""
    exists_message = ""
    if empty_data > 0:
        empty_mess = str(empty_data) + " backlog title is empty.,,"
    if exists_data > 0:
        exists_message = str(exists_data) + " backlog already exists."
    file_data_mess = str(total_data) + " total product.,," + str(import_data) + " product import.,," + empty_mess + exists_message + str(other_error) + " other error"

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