from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.conf import settings
from account.models import AR_organization,Ar_user,Notification
from manage_product.models import AR_product
from .models import AR_EPIC_CAPABILITY
from django.db import IntegrityError
from .forms import Ar_Epic_Capability_Form
from manage_features.models import AR_FEATURE
from django.contrib import messages
from datetime import datetime
from manage_product import views as product_view
from django.db.models import Q

# Create your views here.
@login_required
def get_capanility(request,id):
    if AR_product.objects.filter(id=id).exists():
        get_object =  get_object_or_404(AR_product, pk=id)
        get_data = AR_EPIC_CAPABILITY.objects.filter(PROJECT_ID=get_object)
    else:
        get_data = "false"
    return HttpResponse(get_data)

@login_required
def index(request):
    if product_view.check_permition(request, 'Manage Epic Capability', 0):
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        ar_epic_capability = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).order_by("-id").filter(~Q(Cepic_key = 'None'))
        msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_epic_capability/index.html',{'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'date':datetime.now(),'user_name':request.session['user_name'],'ar_epic_capability':ar_epic_capability,'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized",notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

@login_required
def add_epic_capabilities(request):
    if product_view.check_permition(request, 'Manage Epic Capability', 1):
        ar_feature = AR_FEATURE.objects.all()
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        if request.method == "POST":
            ar_epic_capability_form = Ar_Epic_Capability_Form(data=(request.POST or None),org_info=org_info)
            if ar_epic_capability_form.is_valid():
                Cepic_key = ar_epic_capability_form.cleaned_data.get('Cepic_key')
                if AR_EPIC_CAPABILITY.objects.filter(Cepic_key=Cepic_key).filter(ORG_ID=request.session['org_id']).exists():
                    msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request,Cepic_key+" , " + msg_data)
                else:
                    created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
                    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
                    data = ar_epic_capability_form.save(commit=False)
                    data.created_by=created_by_ins
                    data.update_by = created_by_ins
                    data.ORG_ID=org_ins
                    try:
                        data.save()
                        ar_epic_capability_form.save_m2m()
                        msg = get_object_or_404(Notification, page_name="Manage Epic Capability",
                                                notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                        return redirect(settings.BASE_URL + 'manage-epic-capabilities')
                    except:
                        messages.error(request, ar_epic_capability_form.errors)
            else:
                messages.error(request, ar_epic_capability_form.errors)
            return redirect(settings.BASE_URL+'manage-epic-capabilities')
        else:
            ar_epic_capability_form=Ar_Epic_Capability_Form(org_info)
        return render(request, 'admin/manage_epic_capability/add-manageenv-capabilities.html',{'date':datetime.now(),'user_name':request.session['user_name'],'ar_feature':ar_feature,'ar_epic_capability_form':ar_epic_capability_form,'BASE_URL': settings.BASE_URL})
    else:
        msg = Notification.objects.filter(page_name="Authorized").filter(notification_key="Error")
        error_data = msg[0].notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

@login_required
def edit_epic_capabilities(request,id):
    if product_view.check_permition(request, 'Manage Epic Capability', 1):
        ar_feature = AR_FEATURE.objects.filter(CE_ID=id)
        ar_epic_capability_form = AR_EPIC_CAPABILITY.objects.get(id=id)
        epic_id=ar_epic_capability_form.id
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        if request.method == "POST":
            ar_epic_capability_form = Ar_Epic_Capability_Form( data=(request.POST or None),org_info=org_info,instance = ar_epic_capability_form)
            if ar_epic_capability_form.is_valid():
                data = ar_epic_capability_form.save(commit=False)
                created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
                data.update_by = created_by_ins
                data.update_dt = datetime.now()
                try:
                    data.save()
                    ar_epic_capability_form.save_m2m()
                    msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                    return redirect(settings.BASE_URL + 'manage-epic-capabilities')
                except:
                    msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                    return redirect(settings.BASE_URL + 'manage-epic-capabilities')
            else:
                messages.error(request, ar_epic_capability_form.errors)
        else:
            ar_epic_capability_form = Ar_Epic_Capability_Form(instance=ar_epic_capability_form,org_info=org_info)
        return render(request, 'admin/manage_epic_capability/edit-manageenv-capabilities.html',{'date':datetime.now(),'user_name':request.session['user_name'],'ar_feature':ar_feature,'epic_id':epic_id,'ar_epic_capability_form':ar_epic_capability_form,'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

@login_required
def delete_epic_capabilities(request,id):
    if product_view.check_permition(request, 'Manage Epic Capability', 1):
        try:
            AR_EPIC_CAPABILITY.objects.get(pk=id).delete()
            msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        except(TypeError):
            msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="Manage Epic Capability", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-epic-capabilities')