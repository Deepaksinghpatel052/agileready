from django.contrib.auth import login
from django.shortcuts import render , HttpResponse
from django.http import HttpResponse, JsonResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
from .models import Ar_user,AR_organization,AR_organization_status
from django.db.models import Q,Subquery,Count
import string
import random
import smtplib
from agileproject import settings
from agileproject.tokens import account_activation_token
import email.message
# Create your views here.




def account_activate(request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        get_user_info = Ar_user.objects.get(user=user)
        org_id_set = get_user_info.org_id
        if org_id_set == "0":
            org_id = AR_organization.objects.get(created_by=user)
            org_id_set = org_id.id
        request.session['user_id'] = get_user_info.id
        request.session['org_id'] = org_id_set
        request.session['user_name'] = get_user_info.user_name
        login(request,user)
        message = '0'
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
            return JsonResponse({"status":"0","message":"E-mail is already exists"})
        else:
            if Ar_user.objects.filter(phone=number).exists():
                return JsonResponse({"status": "0", "message": "Phone no. is already exists"})
            else:
                if AR_organization.objects.filter(organization_url=organization_url).filter(~Q(organization_url="")).exists():
                    return JsonResponse({"status": "0", "message": "Organization URL is already exists"})
                else:
                    org_id = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])
                    while AR_organization.objects.filter(org_id=org_id).exists():
                        org_id = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])


                    user = User.objects.create_user(username=user_email, email=user_email,password=password,is_active=False)
                    user.save()
                    get_user_instant = User.objects.get(email=user_email)
                    Ar_users = Ar_user(user_id=user.id,user_name=yourname,country=country, city=city,state=state,zip=zip_code,phone=number)
                    Ar_users.save()
                    # if AR_organization_status.objects.filter(status_key="Active").exists():
                    #     ar_org_status = AR_organization_status.objects.get(status_key="Active")
                    # else:
                    #     ar_org_status = AR_organization_status.objects.none()
                    ar_org= AR_organization(org_id=org_id,organization_name=organization,organization_url=organization_url,created_by=user,update_by=user)
                    ar_org.save()
                    # get_user_instant = User.objects.get(email='mohit@gmail.com')
                    uid = urlsafe_base64_encode(force_bytes(get_user_instant.id))
                    token = account_activation_token.make_token(get_user_instant)
                    varification_link = settings.BASE_URL + "account/activate/" + uid + "/" + token
                    ################################################ EMAL SEND CODE START ##############
                    logo_image = 'http://203.190.153.20/agile/assets/img/basic/logo.png'
                    email_content = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=euc-jp"><meta name="viewport" content="width=device-width"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="x-apple-disable-message-reformatting"><title>Agile | New Registration</title><style>html,body{background-color:#fff!important;margin:0 auto !important;padding:0 !important;height:100% !important;width:100% !important;color:#888!important}.email-container{max-width:600px!important;margin:0 auto!important}*{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}div[style*="margin: 16px 0"]{margin:0 !important}table,td{mso-table-lspace:0pt !important;mso-table-rspace:0pt !important}table{width:100%;border-spacing:0 !important;border-collapse:collapse !important;table-layout:fixed !important;margin:0 auto !important}img{-ms-interpolation-mode:bicubic}a{text-decoration:none!important}*[x-apple-data-detectors], .unstyle-auto-detected-links *,.aBn{border-bottom:0 !important;cursor:default !important;color:inherit !important;text-decoration:none !important;font-size:inherit !important;font-weight:inherit !important;line-height:inherit !important}@media only screen and (min-device-width: 320px) and (max-device-width: 374px){u ~ div .email-container{min-width:320px !important}}@media only screen and (min-device-width: 375px) and (max-device-width: 413px){u ~ div .email-container{min-width:375px !important}}@media only screen and (min-device-width: 414px){u ~ div .email-container{min-width:414px !important}}</style></head><body><div class="email-container"><table style="border-bottom: 2px solid #c52241; "><tr><td><h2 style="color:#c52241; padding-top: 62px; margin-bottom: 0px;">WELCOME</h2></td><td> <img src="'+logo_image+'" style="width: 60%; float: right;"></td></tr></table><table style="color: #000;font-size: 20px;"><tr><td style="padding: 10px 0px;">Dear '+yourname+',</td></tr><tr><td style="padding: 10px 0px;">Welcome to the next generation of being Agile Ready.Your new Agile Ready account has been created.</td></tr><tr><td style="padding: 10px 0px;">To activate your account, press the button below.</td></tr><tr><td style="padding: 10px 0px;text-align:center;"> <button style="padding: 10px 45px;background-color: #c52241;border-radius: 10px;border: none;font-size:20px;color: #fff;"> <a href="'+varification_link+'" style="color: #fff; text-decoration: none;">Activate</a></button></td></tr><tr><td style="padding: 10px 0px;">After activation, please log in to your account using your email address "'+user_email+'" and your password "'+password+'".</td></tr></table><table style="border-top: 1px solid #000; color: #000; font-size: 20px;"><tr><td><h4>MANAGE Your New Account</h4></td></tr><tr><td><a href="'+settings.BASE_URL+'">Change your password</a></td></tr><tr><td><a href="'+settings.BASE_URL+'"> Get Help with your account </a></td></tr><tr><td style="font-weight: bold; padding-top: 30px;">Thank you for Joining!</td></tr><tr><td style="font-weight: bold;padding-bottom: 30px;">The Agile Ready Team</tr></table><table style="background-color: #f2f2f2; font-size: 20px;"><tr><td style="padding: 35px 30px; text-align: center;">DigiMonk Technologies, Software Technology Parks Of India Gwalior, Madhya Pradesh 474005</td></tr></table></div></body></html>'
                    msg = email.message.Message()
                    msg['Subject'] = 'Account Create successfully'
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
                    ################################################ EMAL SEND CODE END ##############

                    return JsonResponse({"status": "1", "message": "Registration is done successfully verification link is sent to your email."})



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
            msg['Subject'] = 'Forgot Password'
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

        return JsonResponse({"status": "0", "message": 'user_email'})


@csrf_exempt
def send_varification_link(request):
    if request.method == "POST":
        user_email = request.POST["email"]
        if User.objects.filter(email=user_email).exists():
            get_user_instant = User.objects.get(email=user_email)
            uid = urlsafe_base64_encode(force_bytes(get_user_instant.id))
            token = account_activation_token.make_token(get_user_instant)
            user_info = Ar_user.objects.get(user_id=get_user_instant.id)
            varification_link = settings.BASE_URL + "account/activate/" + uid + "/" + token
            ################################################ EMAL SEND CODE START ##############
            logo_image = 'http://203.190.153.20/agile/assets/img/basic/logo.png'
            email_content = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=euc-jp"><meta name="viewport" content="width=device-width"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="x-apple-disable-message-reformatting"><title>Agile | New Registration</title><style>html,body{background-color:#fff!important;margin:0 auto !important;padding:0 !important;height:100% !important;width:100% !important;color:#888!important}.email-container{max-width:600px!important;margin:0 auto!important}*{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}div[style*="margin: 16px 0"]{margin:0 !important}table,td{mso-table-lspace:0pt !important;mso-table-rspace:0pt !important}table{width:100%;border-spacing:0 !important;border-collapse:collapse !important;table-layout:fixed !important;margin:0 auto !important}img{-ms-interpolation-mode:bicubic}a{text-decoration:none!important}*[x-apple-data-detectors], .unstyle-auto-detected-links *,.aBn{border-bottom:0 !important;cursor:default !important;color:inherit !important;text-decoration:none !important;font-size:inherit !important;font-weight:inherit !important;line-height:inherit !important}@media only screen and (min-device-width: 320px) and (max-device-width: 374px){u ~ div .email-container{min-width:320px !important}}@media only screen and (min-device-width: 375px) and (max-device-width: 413px){u ~ div .email-container{min-width:375px !important}}@media only screen and (min-device-width: 414px){u ~ div .email-container{min-width:414px !important}}</style></head><body><div class="email-container"><table style="border-bottom: 2px solid #c52241; "><tr><td><h2 style="color:#c52241; padding-top: 62px; margin-bottom: 0px;">Activate Account</h2></td><td> <img src="'+logo_image+'" style="width: 60%; float: right;"></td></tr></table><table style="color: #000;font-size: 20px;"><tr><td style="padding: 10px 0px;">Dear '+user_info.user_name+',</td></tr><tr><td style="padding: 10px 0px;">Welcome to the next generation of Agile Ready.</td></tr><tr><td style="padding: 10px 0px;">To activate your account, press the button below.</td></tr><tr><td style="padding: 10px 0px;text-align:center;"> <button style="padding: 10px 45px;background-color: #c52241;border-radius: 10px;border: none;font-size:20px;color: #fff;"> <a href="'+varification_link+'" style="color: #fff; text-decoration: none;">Activate</a></button></td></tr></table><table style="border-top: 1px solid #000; color: #000; font-size: 20px;"><tr><td><h4>MANAGE Your New Account</h4></td></tr><tr><td><a href="'+settings.BASE_URL+'">Change your password</a></td></tr><tr><td><a href="'+settings.BASE_URL+'"> Get Help with your account </a></td></tr><tr><td style="font-weight: bold; padding-top: 30px;">Thank you for Joining!</td></tr><tr><td style="font-weight: bold;padding-bottom: 30px;">The Agile Ready Team</tr></table><table style="background-color: #f2f2f2; font-size: 20px;"><tr><td style="padding: 35px 30px; text-align: center;">DigiMonk Technologies, Software Technology Parks Of India Gwalior, Madhya Pradesh 474005</td></tr></table></div></body></html>'
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
            message = "Link is send to your email id."
        else:
            status = "0"
            message = "Email is not registered."
        return JsonResponse({"status":status,"message":message})



@csrf_exempt
def login_user(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = auth.authenticate(username=email, password=password)
        if user is not None:
            get_user_info = Ar_user.objects.get(user=user)
            org_id_set = get_user_info.org_id
            if org_id_set == "0":
                org_id = AR_organization.objects.get(created_by=user)
                org_id_set = org_id.id
            request.session['user_id'] = get_user_info.id
            request.session['org_id'] = org_id_set
            request.session['user_name'] = get_user_info.user_name
            auth.login(request, user)
            status = "1"
            message = "Login"
        else:
            status = "0"
            message = "Username and password is incorrect & maybe your account is not activate click <b style='color:#03a9f4' data-toggle='modal'  data-target='#varification_ling'>here</b> to get varification link."
    return JsonResponse({"status":status,"message":message})