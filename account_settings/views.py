from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login
from agileproject import settings
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User,auth
from account.models import Ar_user,ArUserProfile,AR_organization,Notification
from django.contrib import messages
import hashlib
import django
from datetime import datetime
from django.db.models import Subquery

from manage_product.models import AR_team
from manage_iterations.models import ArIterations
from user_story_points.models import ArUserStoryPoints
from manage_role.models import ArRole
from manage_goals.models import ArManageGoals
from manage_benefits.models import ArManageBenefits
from manage_features.models import AR_FEATURE
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from user_story_view.models import AR_USER_STORY
from manage_backlogs.models import AR_BACKLOG
from manage_product.models import AR_product


from account.views import set_default_value_for_org,set_dummy_data
# Create your views here.


@login_required
def set_default_data(request):
    org_id = request.session['org_id']
    user_id = request.session['user_id']
    set_data_type = "default"
    # return HttpResponse(org_id)
    remove_all_data(org_id, user_id)

    set_default_value_for_org(org_id,user_id)

    set_dummy_data(request,org_id,user_id,set_data_type,"Dommy Data")
    # return HttpResponse(org_id)
    msg = Notification.objects.filter(page_name="Account Settings").filter(notification_key="data_reset_done")
    msg_data = msg[0].notification_desc
    messages.info(request, msg_data)
    return redirect(settings.BASE_URL + 'account-settings')
    # return HttpResponse("sjhdcbh")

def remove_all_data(org_id,user_id):
    org_ins  = get_object_or_404(AR_organization,id=org_id)
    error_message = ""
    # ############################### ArIterations all Teams start #############
    if ArIterations.objects.filter(ORG_ID=org_ins).exists():
        try:
            ArIterations.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_message += ",,Error For Iterations"
    # ############################### ArIterations all Teams END #############
    # ############################### ArUserStoryPoints all Teams start #############
    if ArUserStoryPoints.objects.filter(ORG_ID=org_ins).exists():
        try:
            ArUserStoryPoints.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For ArUserStoryPoints"
    # ############################### ArUserStoryPoints all Teams END #############
    # ############################### ArRole all Teams start #############
    if ArRole.objects.filter(ORG_ID=org_ins).exists():
        try:
            ArRole.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For ArRole"
    # ############################### ArRole all Teams END #############
    # ############################### ArManageGoals all Teams start #############
    if ArManageGoals.objects.filter(ORG_ID=org_ins).exists():
        try:
            ArManageGoals.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For ArManageGoals"
    # ############################### ArManageGoals all Teams END #############
    # ############################### ArManageBenefits all Teams start #############
    if ArManageBenefits.objects.filter(ORG_ID=org_ins).exists():
        try:
            ArManageBenefits.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For ArManageBenefits"
    # ############################### ArManageBenefits all Teams END #############
    # ############################### AR_FEATURE all Teams start #############
    if AR_FEATURE.objects.filter(ORG_ID=org_ins).exists():
        try:
            AR_FEATURE.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For AR_FEATURE"
    # ############################### AR_FEATURE all Teams END #############
    # ############################### AR_EPIC_CAPABILITY all Teams start #############
    if AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).exists():
        try:
            AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For AR_EPIC_CAPABILITY"
    # ############################### AR_EPIC_CAPABILITY all Teams END #############
    # ############################### AR_USER_STORY all Teams start #############
    if AR_USER_STORY.objects.filter(ORG_id=org_ins).exists():
        try:
            AR_USER_STORY.objects.filter(ORG_id=org_ins).delete()
        except:
            error_messahe = ",,Error For AR_USER_STORY"
    # ############################### AR_USER_STORY all Teams END #############

    # ############################### AR_BACKLOG all Teams start #############
    if AR_BACKLOG.objects.filter(ORG_ID=org_ins).exists():
        try:
            AR_BACKLOG.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For AR_BACKLOG"
    # ############################### AR_BACKLOG all Teams END #############

    # ############################### AR_product all Teams start #############
    if AR_product.objects.filter(ORG_ID=org_ins).exists():
        try:
            AR_product.objects.filter(ORG_ID=org_ins).delete()
        except:
            error_messahe = ",,Error For AR_product"
    # ############################### AR_product all Teams END #############

    # ############################### AR_team all Teams start #############
    if AR_team.objects.filter(ORG_id=org_ins).exists():
        try:
            AR_team.objects.filter(ORG_id=org_ins).delete()
        except:
            error_messahe = ",,Error For AR_team"
    # ############################### AR_team all Teams END #############

    # ############################### remove all user start #############

    ar_users = Ar_user.objects.filter(org_id=org_ins)
    try:
        for user_data_one in ar_users:
            if user_data_one.user_type != 'Root':
                id = user_data_one.id
                print(user_data_one.id)
                print(user_data_one)
                print("----")
                user_val = Ar_user.objects.get(pk=id)
                user_id = user_val.user_id
                Ar_user.objects.get(pk=id).delete()
                user = User.objects.filter(id=user_id)
                user.delete()
    except:
        error_messahe = ",,Error For Ar_user"
    # # ############################### remove all user END #############

    return True

@login_required
def index(request):
    if request.user.is_authenticated:
        user = Ar_user.objects.filter(id=request.session['user_id'])
        profile = ArUserProfile.objects.filter(ORG_ID=request.session['org_id'])
        get_count_of_invit_user = Ar_user.objects.filter(created_by=request.session['user_id']).count()
        get_active_user = User.objects.filter(is_active=True)
        get_count_of_active_user = Ar_user.objects.filter(created_by=request.session['user_id']).filter(
            user_id__in=Subquery(get_active_user.values("id"))).count()
        if request.method == "POST":
            user_name = request.POST["user_name"]
            city = request.POST["city"]
            state = request.POST["state"]
            zip = request.POST["zip"]
            country = request.POST["country"]
            phone = request.POST["phone"]
            if zip == "":
                zip=0
            if Ar_user.objects.filter(id=request.session['user_id']).exists():
                Ar_user.objects.filter(id=request.session['user_id']).update(user_name=user_name, city=city,state=state,zip=zip,country=country,
                                                            phone=phone)
                msg = Notification.objects.filter(page_name="Account Settings").filter(notification_key="Done")
                msg_data = msg[0].notification_desc
                messages.info(request, msg_data)
                # messages.info(request, "Profile updated successfully !")
                del request.session['user_name']
                request.session['user_name'] = user_name
                return redirect(settings.BASE_URL + 'account-settings')
            else:
                msg = Notification.objects.filter(page_name="Account Settings").filter(notification_key="Not Done")
                msg_data = msg[0].notification_desc
                messages.error(request, msg_data)
                # messages.info(request, "Profile not updated !")
        return render(request,"admin/account_settings/index.html",{'date':datetime.now(),'get_count_of_active_user':get_count_of_active_user,'get_count_of_invit_user':get_count_of_invit_user,'profile':profile,'user':user,"BASE_URL":settings.BASE_URL,'user_name':request.session['user_name']})
    else:
        return redirect(settings.BASE_URL)


@login_required
def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        data = Ar_user.objects.filter(id=request.session['user_id'])

        username = data[0].user_id
        data = User.objects.filter(id=username)
        username = data[0].username
        user = auth.authenticate(username=username,password=check_map)
        if user is not None:
            check_map=0
        else:
            check_map=1
        return JsonResponse({'check_project': check_map})
    return JsonResponse({'check_project':"sorry"})


@login_required
def pass_change(request):
    if request.method == "POST":
        newpwd = request.POST['newpwd']
        # print(newpwd)
        data = Ar_user.objects.filter(id=request.session['user_id'])

        username = data[0].user_id
        data = User.objects.get(id=username)
        username = data.username
        # user = auth.authenticate(username=username,password=check_map)
        #
        #
        # data = User.objects.get(id=request.session['user_id'])
        # username = data.username
        # print(username)
        # print(newpwd)
        data.set_password(newpwd)
        data.save()
        del request.session['user_id']
        del request.session['org_id']
        del request.session['user_name']
        auth.logout(request)
        user = auth.authenticate(username=username, password=newpwd)
        if user is not None:
            get_user_info = Ar_user.objects.get(user=user)
            request.session['user_id'] = get_user_info.id
            request.session['org_id'] = get_user_info.org_id.id
            request.session['user_name'] = get_user_info.user_name
            auth.login(request, user)
        check_map=1
        return JsonResponse({'check_project': check_map})
    return JsonResponse({'check_project':"sorry"})

