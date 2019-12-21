from django.contrib.auth import login
from django.shortcuts import render , HttpResponse ,redirect
from django.http import HttpResponse, JsonResponse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
from account.models import Ar_user,AR_organization,AR_organization_status
from django.db.models import Q,Subquery,Count
import string
import random
import smtplib
from agileproject import settings
from agileproject.tokens import account_activation_token
from django.contrib.auth.decorators import login_required
import email.message
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            user_email = request.POST["email"]
            if User.objects.filter(email=user_email).exists():
                messages.error(request, "Email already exists.")
            else:
                corrent_user_info = Ar_user.objects.get(user_id=request.user.id)
                org_info = AR_organization.objects.get(created_by=request.user.id)
                password = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])
                user = User.objects.create_user(username=user_email, email=user_email, password=password,is_active=False)
                user.save()
                get_user_info = User.objects.get(username=user_email)
                state = "state"
                number = "0"
                zip_code = "0"
                ar_users = Ar_user(user_id=user.id,user_name="",state=state,zip=zip_code,phone=number,org_id=org_info.id,user_type="User",created_by=str(corrent_user_info.user_id),updated_by=str(corrent_user_info.user_id))
                ar_users.save()
                #########################################################################
                uid = urlsafe_base64_encode(force_bytes(get_user_info.id))
                token = account_activation_token.make_token(get_user_info)
                varification_link = settings.BASE_URL + "account/activate/" + uid + "/" + token
                logo_image = 'http://203.190.153.20/agile/assets/img/basic/logo.png'
                email_content = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=euc-jp"><meta name="viewport" content="width=device-width"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="x-apple-disable-message-reformatting"><title>Agile | New Registration</title><style>html,body{background-color:#fff!important;margin:0 auto !important;padding:0 !important;height:100% !important;width:100% !important;color:#888!important}.email-container{max-width:600px!important;margin:0 auto!important}*{-ms-text-size-adjust:100%;-webkit-text-size-adjust:100%}div[style*="margin: 16px 0"]{margin:0 !important}table,td{mso-table-lspace:0pt !important;mso-table-rspace:0pt !important}table{width:100%;border-spacing:0 !important;border-collapse:collapse !important;table-layout:fixed !important;margin:0 auto !important}img{-ms-interpolation-mode:bicubic}a{text-decoration:none!important}*[x-apple-data-detectors], .unstyle-auto-detected-links *,.aBn{border-bottom:0 !important;cursor:default !important;color:inherit !important;text-decoration:none !important;font-size:inherit !important;font-weight:inherit !important;line-height:inherit !important}@media only screen and (min-device-width: 320px) and (max-device-width: 374px){u ~ div .email-container{min-width:320px !important}}@media only screen and (min-device-width: 375px) and (max-device-width: 413px){u ~ div .email-container{min-width:375px !important}}@media only screen and (min-device-width: 414px){u ~ div .email-container{min-width:414px !important}}</style></head><body><div class="email-container"><table style="border-bottom: 2px solid #c52241; "><tr><td><h2 style="color:#c52241; padding-top: 62px; margin-bottom: 0px;">Activate Account</h2></td><td> <img src="'+logo_image+'" style="width: 60%; float: right;"></td></tr></table><table style="color: #000;font-size: 20px;"><tr><td style="padding: 10px 0px;">Welcome to the next generation of being Agile Ready.</td></tr><tr><td style="padding: 10px 0px;">You are invited by <b>"'+corrent_user_info.user_name+' from ('+org_info.organization_name+')"</b> to join their teams using Agile Ready.</td></tr><tr><td style="padding: 10px 0px;">To activate your account, press the button below.</td></tr><tr><td style="padding: 10px 0px;text-align:center;"> <button style="padding: 10px 45px;background-color: #c52241;border-radius: 10px;border: none;font-size:20px;color: #fff;"> <a href="'+varification_link+'" style="color: #fff; text-decoration: none;">Activate</a></button></td></tr><tr> <td style="padding: 10px 0px;">After activation, please log in to your account using your email address <b>"['+user_email+']"</b> and your password <b>"['+password+']".</b> We recommend you to change your password after first login.</td></tr></table><table style="border-top: 1px solid #000; color: #000; font-size: 20px;"><tr><td><h4>MANAGE Your New Account</h4></td></tr><tr><td><a href="'+settings.BASE_URL+'">Change your password</a></td></tr><tr><td><a href="'+settings.BASE_URL+'"> Get Help with your account </a></td></tr><tr><td style="font-weight: bold; padding-top: 30px;">Thank you for Joining!</td></tr><tr><td style="font-weight: bold;padding-bottom: 30px;">The Agile Ready Team</tr></table><table style="background-color: #f2f2f2; font-size: 20px;"><tr><td style="padding: 35px 30px; text-align: center;">DigiMonk Technologies, Software Technology Parks Of India Gwalior, Madhya Pradesh 474005</td></tr></table></div></body></html>'
                msg = email.message.Message()
                msg['Subject'] = 'Invitation Link From Agil'
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
                #########################################################################
                messages.info(request, "Invitation link has been sent.")
            redirect(settings.BASE_URL+"invite-user")
        return render(request,"admin/invite_user/index.html",{'user_name':request.session['user_name'],"BASE_URL":settings.BASE_URL})
    else:
        return redirect(settings.BASE_URL)
