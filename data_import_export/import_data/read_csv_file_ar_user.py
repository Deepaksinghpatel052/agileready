import io,csv
from django.shortcuts import render , HttpResponse,get_object_or_404
from account.models import Ar_user,AR_organization,AR_organization_status,Notification,ArHelpContect
from datetime import datetime
from data_import_export.models import import_files_data
from django.contrib.auth.models import User
import string
import random
from agileproject import settings
from agileproject.tokens import account_activation_token
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
import email.message
import smtplib
from dashboard.views import get_package_limit

from django.contrib import messages


def read_ar_user_csv(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
    file2 = open(file_name_txt, "w+")
    csv_file = file_ins.files
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    get_data = csv.reader(io_string, delimiter=',', quotechar="|")
    get_data2 = ""
    file_name = get_data
    i=2
    created_by = user_id
    updated_by = user_id

    total_u = 0
    import_u = 0
    emty_u = 0
    already_ex = 0
    active_user = 0
    vrification_link = 0
    other_error = 0
    data_import = False
    try:
        for item in file_name:
            data_import_status = False
            if item[2] == "":
                emty_u += 1
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : user email is empty. : " + str(datetime.now()) + "\r\n")
            else:
                if User.objects.filter(email=item[2]).exists():
                    already_ex += 1
                    msg = get_object_or_404(Notification, page_name="E mail", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : "+str(i)+" : "+ str(item[2]) + " : "+msg_data+" : " + str(
                        datetime.now()) + "\r\n")
                    data_import = True
                else:
                    if item[8] != "0":
                        if Ar_user.objects.filter(phone=item[8]).exists():
                            msg = get_object_or_404(Notification, page_name="Phone", notification_key="Exists")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(file_name_value) + " : row no. : "+str(i)+" : "+ str(item[8]) + " : "+msg_data+" : " + str(
                                datetime.now()) + "\r\n")
                    set_user_status = False
                    if item[3] == "True":
                        set_user_status = True
                    user_password = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])
                    print("===="+user_password)

                #     User Entry -----------------
                    user = User.objects.create_user(username=item[2], email=item[2], password=user_password, is_active=set_user_status)
                    try:
                        user.save()
                        import_u += 1
                    except:
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : Something was wrong in this file : " + str(datetime.now()) + "\r\n")
                    created_bt = user_id

                    if item[20] != "":
                        try:
                            created_by_ins_id = int(item[20])
                            if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                                created_by = created_by_ins.id
                        except:
                            if Ar_user.objects.filter(user_name=item[20]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[20], org_id=org_ins)
                                created_by = created_by_ins.id
                    if item[22] != "":
                        try:
                            updateded_by_ins_id = int(item[22])
                            if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                                updated_by = updateded_by_ins.id
                        except:
                            if Ar_user.objects.filter(user_name=item[22]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[22], org_id=org_ins)
                                updated_by = updateded_by_ins.id
                    update_date = item[23]
                    if update_date == "":
                        update_date = datetime.now()
                    create_date = item[21]

                    if create_date == "":
                        create_date = datetime.now()

                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"    
                    Ar_users = Ar_user(status=item[14], user_id=user.id, user_name=item[0], country=item[7],user_type="User", city=item[4], state=item[5], zip=item[6], phone=item[8], org_id=org_ins,created_by=created_by,updated_by=updated_by,created_dt=create_date,updated_dt=update_date,data_Type=set_dummy_data)
                    try:
                        get_status = get_package_limit(org_ins.id,"User_Stories")
                        
                        if set_dummy_data == "Dommy Data":
                              get_status =True
                        
                        if get_status:
                            Ar_users.save()
                            
                            if set_user_status == False:
                                vrification_link += 1
                                send_email(Ar_users, user, org_ins, user_password)
                            else:
                                active_user += 1
                            data_import = True
                            msg_data = get_object_or_404(Notification, page_name="User Story View", notification_key="Add")
                            file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : user add successfully. : " + str(datetime.now()) + "\r\n")
                        else:
                            msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(item[0]) + " : row no. : " + str(i) + " : " + str(item[0]) + " : Subscription limit expiry. : " + str(datetime.now()) + "\r\n")
                    except:
                        other_error += 1
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : Something was wrong in this file : " + str(datetime.now()) + "\r\n")
            i += 1
            total_u += 1
    except:
        other_error += 1
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : Something was wrong in this file : " + str(datetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    mepte_mes = ""
    already_ex_mes = ""
    if emty_u > 0:
        mepte_mes = str(emty_u)+" user email is empty.,,"
    else:
        mepte_mes = ""

    if already_ex > 0:
        already_ex_mes = str(already_ex)+" user email already exists.,,"
    else:
        already_ex_mes = ""


    if vrification_link > 0:
        vrification_link_mes = str(vrification_link)+" user not active varification link is sent to user email.,,"
    else:
        vrification_link_mes = ""
    set_string_data = str(total_u)+" total users.,,"+str(import_u)+" user import.,,"+mepte_mes+already_ex_mes+str(active_user)+" user is active.,,"+vrification_link_mes+str(other_error)+" other error"

    # -------------------------------------------------
    if set_data_type== "default" :
        pass
    else:
        if import_u == 0 :
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="import_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        else:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
    # -------------------------------------------------
    import_files_data.objects.filter(id=file_ins.id).update(upload_status=data_import, error_log=file_name_txt_in_array[1],file_data=set_string_data)
    # print("DSP")
    # print(file_name_txt_in_array)
    # print("DSP")
    return True



# ===========================================================================================================================================
def read_ar_user_csv_text(request,set_data_type,file_ins,org_ins,file_name_value,file_name_txt,user_id,set_dummy_data=""):
    file2 = open(file_name_txt, "w+")
    csv_file = file_ins.files
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    get_data = csv.reader(io_string, delimiter=',', quotechar="|")
    get_data2 = ""
    file_name = get_data
    i=2
    created_by = user_id
    updated_by = user_id

    total_u = 0
    import_u = 0
    emty_u = 0
    already_ex = 0
    active_user = 0
    vrification_link = 0
    other_error = 0
    data_import = False
    try:
        for item in file_name:
            data_import_status = False
            if item[2] == "":
                emty_u += 1
                file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : user email is empty. : " + str(datetime.now()) + "\r\n")
            else:
                if User.objects.filter(email=item[2]).exists():
                    already_ex += 1
                    msg = get_object_or_404(Notification, page_name="E mail", notification_key="Exists")
                    msg_data = msg.notification_desc
                    file2.write("Error : " + str(file_name_value) + " : row no. : "+str(i)+" : "+ str(item[2]) + " : "+msg_data+" : " + str(
                        datetime.now()) + "\r\n")
                    data_import = True
                else:
                    if item[8] != "0":
                        if Ar_user.objects.filter(phone=item[8]).exists():
                            msg = get_object_or_404(Notification, page_name="Phone", notification_key="Exists")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(file_name_value) + " : row no. : "+str(i)+" : "+ str(item[8]) + " : "+msg_data+" : " + str(
                                datetime.now()) + "\r\n")
                    set_user_status = False
                    if item[3] == "True":
                        set_user_status = True
                    user_password = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])
                    print("===="+user_password)

                #     User Entry -----------------
                    user = User.objects.create_user(username=item[2], email=item[2], password=user_password, is_active=set_user_status)
                    try:
                        user.save()
                        import_u += 1
                    except Exception as e:
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")
                    created_bt = user_id

                    if item[20] != "":
                        try:
                            created_by_ins_id = int(item[20])
                            if Ar_user.objects.filter(id=created_by_ins_id).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, pk=created_by_ins_id)
                                created_by = created_by_ins.id
                        except:
                            if Ar_user.objects.filter(user_name=item[20]).filter(org_id=org_ins).exists():
                                created_by_ins = get_object_or_404(Ar_user, user_name=item[20], org_id=org_ins)
                                created_by = created_by_ins.id
                    if item[22] != "":
                        try:
                            updateded_by_ins_id = int(item[22])
                            if Ar_user.objects.filter(id=updateded_by_ins_id).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, pk=updateded_by_ins_id)
                                updated_by = updateded_by_ins.id
                        except:
                            if Ar_user.objects.filter(user_name=item[22]).filter(org_id=org_ins).exists():
                                updateded_by_ins = get_object_or_404(Ar_user, user_name=item[22], org_id=org_ins)
                                updated_by = updateded_by_ins.id
                    update_date = item[23]
                    if update_date == "":
                        update_date = datetime.now()
                    create_date = item[21]

                    if create_date == "":
                        create_date = datetime.now()

                    if set_dummy_data == "":
                        set_dummy_data = "ORG Data"    
                    Ar_users = Ar_user(status=item[14], user_id=user.id, user_name=item[0], country=item[7],user_type="User", city=item[4], state=item[5], zip=item[6], phone=item[8], org_id=org_ins,created_by=created_by,updated_by=updated_by,created_dt=create_date,updated_dt=update_date,data_Type=set_dummy_data)
                    try:
                        get_status = get_package_limit(org_ins.id,"User_Stories")
                        
                        if set_dummy_data == "Dommy Data":
                            get_status =True
                        
                        if get_status:
                            Ar_users.save()
                            
                            if set_user_status == False:
                                vrification_link += 1
                                send_email(Ar_users, user, org_ins, user_password)
                            else:
                                active_user += 1
                            data_import = True
                            msg_data = get_object_or_404(Notification, page_name="User Story View", notification_key="Add")
                            file2.write("Success : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : user add successfully. : " + str(datetime.now()) + "\r\n")
                        else:
                            msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                            msg_data = msg.notification_desc
                            file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : " + str(item[0]) + " : user add successfully. : " + str(datetime.now()) + "\r\n")
                    except Exception as e:
                        other_error += 1
                        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " :"+str(e)+" : " + str(datetime.now()) + "\r\n")
            i += 1
            total_u += 1
    except Exception as e:
        other_error += 1
        file2.write("Error : " + str(file_name_value) + " : row no. : " + str(i) + " : "+str(e)+" : " + str(datetime.now()) + "\r\n")
    file2.close()
    file_name_txt_in_array = file_name_txt.split("media")

    mepte_mes = ""
    already_ex_mes = ""
    if emty_u > 0:
        mepte_mes = str(emty_u)+" user email is empty.,,"
    else:
        mepte_mes = ""

    if already_ex > 0:
        already_ex_mes = str(already_ex)+" user email already exists.,,"
    else:
        already_ex_mes = ""


    if vrification_link > 0:
        vrification_link_mes = str(vrification_link)+" user not active varification link is sent to user email.,,"
    else:
        vrification_link_mes = ""
    set_string_data = str(total_u)+" total users.,,"+str(import_u)+" user import.,,"+mepte_mes+already_ex_mes+str(active_user)+" user is active.,,"+vrification_link_mes+str(other_error)+" other error"


    # -------------------------------------------------
    if set_data_type== "default" :
        pass
    else:
        if import_u == 0 :
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="import_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        else:
            msg = get_object_or_404(Notification, page_name="Import_file", notification_key="upload")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
    # -------------------------------------------------

    import_files_data.objects.filter(id=file_ins.id).update(upload_status=data_import, error_log=file_name_txt_in_array[1],file_data=set_string_data)
    # print("DSP")
    # print(file_name_txt_in_array)
    # print("DSP")
    return True



def send_email(ar_user_ins,user_ins,org_info,password):
    # corrent_user_info => user_ins
    user_email = user_ins.username
    uid = urlsafe_base64_encode(force_bytes(user_ins.id))
    token = account_activation_token.make_token(user_ins)
    varification_link = settings.BASE_URL + "account/activate/" + uid + "/" + token
    logo_image = settings.BASE_URL + 'static/img/basic/logo.png'
    data_content = {"BASE_URL": settings.BASE_URL, "user_name": ar_user_ins.user_name,
                    "organization_name": org_info.organization_name, "user_email": user_email, "password": password,
                    "logo_image": logo_image, "varification_link": varification_link}
    email_content = render_to_string('email_template/email_send_for_invite_user.html', data_content)
    msg = email.message.Message()
    msg['Subject'] = 'Invitation Link From Agile Ready'
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = user_email
    password = settings.EMAIL_HOST_PASSWORD
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
