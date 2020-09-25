from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from account.models import Ar_user,ArAccountRemoveRequest
from .models import ArFeedback, ArSendFeedbackEmail,ArEmailSendToAdmin,ArAcadenyEmailForRecavedEmail
from datetime import datetime
from django.contrib import messages
from manage_backlogs.models import AR_BACKLOG
from manage_backlogs.forms import Ar_Backlog_Form
from account.models import AR_organization,Notification
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from datetime import datetime
from django.template.loader import render_to_string
import email.message
import smtplib
import django
# Create your views here.
def sent_feedback_email(request):
    get_data = ArSendFeedbackEmail.objects.filter(status=False)
    if get_data:
        data_content = {"user_name":"Admin","logo_image":settings.BASE_URL+"static/img/basic/logo.png","get_data":get_data,"BASE_URL": settings.BASE_URL}
        email_content = render_to_string('email_template/email_sent_for_feedback_template.html', data_content)
        user_email = "feedback@agileready.net"
        msg = email.message.Message()
        msg['Subject'] = 'beagileready Feedback'
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = user_email
        password = settings.EMAIL_HOST_PASSWORD
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)
        s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        get_data.update(status=True,sent_date=django.utils.timezone.now())
    # =================================================================================
    get_data_2 = ArAccountRemoveRequest.objects.filter(Mail_send_status=False)
    if get_data_2:
        yourname ="Admin"
        logo_image = settings.BASE_URL + 'static/img/basic/logo.png'
        data_content = {"BASE_URL": settings.BASE_URL, "user_name":yourname, "logo_image":logo_image, "get_data":get_data_2}
        email_content = render_to_string("email_template/email_send_account_remove_request.html",data_content)
        user_email = "CustomerCare@agileready.net"
        msg = email.message.Message()
        msg['Subject'] = 'beagileready Account Remove Request'
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = user_email
        password = settings.EMAIL_HOST_PASSWORD
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)
        s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        get_data_2.update(Mail_send_status=True)
    return HttpResponse("True")

def function_feedback_sent(feedback_page, entry_user,created_by_ins):
    default = 'Test'
    entry_feedback_sent = ArSendFeedbackEmail(page_name=feedback_page, feedback_id=entry_user, user_id=created_by_ins)
    entry_feedback_sent.save()

    return True



def sent_report_email(request):
    set_send_mail_statue = False
    get_new_root_user = None
    if ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='New Root Account').exists():     
        get_new_root_user =  ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='New Root Account')
        set_send_mail_statue = True
    get_root_user_active = None
    if ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='Root Account Activated').exists():     
        get_root_user_active =  ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='Root Account Activated')
        set_send_mail_statue = True
    get_invite_new_user = None
    if ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='Invite New User').exists():     
        get_invite_new_user =  ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='Invite New User')
        set_send_mail_statue = True
    get_invite_active_user = None
    if ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='Invite User Activated').exists():     
        get_invite_active_user =  ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='Invite User Activated')
        set_send_mail_statue = True
    get_upgrate_memvership = None
    if ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='subscription upgraded').exists():     
        get_upgrate_memvership =  ArEmailSendToAdmin.objects.filter(Mail_send=False).filter(Email_Subjects='subscription upgraded')
        set_send_mail_statue = True
    yourname ="Admin"
    logo_image = settings.BASE_URL + 'static/img/basic/logo.png'
    data_content = {"BASE_URL": settings.BASE_URL, "user_name":yourname, "logo_image":logo_image,'get_new_root_user':get_new_root_user,
        "get_root_user_active":get_root_user_active,'get_invite_new_user':get_invite_new_user,'get_invite_active_user':get_invite_active_user,'get_upgrate_memvership':get_upgrate_memvership}
    email_content = render_to_string('email_template/email_send_report_for_admin.html',data_content)
    
    if set_send_mail_statue:
        if ArAcadenyEmailForRecavedEmail.objects.filter(Status=True).exists():
            get_academy_email = ArAcadenyEmailForRecavedEmail.objects.filter(Status=True)
            for item in get_academy_email:
                user_email = item.Email
                msg = email.message.Message()
                msg['Subject'] = 'beagileready Report'
                msg['From'] = settings.EMAIL_HOST_USER
                msg['To'] = user_email
                password = settings.EMAIL_HOST_PASSWORD
                msg.add_header('Content-Type', 'text/html')
                msg.set_payload(email_content)
                s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
                s.starttls()
                s.login(msg['From'], password)
                s.sendmail(msg['From'], [msg['To']], msg.as_string())
    if get_new_root_user:
        get_new_root_user.update(Mail_send=True,Mail_send_date=datetime.now())
    if get_root_user_active:
        get_root_user_active.update(Mail_send=True,Mail_send_date=datetime.now())
    if get_invite_new_user:
        get_invite_new_user.update(Mail_send=True,Mail_send_date=datetime.now())
    if get_invite_active_user:
        get_invite_active_user.update(Mail_send=True,Mail_send_date=datetime.now())
    if get_upgrate_memvership:
        get_upgrate_memvership.update(Mail_send=True,Mail_send_date=datetime.now())                
    return  HttpResponse("test")  

@login_required
def index(request):
    print("enter")
    if request.method == "POST":
        feed_nature = request.POST.get('feed_nature')
        feedback_page = request.POST.get('feedback_page')
        feedinformation = request.POST['feedinformation']
        feedback_file = request.FILES.get('feedback_file', False)
        created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
        today = datetime.now()
        val = today.strftime("%d_%m_%Y_%H_%M_%S_%f")
        if feedback_file is not False:
            filename = feedback_file.name
            splitedfilename = filename.split(".")
            length_of_filename = len(splitedfilename)
            file_extention = splitedfilename[length_of_filename - 1]
            upload_file_name = str(val) + "." + file_extention
            fs = FileSystemStorage()
            fs.save(upload_file_name, feedback_file)
        else:
            upload_file_name = ""
        entry_user = ArFeedback(page_name=feedback_page, feedback_nature=feed_nature, feedback_information=feedinformation,
                                attachments=upload_file_name,created_by=created_by_ins)
        entry_user.save()

        # ___________________________________ feedback store for send mail ___________________________________

        data_res = function_feedback_sent(feedback_page, entry_user,created_by_ins)

        # ____________________________________________________________________________________________________
        msg = Notification.objects.filter(page_name="Feedback").filter(notification_key="Send")
        msg_data = msg[0].notification_desc
        messages.info(request, msg_data)
        if feedback_page =="Manage Products":
            return redirect(settings.BASE_URL+'manage-products')
        elif feedback_page =="Manage Feature":
            return redirect(settings.BASE_URL + 'manage-feature')
        elif feedback_page =="Manage Epic Capabilities":
            return redirect(settings.BASE_URL + 'manage-epic-capabilities')
        elif feedback_page =="Manage Team":
            return redirect(settings.BASE_URL + 'manage-team')
        elif feedback_page =="Manage Backlog":
            return redirect(settings.BASE_URL + 'manage-backlog')
        elif feedback_page =="Manage Team Member":
            return redirect(settings.BASE_URL + 'manage-team-member')
        elif feedback_page =="Manage User Story Point":
            return redirect(settings.BASE_URL + 'user-story-points')
        elif feedback_page =="Invite User":
            return redirect(settings.BASE_URL + 'invite-user')
        elif feedback_page =="User Profile":
            return redirect(settings.BASE_URL + 'user-profile')
        elif feedback_page =="Dashboard":
            return redirect(settings.BASE_URL + 'dashboard')
        elif feedback_page =="User Story View":
            return redirect(settings.BASE_URL + 'user-story-view')
        elif feedback_page =="Product View":
            return redirect(settings.BASE_URL + 'products-view')
        elif feedback_page == "Backlog View":
            return redirect(settings.BASE_URL + 'backlog-view')
        elif feedback_page == "Iteration View":
            return redirect(settings.BASE_URL + 'iteration-view')
        elif feedback_page == "Manage Iteration":
            return redirect(settings.BASE_URL + 'manage-iteration')
        elif feedback_page == "Manage Roles":
            return redirect(settings.BASE_URL + 'manage-role')
        elif feedback_page == "Manage Goal":
            return redirect(settings.BASE_URL + 'manage-goals')
        elif feedback_page == "Manage Benefits":
            return redirect(settings.BASE_URL + 'manage-benefits')
        elif feedback_page == "Manage Story Point":
            return redirect(settings.BASE_URL + 'story-points')
        elif feedback_page == "Account Settings":
            return redirect(settings.BASE_URL + 'account-settings')
    #     ------------------------------------------------------------------------------------

        elif feedback_page == "Manage Job Situation Set":
            return redirect(settings.BASE_URL + 'manage-jobsit-set')

        elif feedback_page == "Manage Scenario":
            return redirect(settings.BASE_URL + 'manage-scenario')

        elif feedback_page == "Manage Job Motivation Set":
            return redirect(settings.BASE_URL + 'manage-jobmot-set')

        elif feedback_page == "Manage Job Outcome Set":
            return redirect(settings.BASE_URL + 'manage-joboutc-set')

        elif feedback_page == "Manage Test Action Set":
            return redirect(settings.BASE_URL + 'manage-testact-set')

        elif feedback_page == "Manage Test Condition Set":
            return redirect(settings.BASE_URL + 'manage-testcond-set')

        elif feedback_page == "Manage Test Outcome Set":
            return redirect(settings.BASE_URL + 'manage-testoutc-set')

        elif feedback_page == "Manage Business Value":
            return redirect(settings.BASE_URL + 'business-value')
        elif feedback_page == "Job Story View":
            return redirect(settings.BASE_URL + 'job-story-view')
        elif feedback_page == "BDD TDD Story View":
            return redirect(settings.BASE_URL + 'bdd-tdd-story-view')

        elif feedback_page == "Words and Patterns":
            return redirect(settings.BASE_URL + 'words-patterns')
        elif feedback_page == "User Story Value":
            return redirect(settings.BASE_URL + 'user-story-value')
        elif feedback_page == "Feature Value":
            return redirect(settings.BASE_URL + 'feature-value')


    #     ------------------------------------------------------------------------------------

    return render(request, 'admin/backlog_view/index.html',{'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
