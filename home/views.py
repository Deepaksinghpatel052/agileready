from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http import  JsonResponse
from django.conf import settings
from user_story_view import set_user_story_acceptance_criteria_and_conver_algo as ACCA
# from account.forms import User_Form,AR_USER_Form
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from subscription.models import Subscription
from django.core.mail import send_mail
import smtplib
import email.message
import stripe
from helpuser.models import Cms_manage
from subscription.models import Subscription, MembershipHistory, Payment
from datetime import datetime
from .models import StripeAccount
from account.models import AR_organization
# Create your views here.


def handler404(request,exception):
    return render(request, 'web/error_page/page_404.html', {'BASE_URL':settings.BASE_URL})

def handler500(request):
    return render(request, 'web/error_page/page_500.html',  {'BASE_URL':settings.BASE_URL})



def test_data(request):
    return render(request, 'web/payment/stripe.html',  {'BASE_URL':settings.BASE_URL})

def login_page(request):
    return render(request, 'web/home/index.html', {'home_active': "active", 'BASE_URL': settings.BASE_URL,"set_login":"do_login"})


def contact_us(request):
    return render(request, 'web/home/contact_us.html', {'BASE_URL': settings.BASE_URL,"Contact_active":"active"})

def about_us(request):
    return render(request, 'web/home/about_us.html', {'BASE_URL': settings.BASE_URL,"about_active":"active"})

def eula(request):
    return render(request, 'web/home/eula.html', {'BASE_URL': settings.BASE_URL,"EULA_active":"active"})

def privacy(request):
    return render(request, 'web/home/privacy.html', {'BASE_URL': settings.BASE_URL,"Privacy_active":"active"})

def security(request):
    return render(request, 'web/home/security.html', {'BASE_URL': settings.BASE_URL,"Security_active":"active"})


def index(request):
    # 'user_form': User_Form, 'ar_user_form': AR_USER_Form,
    # if 'user_email' in request.session:
    #     return render(request, 'dashboard/dashboard_user/dashboard.html', {"message": "Logged in Successfully"})
                
    return render(request, 'web/home/index.html', {'home_active': "active", 'BASE_URL':settings.BASE_URL})

def whyar(request):
   
    return render(request, 'web/why-agile-ready/index.html', {'whyar_active': "active", 'BASE_URL':settings.BASE_URL})

def view_information(request,keyword):
    contecn = ""
    title = ""
    if Cms_manage.objects.filter(keyword=keyword).exists():
        get_data = Cms_manage.objects.get(keyword=keyword)
        contecn = get_data.help_description
        title = get_data.title

    return render(request, 'web/home/view-information.html', {'home_active': "active", 'BASE_URL':settings.BASE_URL,"contect":contecn,"title":title})


def company(request):

    return render(request, 'web/company/index.html', {'company_active': "active", 'BASE_URL':settings.BASE_URL})



def check_login(request):
    # -----------------Stripe Payment Gateway ---------------
    if 'user_id' in request.session and 'org_id' in request.session and 'user_name' in request.session:
        return HttpResponse("login")
    else:
        return render(request, 'web/subscriptions/index.html', {'subscription_active': "active",'data':data,'login_data':login_data, 'BASE_URL':settings.BASE_URL})

    # -----------------Stripe Payment Gateway code After Payment Process---------------

    return render(request, 'web/company/index.html', {'company_active': "active", 'BASE_URL':settings.BASE_URL})

@csrf_exempt
def do_payments(request):
    data = Subscription.objects.filter(All_member=True)
    url = settings.BASE_URL + "subscription"
    StripeAccount_ins = get_object_or_404(StripeAccount, Payment_Method="Stripe")
    currency = StripeAccount_ins.currency_type
    # -----------------Stripe Payment Gateway ---------------
    
    login_data = ""
    key = StripeAccount_ins.STRIPE_PUBLISHABLE_KEY
    key1 = StripeAccount_ins.STRIPE_SECRET_KEY
    stripe.api_key = key1

    # -----------------Stripe Payment Gateway code After Payment Process---------------
    if request.method == 'POST':
        package_id = request.POST['package_id']
        amount = request.POST['amount']
        token = request.POST['stripeToken']
        description = request.POST['description']

        if amount != "0":
            charge = stripe.Charge.create(
                amount=amount,
                currency=StripeAccount_ins.currency_type,
                description=description,
                source=token,
            )
            return JsonResponse({ "status":charge.status,"package_id":package_id,"trans_id":charge.id}) 
                # if charge.status == "succeeded":
                #     trans_id = charge.id
                #     org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
                #     user_ins = get_object_or_404(Ar_user, id=request.session['user_id'])
                #     done_payment_for_package(org_ins, user_ins, trans_id, currency)

        else:
            trans_id = "Free"
            return JsonResponse({ "mssgae":trans_id})        
                # org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
                # user_ins = get_object_or_404(Ar_user, id=request.session['user_id'])
                # done_payment_for_package(org_ins, user_ins, trans_id, currency)    

def subscription(request,amounte="",packeg_id=""):
    data = Subscription.objects.filter(All_member=True).filter(Active=True)
    url = settings.BASE_URL + "subscription"
    StripeAccount_ins = get_object_or_404(StripeAccount, Payment_Method="Stripe")
    currency = StripeAccount_ins.currency_type
    # -----------------Stripe Payment Gateway ---------------

    login_data = ""
    key = StripeAccount_ins.STRIPE_PUBLISHABLE_KEY
    key1 = StripeAccount_ins.STRIPE_SECRET_KEY
    stripe.api_key = key1

    amounte_get = ""
    packeg_id_get = ""
    get_package = {}
    if amounte != "":
        amounte_get = force_text(urlsafe_base64_decode(amounte))
        amounte_get = int(amounte_get)*100
        packeg_id_get = force_text(urlsafe_base64_decode(packeg_id))
        get_package = get_object_or_404(MembershipHistory,id=packeg_id_get)

    if 'org_id' in request.session :
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        if MembershipHistory.objects.filter(Organization=org_ins).filter(Active=True).exists():
            get_package_info = get_object_or_404(MembershipHistory, Active=True,Organization=org_ins)
        else:
            get_package_info = {}
    else:

        get_package_info = {}
    return render(request, 'web/subscriptions/index.html', {'get_package_info':get_package_info, 'get_package':get_package,'amounte_get':amounte_get,'packeg_id_get':packeg_id_get,'currency' :currency, 'key':key,'url': url,'subscription_active': "active",'login_data':login_data,'data':data, 'BASE_URL':settings.BASE_URL})


def usrating(request):
    get_data = None
    if Cms_manage.objects.filter(keyword="User-Story-Rating").exists():
        get_data = Cms_manage.objects.get(keyword="User-Story-Rating")
    return render(request, 'web/user-story-rating/index.html', {'get_data':get_data,'usrating_active': "active", 'BASE_URL':settings.BASE_URL})




# def dashboard(request):
#     del request.session['user_email']
#     return render(request, 'basic/index.html', {'company_active': "active"})
