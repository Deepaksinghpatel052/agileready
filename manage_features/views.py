from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib import messages
from django.conf import settings
from account.models import AR_organization,Ar_user,Notification
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from .forms import Ar_Featurre_Form
from .models import AR_FEATURE
from datetime import datetime
from user_story_view.models import AR_USER_STORY
from agileproject.serializers import Ar_Epic_Serializer,Ar_Feature_Serializer
from manage_product import views as product_view
from django.db.models import Q
# Create your views here.
@login_required
def index(request):
    if product_view.check_permition(request, 'Manage Features', 0):
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        ar_feature = AR_FEATURE.objects.filter(ORG_ID=org_ins).order_by("-id").filter(~Q(Feature_key = 'None'))
        msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_features/index.html',{'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'date':datetime.now(),'ar_feature':ar_feature,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = Notification.objects.filter(page_name="Authorized").filter(notification_key="Error")
        error_data = msg[0].notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


@login_required
def add_features(request):
    if product_view.check_permition(request, 'Manage Features', 1):
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        epic_data = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).order_by("-id")
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        if request.method == "POST":
            ar_featurre_form = Ar_Featurre_Form(org_info,request.POST)
            if ar_featurre_form.is_valid():
                Feature_key = ar_featurre_form.cleaned_data.get('Feature_key')
                if AR_FEATURE.objects.filter(Feature_key=Feature_key).filter(ORG_ID=request.session['org_id']).exists():
                    msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, Feature_key +" , " + msg_data)
                else:
                    created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
                    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
                    data = ar_featurre_form.save(commit=False)
                    data.ORG_ID = org_ins
                    data.create_by = created_by_ins
                    data.update_by = created_by_ins
                    try:
                        data.save()
                        ar_featurre_form.save_m2m()
                        msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                        return redirect(settings.BASE_URL + "manage-feature")
                    except:
                        messages.error(request, ar_featurre_form.errors)
                    return redirect(settings.BASE_URL+"manage-feature")
            else:
                messages.error(request, ar_featurre_form.errors)
        else:
            ar_featurre_form=Ar_Featurre_Form(org_info)
        return render(request, 'admin/manage_features/add-manageenv-feature.html',{'date':datetime.now(),'epic_data':epic_data,'ar_featurre_form':ar_featurre_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


@login_required
def edit_features(request,id):
    if product_view.check_permition(request, 'Manage Features', 1):
        ar_feature_form =AR_FEATURE.objects.get(id=id)
        feature_id=ar_feature_form.id
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        org_info = AR_organization.objects.filter(id=str(org_ins.id))
        if request.method == "POST":
            ar_feature_form = Ar_Featurre_Form( data=(request.POST or None),org_info=org_info,instance = ar_feature_form)
            if ar_feature_form.is_valid():
                try:
                    ar_feature_form.save()
                    msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                    return redirect(settings.BASE_URL + "manage-feature")
                except:
                    messages.error(request, ar_feature_form.errors)
            else:
                messages.error(request, ar_featurre_form.errors)
            return redirect(settings.BASE_URL + 'manage-feature/edit-feature/' + id + '')
        else:
            ar_feature_form = Ar_Featurre_Form(instance=ar_feature_form,org_info=org_info)
        return render(request, 'admin/manage_features/edit-manageenv-feature.html',{'date':datetime.now(),'feature_id':feature_id,'ar_feature_form':ar_feature_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

@login_required
def delete_features(request,id):
    if product_view.check_permition(request, 'Manage Features', 1):
        try:
            AR_FEATURE.objects.get(id=id).delete()
            msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        except(TypeError):
            msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="Manage Feature", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-feature')

@login_required
def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        print('check_map[0]')
        print(check_map)
        feature_data = AR_FEATURE.objects.filter(CE_ID=check_map)
        feature = Ar_Feature_Serializer(feature_data, many=True)
        return JsonResponse({'check_project': feature.data})
    return JsonResponse({'check_project':"sorry"})