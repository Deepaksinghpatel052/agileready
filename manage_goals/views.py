from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import ArManageGoalsForm
from .models import ArManageGoals
from account.models import AR_organization,Ar_user,Notification
from django.contrib import messages
from django.db.models import Q
from manage_product import views as product_view
from django.http import HttpResponse,JsonResponse
from user_story_view.models import AR_USER_STORY
from datetime import datetime
from agileproject.serializers import ArUserStoryViewSerializer
from user_story_view.user_story_score.readiness_quality_score import quelity_score
# Create your views here.


@login_required
def index(request):
    if product_view.check_permition(request, 'Manage Goals', 0):
        goal_edit_status = product_view.check_permition(request, 'Manage Goals', 1)
        ArManageGoalsForm_get = ArManageGoalsForm()
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        get_all_goal = ArManageGoals.objects.filter(ORG_ID=org_ins)
        if request.method == 'POST':
            ArManageGoalsForm_get = ArManageGoalsForm(request.POST)
            if ArManageGoalsForm_get.is_valid():
                Goal_title = ArManageGoalsForm_get.cleaned_data.get('Goal_title')
                use = ArManageGoalsForm_get.cleaned_data.get('Use_in')
                if use != "":
                    data = use.split(" , ")
                else:
                    data = 0
                if ArManageGoals.objects.filter(Goal_title=Goal_title).filter(ORG_ID=org_ins).exists():
                    msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, Goal_title +" , " + msg_data)
                else:
                    try:
                        ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                        ManageGoals = ArManageGoalsForm_get.save(commit=False)
                        ManageGoals.ORG_ID = org_ins
                        ManageGoals.created_by = ar_user_insta
                        ManageGoals.updated_by = ar_user_insta
                        ManageGoals.save()
                        create_goal_id = "AR_GOAL_"+str(ManageGoals.id)
                        ArManageGoals.objects.filter(id=ManageGoals.id).update(Goal_id=create_goal_id)
                        # ###########-----------------------------------------
                        if data != 0:
                            for val in data:
                                story_data = AR_USER_STORY.objects.filter(title=str(val))
                                for data in story_data:
                                    STP = data.story_tri_part_text
                                    data = quelity_score(STP)
                                AR_USER_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
                        # ###########-----------------------------------------

                        msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                    except(TypeError, OverflowError):
                        messages.error(request, "Something was wrong !")
            else:
                messages.info(request, ArManageGoalsForm_get.errors)
            return redirect(settings.BASE_URL + "manage-goals")
        msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_goals/index.html',{'date':datetime.now(),'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'goal_edit_status':goal_edit_status,'get_all_goal':get_all_goal,'ArManageGoalsForm_get':ArManageGoalsForm_get,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

@login_required
def edit(request,id):
    ArManageGoals_info = get_object_or_404(ArManageGoals, pk=id)

    use_old = ArManageGoals_info.Use_in
    if use_old != "":
        data_old = use_old.split(" , ")
    else:
        data_old = 0
    ArManageGoalsForm_get = ArManageGoalsForm(instance=ArManageGoals_info)
    
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    if request.method == 'POST':
        ArManageGoalsForm_get = ArManageGoalsForm(request.POST,instance=ArManageGoals_info)
        if ArManageGoalsForm_get.is_valid():
            Goal_title = ArManageGoalsForm_get.cleaned_data.get('Goal_title')
            use = ArManageGoalsForm_get.cleaned_data.get('Use_in')
            if use != "":
                data = use.split(" , ")
            else:
                data = 0
            if ArManageGoals.objects.filter(Goal_title=Goal_title).filter(ORG_ID=org_ins).filter(~Q(id=id)).exists():
                msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request, Goal_title +" , " + msg_data)
            else:
                try:
                    ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                    ManageGoals = ArManageGoalsForm_get.save(commit=False)
                    ManageGoals.updated_by = ar_user_insta
                    ManageGoals.save()
                    # ###########-----------------------------------------
                    if data_old != 0:
                        for val_old in data_old:
                            # return HttpResponse(val_old)
                            story_data = AR_USER_STORY.objects.filter(title=str(val_old))
                            STP = story_data[0].story_tri_part_text
                            title = story_data[0].title
                            data_val = quelity_score(STP)
                            # return HttpResponse(data_val)
                            AR_USER_STORY.objects.filter(title=title).update(readiness_quality_score=data_val[0])
                    # ###########-----------------------------------------
                    # ###########-----------------------------------------
                    if data != 0:
                        for val in data:
                            # return HttpResponse(val)
                            story_data = AR_USER_STORY.objects.filter(title=str(val))
                            STP = story_data[0].story_tri_part_text
                            title = story_data[0].title
                            data_get = quelity_score(STP)
                            # return HttpResponse(data_get)
                            AR_USER_STORY.objects.filter(title=title).update(readiness_quality_score=data_get[0])
                    # ###########-----------------------------------------

                    msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Add")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                except(TypeError, OverflowError):
                    messages.error(request, "Something was wrong !")
        else:
            messages.info(request, ArManageGoalsForm_get.errors)
        return redirect(settings.BASE_URL + "manage-goals")
    return render(request,'admin/manage_goals/edit.html',{'date':datetime.now(),'ArManageGoalsForm_get':ArManageGoalsForm_get,'id':id})


@login_required
def remove_goal(request,id):
    if product_view.check_permition(request, 'Manage Goals', 1):
        try:
            managegoals = get_object_or_404(ArManageGoals, pk=id)
            use = managegoals.Use_in
            if use != "":
                data = use.split(" , ")
            else:
                data = 0
            managegoals.delete()
            # ###########-----------------------------------------
            if data != 0:
                for val in data:
                    story_data = AR_USER_STORY.objects.filter(title=str(val))
                    for data in story_data:
                        STP = data.story_tri_part_text
                        data = quelity_score(STP)
                    AR_USER_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
            # ###########-----------------------------------------
            msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        except(TypeError):
            msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        return redirect(settings.BASE_URL + 'manage-goals')
    else:
        msg = get_object_or_404(Notification, page_name="Manage Goal", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
        return redirect(settings.BASE_URL + 'manage-goals')


def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        print(check_map)
        if check_map == "" :
            gole_val=0
        else:
            result = AR_USER_STORY.objects.filter(story_tri_part_text__icontains=check_map)
            gole_data = ArUserStoryViewSerializer(result, many=True)
            gole_val=gole_data.data
        return JsonResponse({'check_project': gole_val})