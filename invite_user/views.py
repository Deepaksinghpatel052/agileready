from django.contrib.auth import login
from django.shortcuts import render , HttpResponse ,redirect,get_object_or_404
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
            user_emails  = user_email.split(";")
            for email_get in user_emails:
                user_email = email_get
                if User.objects.filter(email=user_email).exists():
                    messages.error(request, "Email already exists '"+user_email+"' !")
                else:
                    corrent_user_info = Ar_user.objects.get(user_id=request.user.id)
                    org_info = get_object_or_404(AR_organization, pk=request.session['org_id'])
                    password = ''.join([random.choice(string.digits + string.ascii_letters) for i in range(0, 10)])
                    user = User.objects.create_user(username=user_email, email=user_email, password=password,is_active=False)
                    user.save()
                    get_user_info = User.objects.get(username=user_email)
                    state = "state"
                    number = "0"
                    zip_code = "0"
                    ar_users = Ar_user(user_id=user.id,user_name="",state=state,zip=zip_code,phone=number,org_id=org_info,user_type="User",created_by=corrent_user_info.user_id,updated_by=corrent_user_info.user_id)
                    ar_users.save()
                    #########################################################################
                    uid = urlsafe_base64_encode(force_bytes(get_user_info.id))
                    token = account_activation_token.make_token(get_user_info)
                    varification_link = settings.BASE_URL + "account/activate/" + uid + "/" + token
                    logo_image = 'http://203.190.153.20/agile/assets/img/basic/logo.png'
                    email_content = ''

                    logo_image = settings.BASE_URL + 'static/img/basic/logo.png'
                    data_content = {"BASE_URL": settings.BASE_URL, "user_name": corrent_user_info.user_name, "organization_name": org_info.organization_name,"user_email": user_email,"password":password, "logo_image": logo_image,"varification_link": varification_link}
                    email_content = render_to_string('email_template/email_send_for_invite_user.html',data_content)
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
                    messages.info(request, "Invitation link has been sent '"+user_email+"' !")
            redirect(settings.BASE_URL+"invite-user")
        return render(request,"admin/invite_user/index.html",{'user_name':request.session['user_name'],"BASE_URL":settings.BASE_URL})
    else:
        return redirect(settings.BASE_URL)
