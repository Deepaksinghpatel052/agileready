from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from account.models import Ar_user,Notification,AR_organization
from .models import MembershipRequest,Subscription,MembershipHistory,Payment,MailForPaymentStatus
from django.conf import settings
from datetime import datetime,timedelta
from django.template.loader import render_to_string
import email.message
import smtplib
import django
from feedback.models import ArEmailSendToAdmin
# Create your views here.

@csrf_exempt
def check_payment_status_data(request):
    pa_id = request.POST['package_id']
    get_data = get_object_or_404(MembershipHistory,id=pa_id)
    if get_data.Payment_Done:
        set_status = "True"
    else:
        set_status = "False"    
    return JsonResponse({"status":set_status,"message":"Payment is already done for this package."})    

def get_package_limit(org_id,check_for):
    
    Ar_org = get_object_or_404(AR_organization,id=org_id)
    get_package = get_object_or_404(MembershipHistory,Organization=Ar_org,Active=True)
    if check_for == "users":
        test = ""
    return JsonResponse({"status":"True","message":org_id,"check_for":get_package.Invite_user})


@csrf_exempt
def check_user_type(request):
    user_data =get_object_or_404(Ar_user,id=request.session['user_id'])
    if user_data.user_type == "Root":
        type = "Root"
        mssgae = "done"
    else:
        msg = get_object_or_404(Notification, page_name="subscription", notification_key="root_user")
        msg_data = msg.notification_desc
        type = "user"
        mssgae = msg_data
    return JsonResponse({"type": type,"mssgae":mssgae})

@csrf_exempt
def send_request_for_ee(request):
    Ar_user_ins = get_object_or_404(Ar_user,id=request.session['user_id'])
    Ar_org = get_object_or_404(AR_organization,id=request.session['org_id'])
    Request_for = 'Enterprise Edition'
    try:
        MR = MembershipRequest(Request_from=Ar_user_ins,Organization=Ar_org,Request_for=Request_for)
        MR.save()
        msg = get_object_or_404(Notification, page_name="subscription", notification_key="request_send_for_enterprise_edition")
        msg_data = msg.notification_desc
        return JsonResponse({"staus": "done","mssgae":msg_data})
    except:
        msg_data = "Something was wrong please try again after some time."
        return JsonResponse({"staus": "fail", "mssgae": msg_data})

@csrf_exempt
def add_data_in_membership_historty(request):
    pa_id = request.POST['pachage_id']
    package_ins = get_object_or_404(Subscription,id=pa_id)
    Ar_user_ins = get_object_or_404(Ar_user,id=request.session['user_id'])
    Ar_org = get_object_or_404(AR_organization,id=request.session['org_id'])
    MembershipHistory.objects.filter(Organization=Ar_org).update(Active=False)    
    m_his = MembershipHistory(Package_name=package_ins,Organization=Ar_org,Root_user=Ar_user_ins,Price=package_ins.Price,Role_access_and_security=package_ins.Role_access_and_security,Invite_user=package_ins.Invite_user,Team=package_ins.Team,Product=package_ins.Product,Backlog_per_Product=package_ins.Backlog_per_Product,Rating_cycle=package_ins.Rating_cycle,User_story=package_ins.User_story,Job_story=package_ins.Job_story,Test_story=package_ins.Test_story,Time_duration_count=package_ins.Time_duration_count,Time_duration_type=package_ins.Time_duration_type,create_by=Ar_user_ins)
    m_his.save()
    msg = get_object_or_404(Notification, page_name="subscription", notification_key="add_data_in_membership_historty")
    msg_data = msg.notification_desc
    amount = package_ins.Price
    if amount == "":
        amount = 0
    return JsonResponse({"staus": "done", "mssgae":msg_data,"data":{"payment_obj_id":m_his.id,"payment_amount":amount,"payment_for":package_ins.Title}})

@csrf_exempt
def update_payment_status(request):
    payment_id = request.POST['payment_id']
    tranj_id = request.POST['tranj_id']
    Payment_method = request.POST['Payment_method']

    membership_his_obj = get_object_or_404(MembershipHistory,id=payment_id)
    Ar_user_ins = get_object_or_404(Ar_user,id=request.session['user_id'])
    Ar_org = get_object_or_404(AR_organization,id=request.session['org_id'])
    MembershipHistory.objects.filter(Organization=Ar_org).update(Active=False)
    try:
        if membership_his_obj.Payment_Done:
            msg = get_object_or_404(Notification, page_name="subscription", notification_key="payment_status_update_already")
            msg_data = msg.notification_desc
            status = "1"
        else:    
            payment_obj = Payment(payment_for=membership_his_obj,Amount=membership_his_obj.Price,Transaction_id=tranj_id,Organization=Ar_org,Root_user=Ar_user_ins,Payment_method=Payment_method,Payment_Done=True,Currency_type="$")
            payment_obj.save()
            N = membership_his_obj.Time_duration_count
            date_N_days_ago = datetime.today() + timedelta(days=N)
            end_date = date_N_days_ago.strftime('%Y-%m-%d')    
            
            mail_obj = MailForPaymentStatus(payment_for=payment_obj,Organization=Ar_org,Request_from=Ar_user_ins,User_email=Ar_user_ins.user.username)
            mail_obj.save()    

            MembershipHistory.objects.filter(id=payment_id).update(Payment_Done=True,Active=True,Active_date=datetime.now(),end_date=end_date)
            
            add_email = ArEmailSendToAdmin(User_Email=Ar_user_ins.user.username,Email_Subjects="subscription upgraded",Ar_user=Ar_user_ins,ORG_ID=Ar_org,Subscription_Plan=membership_his_obj.Package_name.Title)
            add_email.save()

            msg = get_object_or_404(Notification, page_name="subscription", notification_key="add_data_in_membership_historty")
            msg_data = msg.notification_desc
            status = "1"
    except:
        msg_data = "Something was wrong please try again after some time. Please contact to Agileread Support team."
        status = "0"    
    return JsonResponse({"staus": status, "mssgae":msg_data})


@csrf_exempt
def check_exists_package(request):
    today = datetime.today()
    Ar_org = get_object_or_404(AR_organization,id=request.session['org_id'])
    get_package= MembershipHistory.objects.filter(Active=True).filter(Organization=Ar_org).filter(end_date__gte=today)
    print(get_package)
    print(datetime.now())
    if get_package:
        status = True
        msg = get_object_or_404(Notification, page_name="subscription", notification_key="check_exists_package")
        msg_data = msg.notification_desc
        message = msg_data

    else:
        status = False 
        message = ""  
    return JsonResponse({"status":status,"message":message})

@csrf_exempt
def sent_payment_email(request):
    get_emails = MailForPaymentStatus.objects.filter(send_status=False)
    # items = MailForPaymentStatus.objects.get(id=2)
    if get_emails:
        for items in get_emails:
            data_content = { "BASE_URL": settings.BASE_URL,"user_name":"Admin","logo_image":settings.BASE_URL+"static/img/basic/logo.png","get_data":items}
            email_content = render_to_string('email_template/email_sent_for_package_payment_template.html',data_content)
            user_email = items.User_email
            msg = email.message.Message()
            msg['Subject'] = 'Invoice - AgileReady'
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = user_email
            password = settings.EMAIL_HOST_PASSWORD
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            MailForPaymentStatus.objects.filter(id=items.id).update(send_status=True,send_date=django.utils.timezone.now())
    return HttpResponse("email send")
    # data_content = {"user_name":"Admin","logo_image":settings.BASE_URL+"static/img/basic/logo.png","get_data":items}
    # return render( request,'email_template/email_sent_for_package_payment_template.html',data_content)

    # =======================================================================================================================

@csrf_exempt
def add_data_in_membership_historty_default(request,pachage_id,user_id = "",org_id=""):
    if user_id == "":
        user_id = request.session['user_id']
    if org_id == "":
        org_id  = request.session['org_id']
    pa_id = pachage_id
    package_ins = get_object_or_404(Subscription,id=pa_id)
    Ar_user_ins = get_object_or_404(Ar_user,id=user_id)
    Ar_org = get_object_or_404(AR_organization,id=org_id)
    MembershipHistory.objects.filter(Organization=Ar_org).update(Active=False)    
    m_his = MembershipHistory(Package_name=package_ins,Organization=Ar_org,Root_user=Ar_user_ins,Price=package_ins.Price,Role_access_and_security=package_ins.Role_access_and_security,Invite_user=package_ins.Invite_user,Team=package_ins.Team,Product=package_ins.Product,Backlog_per_Product=package_ins.Backlog_per_Product,Rating_cycle=package_ins.Rating_cycle,User_story=package_ins.User_story,Job_story=package_ins.Job_story,Test_story=package_ins.Test_story,Time_duration_count=package_ins.Time_duration_count,Time_duration_type=package_ins.Time_duration_type,create_by=Ar_user_ins)
    m_his.save()
    msg = get_object_or_404(Notification, page_name="subscription", notification_key="add_data_in_membership_historty")
    msg_data = msg.notification_desc
    amount = package_ins.Price
    if amount == "":
        amount = 0
    return {"staus": "done", "mssgae":msg_data,"data":{"payment_obj_id":m_his.id,"payment_amount":amount,"payment_for":package_ins.Title}}



@csrf_exempt
def update_payment_status_default(request,payment_id,tranj_id,Payment_method,user_id = "",org_id=""):
    payment_id = payment_id
    tranj_id = tranj_id
    Payment_method = Payment_method
    if user_id == "":
        user_id = request.session['user_id']
    if org_id == "":
        org_id  = request.session['org_id']
    membership_his_obj = get_object_or_404(MembershipHistory,id=payment_id)
    Ar_user_ins = get_object_or_404(Ar_user,id=user_id)
    Ar_org = get_object_or_404(AR_organization,id=org_id)
    MembershipHistory.objects.filter(Organization=Ar_org).update(Active=False)
    try:
        if membership_his_obj.Payment_Done:
            msg = get_object_or_404(Notification, page_name="subscription", notification_key="payment_status_update_already")
            msg_data = msg.notification_desc
            status = "1"
        else:    
            payment_obj = Payment(payment_for=membership_his_obj,Amount=membership_his_obj.Price,Transaction_id=tranj_id,Organization=Ar_org,Root_user=Ar_user_ins,Payment_method=Payment_method,Payment_Done=True,Currency_type="$")
            payment_obj.save()
            N = membership_his_obj.Time_duration_count
            date_N_days_ago = datetime.today() + timedelta(days=N)
            end_date = date_N_days_ago.strftime('%Y-%m-%d')    
            
            mail_obj = MailForPaymentStatus(payment_for=payment_obj,Organization=Ar_org,Request_from=Ar_user_ins,User_email=Ar_user_ins.user.username)
            mail_obj.save()    

            MembershipHistory.objects.filter(id=payment_id).update(Payment_Done=True,Active=True,Active_date=datetime.now(),end_date=end_date)
            msg = get_object_or_404(Notification, page_name="subscription", notification_key="add_data_in_membership_historty")
            msg_data = msg.notification_desc
            status = "1"
    except:
        msg_data = "Something was wrong please try again after some time. Please contact to Agileread Support team."
        status = "0"    
    return {"staus": status, "mssgae":msg_data}