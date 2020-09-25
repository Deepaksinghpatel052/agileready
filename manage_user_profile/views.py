from django.contrib.auth import login
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib import messages
from account.models import AR_organization,Ar_user,ArUserProfile,ArUserProfilePermission,Notification
from .forms import ArUserProfileForm
from agileproject.serializers import ArUserProfilePermissionSerializer

# Create your views here.
def index(request):
    get_current_user = Ar_user.objects.get(id=request.session['user_id'])
    if get_current_user.user_type == "Root":
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        ar_user_profile_form = ArUserProfileForm()
        ar_user_data = ArUserProfile.objects.filter(ORG_ID=org_ins)
        if request.method == "POST":
            list = request.POST.get("list")
            if list is not None:
                list_ins = get_object_or_404(ArUserProfile, profile_key=list,ORG_ID=org_ins)
                username = get_current_user.user.id
                created_by_ins = get_object_or_404(User, pk=username)
                org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
                activity = request.POST.getlist('activity[]')
                if ArUserProfilePermission.objects.filter(profile_key=list_ins).exists():
                    msg = get_object_or_404(Notification, page_name="Manage User Profile Permissions",
                                            notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                else:
                    msg = get_object_or_404(Notification, page_name="Manage User Profile Permissions",
                                            notification_key="Add")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                for activityvalue in activity:
                    value = activityvalue.lower()
                    valueacti = value.replace(" ", "")
                    editor = request.POST.get(valueacti + "edit")
                    if editor == "on" :
                        editoracti= True
                    else:
                        editoracti=False
                    viewer = request.POST.get(valueacti + "view")
                    if viewer == "on":
                        vieweracti = True
                    else:
                        vieweracti = False
                    if ArUserProfilePermission.objects.filter(profile_key=list_ins).filter(activites=activityvalue).exists():
                        ArUserProfilePermission.objects.filter(profile_key=list_ins).filter(activites=activityvalue).update(update_dt=datetime.now(),update_by=created_by_ins,
                                                               activites=activityvalue, editor=editoracti,
                                                               viewer=vieweracti)
                    else:
                        activitydata = ArUserProfilePermission(profile_key=list_ins, ORG_ID=org_ins, create_by=created_by_ins, update_by=created_by_ins,
                                                            activites=activityvalue,editor=editoracti,viewer=vieweracti)
                        activitydata.save()
                return redirect(settings.BASE_URL + 'user-profile')
            else:
                messages.info(request, "Please select a Profile Key !")
        msg = get_object_or_404(Notification, page_name="Manage User Profile", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage User Profile",   notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage User Profile",
                                notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_user_profile/index.html',{'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'ar_user_data':ar_user_data,'ar_user_profile_form':ar_user_profile_form,'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


def add_profile(request):
    if request.session['user_type'] == "Root":
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        ar_user_profile_form = ArUserProfileForm()
        ar_user_data = ArUserProfile.objects.filter(ORG_ID=org_ins)
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        if request.method == "POST":
            ar_user_profile_form = ArUserProfileForm(request.POST)
            if ar_user_profile_form.is_valid():
                profile_key  = ar_user_profile_form.cleaned_data.get('profile_key')
                if ArUserProfile.objects.filter(profile_key=profile_key).filter(ORG_ID=request.session['org_id']).exists():
                    msg = get_object_or_404(Notification, page_name="Manage User Profile",
                                            notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request,profile_key +" , " + msg_data)
                else:
                    data = Ar_user.objects.filter(id=request.session['user_id'])
                    username = data[0].user_id
                    created_by_ins = get_object_or_404(User, pk=username)
                    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
                    data = ar_user_profile_form.save(commit=False)
                    data.create_by=created_by_ins
                    data.update_by = created_by_ins
                    data.ORG_ID=org_ins
                    try:
                        data.save()
                        msg = get_object_or_404(Notification, page_name="Manage User Profile",
                                                notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                        return redirect(settings.BASE_URL + 'user-profile/add-profile')
                    except:
                        messages.error(request, ar_user_profile_form.errors)
            else:
                messages.error(request, ar_user_profile_form.errors)
        return render(request, 'admin/manage_user_profile/profile.html',{'ar_user_data':ar_user_data,'ar_user_profile_form':ar_user_profile_form,'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

def edit_user_profile(request,id):
    if request.session['user_type'] == "Root":
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        ar_user_data = ArUserProfile.objects.filter(ORG_ID=org_ins)
        ar_user_profile = ArUserProfile.objects.filter(ORG_ID=request.session['org_id'])
        ar_user_profile_form = ArUserProfile.objects.get(id=id)
        user_profile_id=ar_user_profile_form.id
        if request.method == "POST":
            ar_user_profile_form = ArUserProfileForm( data=(request.POST or None),instance = ar_user_profile_form)
            if ar_user_profile_form.is_valid():
                try:
                    ar_user_profile_form.save()
                    msg = get_object_or_404(Notification, page_name="Manage User Profile",
                                            notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                    return redirect(settings.BASE_URL + 'user-profile/add-profile')
                except:
                    messages.error(request, ar_user_profile_form.errors)
            else:
                messages.error(request, ar_user_profile_form.errors)
        else:
            ar_user_profile_form = ArUserProfileForm(instance=ar_user_profile_form)
        return render(request, 'admin/manage_user_profile/edit_profile.html',{'backlog_edit':"value",'ar_user_data':ar_user_data,'ar_user_profile_form':ar_user_profile_form,'ar_user_profile':ar_user_profile,'date':datetime.now(),'user_profile_id':user_profile_id,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

def delete_user_profile(request,id):
    if request.session['user_type'] == "Root":
        try:
            ArUserProfile.objects.get(pk=id).delete()
            msg = get_object_or_404(Notification, page_name="Manage User Profile", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
            return redirect(settings.BASE_URL + 'user-profile')
        except(TypeError):
            msg = get_object_or_404(Notification, page_name="Manage User Profile", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="Manage User Profile", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'user-profile/add-profile')

def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        data = ArUserProfile.objects.get(profile_key=check_map,ORG_ID=org_ins)
        val = data.id
        data = ArUserProfilePermission.objects.filter(profile_key=val)
        profiledata = ArUserProfilePermissionSerializer(data, many=True)
        return JsonResponse({'check_project': profiledata.data})
    return JsonResponse({'check_project':"sorry"})
