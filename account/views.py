from django.contrib.auth import login
from django.shortcuts import render , HttpResponse,get_object_or_404,redirect
from django.http import HttpResponse, JsonResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
from .models import Ar_user,AR_organization,AR_organization_status,Notification,ArHelpContect,ArUserProfile,ArAccountRemoveRequest
from django.db.models import Q,Subquery,Count
import string
import random
from django.contrib import messages
import smtplib
from agileproject import settings
from agileproject.tokens import account_activation_token
import email.message
from django.template.loader import render_to_string
# Create your views here.
from data_import_export.models import import_files_data
from data_import_export.views import read_csv_file
# import all module start
from manage_product.models import AR_team,AR_product
from manage_backlogs.models import AR_BACKLOG
from user_story_view.models import AR_USER_STORY
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from manage_features.models import AR_FEATURE
from subscription.models import MembershipHistory
from user_story_points.models import ArUserStoryPoints
from dashboard.views import get_package_limit
from datetime import datetime
from subscription.views import add_data_in_membership_historty_default,update_payment_status_default
from subscription.models import Subscription,MembershipHistory
from feedback.models import ArEmailSendToAdmin
# import all module end



def test_mail(request):
    default = "Test"
    # logo_image = settings.BASE_URL + 'static/img/basic/logo.png'
    # get_data = ArAccountRemoveRequest.objects.filter(Mail_send_status=False)
    # yourname ="Admin"
    # data_content = {"BASE_URL": settings.BASE_URL, "user_name":yourname, "logo_image":logo_image, "get_data":get_data}
    
  
    return HttpResponse(default)

def set_default_value_for_org(org_id,user_id):

    org_id = org_id
    user_id = user_id
    get_user_instant = Ar_user.objects.get(id=user_id)
    org_ins = AR_organization.objects.get(id=org_id)
    default = 'None'

    # Nonne for Team start
    res = AR_team.objects.filter(Team_name=default).filter(ORG_id=org_ins).exists()
    if AR_team.objects.filter(Team_name=default).filter(ORG_id=org_ins).exists():
        print("already")
    else:
        add_team = AR_team(Team_name=default, Team_description=default, ORG_id=org_ins, create_by=get_user_instant,
                           update_by=get_user_instant)
        add_team.save()
    # Nonne for Team END

    # AR_product for Team start
    if AR_product.objects.filter(Product_name=default).filter(ORG_ID=org_ins).exists():
        print("already")
    else:
        add_team = AR_product(Product_name=default, Product_description=default, ORG_ID=org_ins,
                              create_by=get_user_instant,
                              update_by=get_user_instant)
        add_team.save()
    # AR_product for Team end

    # AR_BACKLOG for Team start
    if AR_BACKLOG.objects.filter(title=default).filter(ORG_ID=org_ins).exists():
        print("already")
    else:
        add_team = AR_BACKLOG(title=default, ORG_ID=org_ins, created_by=get_user_instant, updated_by=get_user_instant,
                              backlog_score=0, Backlog_size=0)
        add_team.save()
    # AR_BACKLOG for Team end

    # AR_USER_STORY for Team start
    if AR_USER_STORY.objects.filter(title=default).filter(ORG_id=org_ins).exists():
        print("already")
    else:
        add_team = AR_USER_STORY(title=default, ORG_id=org_ins, created_by=get_user_instant,
                                 updated_by=get_user_instant, ac_readability_score=0, convo_readability_score=0,
                                 readiness_quality_score=0)
        add_team.save()
    # AR_USER_STORY for Team end

    # AR_EPIC_CAPABILITY for Team start
    if AR_EPIC_CAPABILITY.objects.filter(Cepic_key=default).filter(ORG_ID=org_ins).exists():
        print("already")
    else:
        add_team = AR_EPIC_CAPABILITY(Cepic_key=default, Cepic_desc=default, ORG_ID=org_ins,
                                      created_by=get_user_instant, update_by=get_user_instant)
        add_team.save()
    # AR_EPIC_CAPABILITY for Team end

    # AR_FEATURE for Team start
    if AR_FEATURE.objects.filter(Feature_key=default).filter(ORG_ID=org_ins).exists():
        print("already")
    else:
        add_team = AR_FEATURE(Feature_key=default, Feature_desc=default, ORG_ID=org_ins, create_by=get_user_instant,
                              update_by=get_user_instant)
        add_team.save()
    # AR_FEATURE for Team end

    # AR_FEATURE for Team start
    if ArUserStoryPoints.objects.filter(Point_Key=default).filter(ORG_ID=org_ins).exists():
        print("already")
    else:
        add_team = ArUserStoryPoints(Point_Key=default, Point_Description=default, Point_score=0, ORG_ID=org_ins,
                                     create_by=get_user_instant, update_by=get_user_instant)
        add_team.save()
    # AR_FEATURE for Team end
    return True

def remove_root_user_account(request):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    user_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
    add_request = ArAccountRemoveRequest(RootUser=user_ins.user_name,userEmail=user_ins.user.username,ORG_ID=org_ins)
    add_request.save()
    msg = get_object_or_404(Notification, page_name="root_account_remove", notification_key="request")
    msg_data = msg.notification_desc
    messages.info(request, msg_data)
    return redirect(settings.BASE_URL + 'account-settings')

def set_dummy_data(request,org_id,user_id,set_data_type,set_dummy_data=""):
    default = "Test"
    if import_files_data.objects.filter(dommy_set=1).exists():
        get_data =  import_files_data.objects.filter(dommy_set=1).order_by("priority")
        set_list = []

        for item in get_data:
            set_list.append(item.id)

        # return HttpResponse("org_id = " + set_dummy_data)
        read_csv_file(request,set_list, org_id, user_id,set_data_type,set_dummy_data)
        # return HttpResponse("org_id = " + set_dummy_data)
    else:
        print("sdjfdhbv")
    return True




@csrf_exempt
def get_help_content(request):
    page_name = request.POST["page_name"]
    if ArHelpContect.objects.filter(Page_slug=page_name).exists():
        get_help_content = get_object_or_404(ArHelpContect, Page_slug=page_name)
    else:
        get_help_content = get_object_or_404(ArHelpContect, Page_slug="dashboard")
    # return HttpResponse(page_name)
    return render(request, 'admin/dashboard/help_content.html', {'get_help_content': get_help_content,"BASE_URL":settings.BASE_URL})





def account_activate(request,uidb64,token):
    message_text = ""
    message = ""
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        get_user_info = Ar_user.objects.get(user=user)

        # set_default_value_for_org(get_user_info.org_id.id,get_user_info.id)
        # set_dummy_data(get_user_info.org_id.id ,get_user_info.id,'default',"Dommy Data")
        if user is not None:
            if get_user_info.org_id.Activate_status:
                # request.session['user_id'] = get_user_info.id
                # request.session['org_id'] = get_user_info.org_id.id
                # request.session['user_name'] = get_user_info.user_name
                # request.session['user_type'] = get_user_info.user_type
                # auth.login(request,user_auth)
                if get_user_info.user_type == "Root":
                    get_free_sub= Subscription.objects.filter(All_member=True).filter(Active=True).filter(Price=0).filter(Undefine_price=False)
                    if len(get_free_sub) == 1 :
                        get_info  = add_data_in_membership_historty_default(request,get_free_sub[0].id,get_user_info.id,get_user_info.org_id.id)
                        update_payment_status_default(request,get_info['data']["payment_obj_id"],"","",get_user_info.id,get_user_info.org_id.id)
                    add_email = ArEmailSendToAdmin(User_Email=user.username,Email_Subjects="Root Account Activated",Ar_user=get_user_info,ORG_ID=get_user_info.org_id)
                    add_email.save()
                else:
                    add_email = ArEmailSendToAdmin(User_Email=user.username,Email_Subjects="Invite User Activated",Ar_user=get_user_info,ORG_ID=get_user_info.org_id)
                    add_email.save()
                message = '0'
            else:
                msg = get_object_or_404(Notification, page_name="Login", notification_key="org_account_inactivated")
                msg_data = msg.notification_desc
                message_text = msg_data
                message = "2"
        else:
           message = '1'
    else:
        message = '1'

    return render(request, 'web/account/index.html', {'message': message,"BASE_URL":settings.BASE_URL})


def index(request):
    ###########################
    get_user_instant = User.objects.get(email='deepaksinghpatel052@gmail.com')
    uid=urlsafe_base64_encode(force_bytes(get_user_instant.id))
    token = account_activation_token.make_token(get_user_instant)
    email_content = settings.BASE_URL+"account/activate/"+uid+"/"+token
    msg = email.message.Message()
    msg['Subject'] = 'Account Create successfully'
    msg['From'] = settings.EMAIL_HOST_USER
    msg['To'] = 'deepaksinghpatel052@gmail.com'
    password = settings.EMAIL_HOST_PASSWORD
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(email_content)
    s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    return HttpResponse("test")






@csrf_exempt
def register(request):
    if request.method == "POST":
        print(request.POST)
        yourname = request.POST["yourname"]
        user_email = request.POST["user_email"]
        user_in_dis = user_email.split("@")
        username = user_in_dis[0]
        password = request.POST["password"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip_code = request.POST["zip_code"]
        country = request.POST["country"]
        number = request.POST["number"]
        organization = request.POST["organization"]
        organization_url = request.POST["organization_url"]
        if User.objects.filter(email=user_email).exists():
            msg = get_object_or_404(Notification, page_name="E mail", notification_key="Exists")
            msg_data = msg.notification_desc
            # messages.error(request, title + " " + msg_data)
            return JsonResponse({"status":"0","message":user_email + " , " + msg_data})
        
        else:
            if Ar_user.objects.filter(phone=number).exists():
                msg = get_object_or_404(Notification, page_name="Phone", notification_key="Exists")
                msg_data = msg.notification_desc
                return JsonResponse({"status": "0", "message": number + " , " + msg_data})
            else:
                if AR_organization.objects.filter(organization_url=organization_url).filter(~Q(organization_url="")).exists():
                    msg = get_object_or_404(Notification, page_name="Organization Url", notification_key="Exists")
                    msg_data = msg.notification_desc
                    return JsonResponse({"status": "0", "message": organization_url + " , " + msg_data})
                else:
                    org_id = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])
                    while AR_organization.objects.filter(org_id=org_id).exists():
                        org_id = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])


                    user = User.objects.create_user(username=user_email, email=user_email,password=password,is_active=False)
                    user.save()
                    get_user_instant = User.objects.get(email=user_email)
                    if AR_organization.objects.filter(organization_url=organization_url).exists():
                        pass
                    else:
                        ar_org= AR_organization(org_id=org_id,organization_name=organization,organization_url=organization_url,created_by=user,update_by=user)
                        ar_org.save()
                    org_ins = get_object_or_404(AR_organization, organization_url=organization_url)



                    Ar_users = Ar_user(status = "Active", user_id=user.id,user_name=yourname,country=country, city=city,state=state,zip=zip_code,phone=number,org_id=org_ins)
                    Ar_users.save()



                    add_email = ArEmailSendToAdmin(User_Email=user.username,Email_Subjects="New Root Account",Ar_user=Ar_users,ORG_ID=org_ins)
                    add_email.save()


                    # data_res = set_default_value_for_org(org_ins.id, Ar_users.id)
                    # data_res = set_dummy_data(org_ins.id, Ar_users.id,"Dommy Data")


                    uid = urlsafe_base64_encode(force_bytes(get_user_instant.id))
                    # return JsonResponse({"status": "1", "message": "msg_data" + " " + user_email + "' !"})
                    token = account_activation_token.make_token(get_user_instant)
                    varification_link = settings.BASE_URL + "account/activate/" + uid + "/" + token
                    # print(varification_link)
                    ################################################ EMAL SEND CODE START ##############
                    logo_image = settings.BASE_URL + 'static/img/basic/logo.png'
                    data_content = {"BASE_URL": settings.BASE_URL, "yourname":yourname, "user_email": user_email,"password":password,"logo_image":logo_image,"varification_link":varification_link}
                    email_content = render_to_string('email_template/email_send_for_create_new_account.html', data_content)
                    msg = email.message.Message()
                    msg['Subject'] = 'Account Create successfully'
                    msg['From'] = settings.EMAIL_HOST_USER
                    msg['To'] = user_email
                    password = settings.EMAIL_HOST_PASSWORD
                    msg.add_header('Content-Type', 'text/html')
                    msg.set_payload(email_content)
                    s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
                    s.starttls()
                    s.login(msg['From'], password)
                    s.sendmail(msg['From'], [msg['To']], msg.as_string())
                    ################################################ EMAL SEND CODE END ##############
                    msg = get_object_or_404(Notification, page_name="Registration", notification_key="Done")
                    msg_data = msg.notification_desc
                    # return JsonResponse({"status": "0", "message": organization_url + " " + msg_data})
                    return JsonResponse({"status": "1", "message": msg_data + " "+user_email+"' !"})



@csrf_exempt
def send_forgate_password_link(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        if User.objects.filter(email=user_email).exists():
            data = User.objects.get(email=user_email)
            user_id = data.id

            user_data = Ar_user.objects.get(user_id=user_id)
            name=user_data.user_name
            # id=str(user_data.pk)

            ###########################
            email_content = '<html> <head> <meta http-equiv="Content-Type" content="text/html; charset=euc-jp"> <meta name="viewport" content="width=device-width"> <meta http-equiv="X-UA-Compatible" content="IE=edge"> <meta name="x-apple-disable-message-reformatting"> <title>Agile | Password Reset</title> <style> html, body {background-color: #fff!important; margin: 0 auto !important; padding: 0 !important; height: 100% !important; width: 100% !important; color:#888!important; } .email-container{max-width: 600px!important; margin: 0 auto!important; } * {-ms-text-size-adjust: 100%; -webkit-text-size-adjust: 100%; } div[style*="margin: 16px 0"] {margin: 0 !important; } table, td {mso-table-lspace: 0pt !important; mso-table-rspace: 0pt !important; } table { width: 100%; border-spacing: 0 !important; border-collapse: collapse !important; table-layout: fixed !important; margin: 0 auto !important; } img {-ms-interpolation-mode:bicubic; } a {text-decoration: none!important; } *[x-apple-data-detectors], .unstyle-auto-detected-links *, .aBn {border-bottom: 0 !important; cursor: default !important; color: inherit !important; text-decoration: none !important; font-size: inherit !important; font-weight: inherit !important; line-height: inherit !important; } @media only screen and (min-device-width: 320px) and (max-device-width: 374px) {u ~ div .email-container {min-width: 320px !important; } } @media only screen and (min-device-width: 375px) and (max-device-width: 413px) {u ~ div .email-container {min-width: 375px !important; } } @media only screen and (min-device-width: 414px) {u ~ div .email-container {min-width: 414px !important; } } </style> </head> <body> <div class="email-container"> <table style="border-bottom: 2px solid #c52241; "> <tr> <td> <h2 style="color:#c52241; padding-top: 62px; margin-bottom: 0px;">Password Reset</h2> </td> <td> <img src="'+ settings.BASE_URL +'agile/assets/img/basic/logo.png" style="width: 60%; float: right;"> </td> </tr> </table> <table style="color: #000;font-size: 20px;"> <tr> <td style="padding: 10px 0px;">Dear '+ name +',</td> </tr> <tr> <td style="padding: 10px 0px;">Seems like you forgot your password for AGILE READY Platform. If it is True, Please click below to reset your password.</td> </tr> <tr> <td style="padding: 10px 0px;text-align:center;"> <button style="padding: 10px 45px;background-color: #c52241;border-radius: 10px;border: none;font-size:20px;color: #fff;"> <a href="'+ settings.BASE_URL +'" style="color: #fff; text-decoration: none;">Reset Password</a></button> </td> </tr> <tr> <td style="padding: 10px 0px;">If you did not forget your password, you can safely ignore this email.</td> </tr> </table> <table style="border-top: 1px solid #000; color: #000; font-size: 20px;"> <tr> <td style="font-weight: bold; padding-top: 30px;">Thank you for Joining!</td> </tr> <tr> <td style="font-weight: bold;padding-bottom: 30px;">The Agile Ready Team</tr> </table> <table style="background-color: #f2f2f2; font-size: 20px;"> <tr> <td style="padding: 35px 30px; text-align: center;">DigiMonk Technologies, Software Technology Parks Of India Gwalior, Madhya Pradesh 474005</td> </tr> </table> </div> </body> </html>'
            msg = email.message.Message()
            msg['Subject'] = 'Forgot Password done'
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

            ############################

        return JsonResponse({"status": "0", "message": 'user_email !'})


@csrf_exempt
def send_varification_link(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        if User.objects.filter(email=user_email).exists():
            if User.objects.filter(email=user_email).filter(is_active = True).exists():
                status = "0"
                message = "Your Account already Activated"
                return JsonResponse({"status": status, "message": message})
            else:
                get_user_instant = User.objects.get(email=user_email)
                uid = urlsafe_base64_encode(force_bytes(get_user_instant.id))
                token = account_activation_token.make_token(get_user_instant)
                user_info = Ar_user.objects.get(user_id=get_user_instant.id)
                varification_link = settings.BASE_URL + "account/activate/" + uid + "/" + token
                ################################################ EMAL SEND CODE START ##############
                logo_image = settings.BASE_URL + 'static/img/basic/logo.png'
                data_content = {"BASE_URL": settings.BASE_URL,"logo_image": logo_image ,"user_name": user_info.user_name, "varification_link": varification_link}
                email_content = render_to_string('email_template/email_send_for_send_varification_link.html', data_content)
                msg = email.message.Message()
                msg['Subject'] = 'Account Varification Link'
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
                status = "1"
                msg = get_object_or_404(Notification, page_name="Sign_Up", notification_key="Send")
                msg_data = msg.notification_desc
                message = msg_data
        else:
            status = "0"
            msg = get_object_or_404(Notification, page_name="Sign_Up", notification_key="Not_Send")
            msg_data = msg.notification_desc
            message = msg_data
        return JsonResponse({"status":status,"message":message})



@csrf_exempt
def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(username=email, password=password)
        status = 0
        if user is not None:
            get_user_info = Ar_user.objects.get(user=user)
            status=get_user_info.status
            if status=="Active":
                print("=======================================") 
                print(get_user_info)
                print(get_user_info.id) 
                print(get_user_info.org_id.id) 
                print(get_user_info.user_name) 
                print(get_user_info.user_type)
                print("=======================================")    
                if get_user_info.org_id.Activate_status:
                    # org_ins = get_object_or_404(AR_organization, id=get_user_info.org_id_id)
                    request.session['user_id'] = get_user_info.id
                    request.session['org_id'] = get_user_info.org_id.id
                    request.session['user_name'] = get_user_info.user_name
                    request.session['user_type'] = get_user_info.user_type
                    auth.login(request, user)
                    status = "1"
                    message = "Login"
                    # return JsonResponse({"status": get_user_info.org_id.id, "message": message})
                else:
                    status = "0"
                    msg = get_object_or_404(Notification, page_name="Login", notification_key="org_account_inactivated")
                    msg_data = msg.notification_desc
                    message = msg_data     
            else:
                status = "0"
                msg = get_object_or_404(Notification, page_name="Login", notification_key="Not_Active_Root")
                msg_data = msg.notification_desc
                message = msg_data
        else:
            status = "0"
            msg = get_object_or_404(Notification, page_name="Login", notification_key="Not_Active")
            msg_data = msg.notification_desc
            message = msg_data
    return JsonResponse({"status":status,"message":message})