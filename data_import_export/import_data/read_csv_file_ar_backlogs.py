import io,csv
from django.shortcuts import render , HttpResponse,get_object_or_404
from account.models import Ar_user,AR_organization,AR_organization_status,Notification,ArHelpContect
from datetime import datetime
from data_import_export.models import import_files_data
from django.contrib.auth.models import User
from manage_backlogs.models import AR_BACKLOG,AR_BACKLOG_STATUS
from manage_product.models import AR_product,AR_team
import string
import random
from agileproject import settings
from dashboard.views import get_package_limit

from django.contrib import messages



def read_ar_backlogs_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
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
    owner =  get_object_or_404(Ar_user, pk=user_id)
    i = 2

    total_data = 0
    import_data = 0
    empty_data = 0
    exists_data = 0
    other_error = 0

    try:
        for item in file_name:
            # print("===")
            # print("0:"+str(item[0])+"====1:"+str(item[1])+"====2:"+str(item[2])+"====3:"+str(item[3])+"====4:"+str(item[4])+"====5:"+str(item[5])+"====6:"+str(item[6])+"====7:"+str(item[7])+"8:"+str(item[8])+"====9:"+str(item[9])+"====10:"+str(item[10])
            #       +"====11:"+str(item[11]))
            # print("===")
            if item[0] != "":
                if AR_BACKLOG.objects.filter(title=item[0]).filter(ORG_ID=org_ins).exists():
                    exists_data += 1
                    msg = get_object_or_404(Notification, page_name="Manage Backlog", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : "+str(i)+" : "+ str(item[0]) + " : "+str(msg_data)+" : " + str(datetime.now()) + "\r\n")
                else:
                    updated_dt = datetime.now()
                    created_dt = datetime.now()
                    # updated_dt = item[10]
                    # if updated_dt == "":
                    #     updated_dt = datetime.now()
                    # created_dt = item[8]
                    # if created_dt == "":
                    #     created_dt = datetime.now()
                    product_ins = None
                    if item[5] != "":
                        try:
                            product_id = int(item[5])
                            if AR_product.objects.filter(id=product_id).filter(ORG_ID=org_ins).exists():
                                product_ins = get_object_or_404(AR_product, id=product_id, ORG_ID=org_ins)
                        except:
                            if AR_product.objects.filter(Product_name=item[5]).filter(ORG_ID=org_ins).exists():
                                product_ins = get_object_or_404(AR_product, Product_name=item[5], ORG_ID=org_ins)
                    # ============== create_by update_by start

                    backlog_status_ins = None
                    if item[6] != "":
                        try:
                            backlog_ins = int(item[6])
                            if AR_BACKLOG_STATUS.objects.filter(id=backlog_ins).exists():
                                backlog_status_ins = get_object_or_404(AR_BACKLOG_STATUS, id=backlog_ins)
                        except:
                            if AR_BACKLOG_STATUS.objects.filter(bl_status_key=item[6]).exists():
                                backlog_status_ins = get_object_or_404(AR_BACKLOG_STATUS, bl_status_key=item[6])

                    if item[7] != "":
                        try:
                            created_by_ins_id = int(item[7])
                            if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[7]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[7], org_id=org_ins)
                    if item[9] != "":
                        try:
                            updateded_by_ins_id = int(item[9])
                            if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[9]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[9], org_id=org_ins)

                    if item[1] != "":
                        try:
                            owner_id = int(item[1])
                            if Ar_user.objects.filter(id=owner_id).filter(org_id=org_ins).exists():
                                owner = get_object_or_404(Ar_user, pk=owner_id)
                        except:
                            if Ar_user.objects.filter(user_name=item[1]).filter(org_id=org_ins).exists():
                                owner = get_object_or_404(Ar_user, user_name=item[1], org_id=org_ins)

                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"
                    backlog_create = AR_BACKLOG(title=item[0],data_Type=set_dummy_data,backlog_score=0,Backlog_size=0,owner=owner,product_parent=product_ins,BL_STATUS=backlog_status_ins,ORG_ID=org_ins,
                                                created_by=created_by_ins,created_dt=created_dt,updated_by=updateded_by_ins,updated_dt=updated_dt)



                    try:
                        get_status = get_package_limit(org_ins.id,"Backlogs")
                         
                        if set_dummy_data == "Dommy Data":
                              get_status =True

                        if get_status:
                            backlog_create.save()
                            teams_ins = None
                            if item[4] != "":
                                teams_in_list = item[4].split("|")
                                try:
                                    team_id = int(teams_in_list[0])
                                    if AR_team.objects.filter(id__in=teams_in_list).filter(ORG_id=org_ins).exists():
                                        teams_ins = AR_team.objects.filter(id__in=teams_in_list).filter(ORG_id=org_ins)
                                except:
                                    if AR_team.objects.filter(Team_name__in=teams_in_list).filter(ORG_id=org_ins).exists():
                                        teams_ins = AR_team.objects.filter(Team_name__in=teams_in_list).filter(ORG_id=org_ins)
                            if teams_ins != None:
                                backlog_create.team_list.set(teams_ins)
                            import_data += 1
                            file2.write("Success: " + str(file_name_value) + " : row no. : " + str(i) + " : Baccklog add succcessfully : " + str(datetime.now()) + "\r\n")
                        else:
                            msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(item[0]) + " : row no. : " + str(i) + " : " + str(item[0]) + " : Subscription limit expiry. : " + str(datetime.now()) + "\r\n")
                    except Exception as e:
                        other_error += 1
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")

            else:
                empty_data += 1
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : backlog name is empty. : " + str(datetime.now()) + "\r\n")
            i += 1
            total_data += 1
    except Exception as e:
        other_error += 1
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+"  : " + str(datetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    empty_mess = ""
    exists_message = ""
    if empty_data > 0:
       empty_mess = str(empty_data)+" backlog title is empty.,,"
    if exists_data > 0:
       exists_message = str(exists_data)+" backlog already exists."

    file_data_mess = str(total_data) + " total backlog.,," + str(import_data) + " backlog import.,," + empty_mess + exists_message + str(other_error) + " other error"

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

