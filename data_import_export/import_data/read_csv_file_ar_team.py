import io,csv
from django.shortcuts import render , HttpResponse,get_object_or_404
from account.models import Ar_user,AR_organization,AR_organization_status,Notification,ArHelpContect
from datetime import datetime
from data_import_export.models import import_files_data
from django.contrib.auth.models import User
from manage_product.models import AR_team
import string
import random
from django.contrib import messages
from agileproject import settings
from dashboard.views import get_package_limit


def read_ar_team_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
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

    total_team = 0
    import_team = 0
    empty = 0
    exists_team = 0
    other_error = 0
    i = 2
    try:
        for item in file_name:
            import_status = False
            # print("===")
            # print("0:"+item[0]+"====1:"+item[1]+"====2:"+item[2]+"====3:"+item[3]+"====4:"+item[4]+"====5:"+item[5]+"====6:"+item[6]+"====7:"+item[7])
            # print("===")
            if item[0] != "":
                if AR_team.objects.filter(Team_name=item[0]).filter(ORG_id=org_ins).exists():
                    exists_team += 1
                    msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : "+str(i)+" : "+ str(item[0]) + " : "+str(msg_data)+" : " + str(
                        datetime.now()) + "\r\n")
                    import_status = True

                else:
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

                    # update_date = item[7]
                    # if update_date == "":
                    #     update_date = datetime.now()
                    # create_date = item[5]
                    # if create_date == "":
                    #     create_date = datetime.now()
                    update_date = datetime.now()
                    create_date = datetime.now()

                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data" 

                    AR_team_create = AR_team(Team_name=item[0],data_Type=set_dummy_data,Team_description=item[1],ORG_id=org_ins,create_by=created_by_ins,create_dt=create_date,update_by=updateded_by_ins,update_dt=update_date)
                    try:
                        get_status = get_package_limit(org_ins.id,"Teams")
                        
                        if set_dummy_data == "Dommy Data":
                              get_status =True
                        
                        if get_status:
                            AR_team_create.save()
                            team_members = None
                            import_team += 1
                            if item[3] != "":
                                team_member_in_list = item[3].split("|")
                                try:
                                    member_id = int(team_member_in_list[0])
                                    if Ar_user.objects.filter(id__in=team_member_in_list).filter(org_id=org_ins).exists():
                                        team_members = Ar_user.objects.filter(id__in=team_member_in_list).filter(org_id=org_ins)
                                except:
                                    if Ar_user.objects.filter(user_name__in=team_member_in_list).filter(org_id=org_ins).exists():
                                        team_members = Ar_user.objects.filter(user_name__in=team_member_in_list).filter(org_id=org_ins)
                            # print(team_members)      # member list
                            file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : Team create successfully, : " + str(datetime.now()) + "\r\n")
                            if team_members != None:
                                AR_team_create.Team_member_list.set(team_members)
                            import_status = True
                        else:
                            msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : "+str(msg_data)+" : " + str(datetime.now()) + "\r\n")    
                    except Exception as e:
                        import_status = False
                        other_error += 1
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")
            else:
                empty += 1
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : team name is empty. : " + str(datetime.now()) + "\r\n")
            i +=1
            total_team += 1
    except Exception as e:
        other_error += 1
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")

    file2.close()
    empty_mess = ""
    exists_mess = ""
    if empty > 0:
       empty_mess = str(empty)+" team title is empty.,,"
    if exists_team > 0:
        exists_mess = str(exists_team)+" team already exists."
    file_data_mess = str(total_team)+" total teams.,,"+str(import_team)+" team import.,,"+empty_mess+exists_mess+str(other_error)+" other error"
    file_name_txt_in_array = file_name_txt.split("media")
    if set_data_type== "default" :
        pass
    else:
        if import_team == 0 :
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="import_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        else:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
    import_files_data.objects.filter(id=file_ins.id).update( error_log=file_name_txt_in_array[1],file_data=file_data_mess,)
    return True

