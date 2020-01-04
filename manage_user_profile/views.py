from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.contrib import messages
from account.models import AR_organization,Ar_user
from .forms import ArUserProfileForm
from .models import ArUserProfile,ArUserProfilePermission
from agileproject.serializers import ArUserProfilePermissionSerializer

# Create your views here.
def index(request):
    ##################################################################333333333333
    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
    ar_user_profile_form = ArUserProfileForm()
    ar_user_data = ArUserProfile.objects.filter(ORG_ID=org_ins)
    if request.method == "POST":
        list = request.POST.get("list")
        if list is not None:
            #############################################3
            list_ins = get_object_or_404(ArUserProfile, profile_key=list)
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
            activity = request.POST.getlist('activity[]')
            if ArUserProfilePermission.objects.filter(profile_key=list_ins).exists():
                messages.info(request, "Profile update successfully !")
            else:
                messages.info(request, "Profile added successfully !")
            for activityvalue in activity:
                value = activityvalue.lower()
                valueacti = value.replace(" ", "")
                editor = request.POST.get(valueacti+"edit")
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
                    ArUserProfilePermission.objects.filter(profile_key=list_ins).filter(activites=activityvalue).update(update_by=created_by_ins,
                                                           activites=activityvalue, editor=editoracti,
                                                           viewer=vieweracti)
                else:
                    activitydata = ArUserProfilePermission(profile_key=list_ins, ORG_ID=org_ins, create_by=created_by_ins, update_by=created_by_ins,
                                                        activites=activityvalue,editor=editoracti,viewer=vieweracti)
                    activitydata.save()
        else:
            messages.info(request, "Please select a Profile Key !")



    #     # data = ar_backlog_form.save(commit=False)
    #     # data.created_by = created_by_ins
    #     # data.updated_by = created_by_ins
    #     # data.ORG_ID = org_ins
    #     #############################################3
    #     superuseredit = request.POST.get("superuseredit")
    #     superuserview = request.POST.get("superuserview")
    #
    #     # completed = request.POST.get('completed', '') == 'on'
    #     print('superuserview')
    #     print(superuserview)
    #     print('superuseredit')
    #     print(superuseredit)
    #     # activity=request.POST["activity"]
    #
    #     activity = request.POST.getlist('activity[]')
    #
    #     for activ in activity:
    #         # print(lower(activ))
    #         # activate_name = activ
    #         value = activ.lower()
    #         valuea = value.replace(" ", "")
    #         print(request.POST.get(valuea+"edit"))
    #         print(request.POST.get(valuea+"view"))
    #
    #         # user = User.objects.create_user(username=user_email, email=user_email, password=password, is_active=False)
    #         # user.save()
    #
    #     # print("request.POST[activity[]]")
    #     # print(request.POST["activity[]"])
    #     # print(activity)
    #     # print(superuserview)
    #
    # ######################################
    ##################################################################333333333333
    return render(request, 'admin/manage_user_profile/index.html',{'ar_user_data':ar_user_data,'ar_user_profile_form':ar_user_profile_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


# def add_profile(request):
#     ##################################################################333333333333
#     # org_info = AR_organization.objects.filter(id=request.session['org_id'])
#     # print(request.session['org_id'])
#     # print(org_ins)
#     org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
#     ar_user_profile_form = ArUserProfileForm()
#     ar_user_data = ArUserProfile.objects.filter(ORG_ID=org_ins)
#
#     ######################################
#     ##################################################################333333333333
#     return render(request, 'admin/manage_user_profile/profile.html',{'ar_user_data':ar_user_data,'ar_user_profile_form':ar_user_profile_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


def add_profile(request):
    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
    ar_user_profile_form = ArUserProfileForm()
    ar_user_data = ArUserProfile.objects.filter(ORG_ID=org_ins)
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    #####################################
    if request.method == "POST":
        ar_user_profile_form = ArUserProfileForm(request.POST)
        if ar_user_profile_form.is_valid():
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
            data = ar_user_profile_form.save(commit=False)
            data.create_by=created_by_ins
            data.update_by = created_by_ins
            data.ORG_ID=org_ins
            try:
                data.save()
                messages.info(request, "User profile added successfully !")
            except:
                messages.error(request, ar_user_profile_form.errors)
        else:
            messages.error(request, ar_user_profile_form.errors)
    else:
        ar_backlog_form=ArUserProfileForm(org_info)
    return render(request, 'admin/manage_user_profile/profile.html',{'ar_user_data':ar_user_data,'ar_user_profile_form':ar_user_profile_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})



def edit_user_profile(request,id):
    ##################################################################333333333333
    org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
    ar_user_data = ArUserProfile.objects.filter(ORG_ID=org_ins)
    ar_user_profile = ArUserProfile.objects.filter(ORG_ID=request.session['org_id'])
    #######################################
    ar_user_profile_form = ArUserProfile.objects.get(id=id)
    user_profile_id=ar_user_profile_form.id
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    if request.method == "POST":
        ar_user_profile_form = ArUserProfileForm( data=(request.POST or None),instance = ar_user_profile_form)
        if ar_user_profile_form.is_valid():
            try:
                ar_user_profile_form.save()
                messages.info(request, "User profile updated successfully !")
                return redirect(settings.BASE_URL + 'user-profile/add-profile')
            except:
                messages.error(request, ar_user_profile_form.errors)
        else:
            messages.error(request, ar_user_profile_form.errors)
    else:
        ar_user_profile_form = ArUserProfileForm(instance=ar_user_profile_form)
    #######################################
    return render(request, 'admin/manage_user_profile/profile.html',{'ar_user_data':ar_user_data,'ar_user_profile_form':ar_user_profile_form,'ar_user_profile':ar_user_profile,'user_profile_id':user_profile_id,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


def delete_user_profile(request,id):
    ArUserProfile.objects.get(id=id).delete()
    messages.info(request, "User profile removed !")
    return redirect(settings.BASE_URL + 'user-profile/add-profile')


def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        print('check_map[0]')
        print(check_map)
        data = ArUserProfile.objects.get(profile_key=check_map)
        val = data.id
        data = ArUserProfilePermission.objects.filter(profile_key=val)
        print(data)
        profiledata = ArUserProfilePermissionSerializer(data, many=True)
        return JsonResponse({'check_project': profiledata.data})
    return JsonResponse({'check_project':"sorry"})
