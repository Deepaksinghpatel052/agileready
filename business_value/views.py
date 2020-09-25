from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from .forms import ArBusinessValueForm
from .models import AR_BUSINESS_VALUE
from django.contrib import messages
from datetime import datetime
from account.models import AR_organization,Ar_user,Notification
from manage_product import views as product_view
from django.http import HttpResponse,JsonResponse
from user_story_view.models import AR_USER_STORY
from agileproject.serializers import ArUserStoryViewSerializer
from user_story_view.user_story_score.readiness_quality_score import quelity_score

# Create your views here.
@login_required
def index(request):
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
    bus_value_data = AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_ins)
    role_edit_status = product_view.check_permition(request, 'Manage Roles', 1)
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    ArBusinessValueForm_get = ArBusinessValueForm()
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    get_all_role = AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_ins)
    if request.method == 'POST':
        ArBusinessValueForm_get = ArBusinessValueForm(request.POST)
        if ArBusinessValueForm_get.is_valid():
            business_text_code = ArBusinessValueForm_get.cleaned_data.get('business_text_code')
            if AR_BUSINESS_VALUE.objects.filter(bus_value_txt_code=business_text_code).filter(ORG_ID=org_ins).exists():
                msg = get_object_or_404(Notification, page_name="Manage Business Text Code", notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request, business_text_code +" , " + msg_data)
            else:
                try:
                    ArBusinessValue = ArBusinessValueForm_get.save(commit=False)
                    ArBusinessValue.ORG_ID = org_ins
                    ArBusinessValue.save()
                except(TypeError, OverflowError):
                    messages.error(request, "Something was wrong !")
        else:
            messages.error(request, ArBusinessValueForm_get.errors)
        return redirect(settings.BASE_URL + "business-value")
    msg = get_object_or_404(Notification, page_name="Manage Business Value", notification_key="Not_Remove")
    Not_Remove_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Business Value", notification_key="Remove Request")
    Remove_Request_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Business Value", notification_key="Remove_Success")
    Remove_done_msg = msg.notification_desc
    return render(request, 'admin/manage_business_value/index.html',{'date':datetime.now(),'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'bus_value_data':bus_value_data,'role_edit_status':role_edit_status,'get_all_role':get_all_role,'ArBusinessValueForm_get':ArBusinessValueForm_get,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


@login_required
def edit_business_value(request,id):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    ArBusinessValue_info = get_object_or_404(AR_BUSINESS_VALUE, pk=id)
    Ar_Business_Value = AR_BUSINESS_VALUE.objects.filter(ORG_ID=org_ins)
    business_value_form = AR_BUSINESS_VALUE.objects.get(id=id)
    business_value_id=business_value_form.id
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    if request.method == "POST":
        business_value_form = ArBusinessValueForm( data=(request.POST or None),instance = business_value_form)
        if business_value_form.is_valid():
            business_text_code = business_value_form.cleaned_data.get('business_text_code')
            if AR_BUSINESS_VALUE.objects.filter(bus_value_txt_code=business_text_code).filter(ORG_ID=org_ins).exists():
                msg = get_object_or_404(Notification, page_name="Manage Business Text Code", notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request, business_text_code +" , " + msg_data)
            else:
                try:
                    business_value_form.save()
                    msg = get_object_or_404(Notification, page_name="Manage Business Value", notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                    return redirect(settings.BASE_URL + 'business-value')
                except:
                    messages.error(request,  business_value_form.errors)
        else:
            messages.error(request,  business_value_form.errors)
    else:
        business_value_form = ArBusinessValueForm(instance=business_value_form)
    return render(request, 'admin/manage_business_value/edit.html',{'date':datetime.now(),'role_edit':"value",'Ar_Business_Value':Ar_Business_Value,'business_value_id':business_value_id,'business_value_form':business_value_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})



@login_required
def remove_business_value(request,id):
    try:
        business_value = get_object_or_404(AR_BUSINESS_VALUE, pk=id)
        business_value.delete()
        msg = get_object_or_404(Notification, page_name="Manage Business Value", notification_key="Remove")
        msg_data = msg.notification_desc
        messages.info(request, msg_data)
    except(TypeError):
        msg = get_object_or_404(Notification, page_name="Manage Business Value", notification_key="Remove_error")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'business-value')
