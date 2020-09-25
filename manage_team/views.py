from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from agileproject import settings
from account.models import Ar_user,AR_organization,Notification
from .forms import ManageTeamForm
from manage_product.models import AR_team
from django.contrib import messages
import django
from datetime import datetime
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
from manage_product import views as product_view
from django.db.models import Q
from dashboard.views import get_package_limit
# Create your views here.

@login_required
def index(request):
    if product_view.check_permition(request, 'Manage Teams', 0):
        check_edit_permission = product_view.check_permition(request, 'Manage Teams', 1)
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        if AR_team.objects.filter(ORG_id=org_ins).exists():
            AR_team_get = AR_team.objects.filter(ORG_id=org_ins).order_by("-id").filter(~Q(Team_name = 'None'))
        else:
            AR_team_get = {}
        user_objects = []
        for team in AR_team_get:
            for ids in team.Team_member_list.all():
                user_objects.append(ids.id)
        if request.method == 'POST':
            TeamForm = ManageTeamForm(request.user, request.session['org_id'],user_objects,request.POST)
            if TeamForm.is_valid():
                org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
                ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                team = TeamForm.save(commit=False)
                team.create_by =  ar_user_insta
                team.update_by =  ar_user_insta
                team.ORG_id =  org_ins
                try:
                    get_status = get_package_limit(request.session['org_id'],"Teams")
                    if get_status:
                        team.save()
                        TeamForm.save_m2m()
                        msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                    else:
                        msg = get_object_or_404(Notification, page_name="package_limit_excid", notification_key="package_limit_excid")
                        msg_data = msg.notification_desc
                        messages.error(request, msg_data)     
                except IntegrityError:
                    msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, msg_data)
                return redirect(settings.BASE_URL+"manage-team")
        TeamForm = ManageTeamForm(request.user, request.session['org_id'],user_objects)
        msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_team/index.html', {'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'check_edit_permission':check_edit_permission,'date':datetime.now(),'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL,'TeamForm':TeamForm,'team_get':AR_team_get})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


@login_required
def remove_team(request,id):
    try:
        team = get_object_or_404(AR_team, pk=id)
        team.delete()
        msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Remove")
        msg_data = msg.notification_desc
        messages.info(request, msg_data)
    except(TypeError):
        msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Remove_error")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-team')

@login_required
@csrf_exempt
def edit_team(request,id):
    TeamForm_info = get_object_or_404(AR_team, pk=id)
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    if AR_team.objects.filter(ORG_id=org_ins).exists():
        AR_team_get = AR_team.objects.filter(ORG_id=org_ins).order_by("-id")
    else:
        AR_team_get = {}
    user_objects = []
    for team in AR_team_get:
        if team.id == id:
            test ="test"
        else:
            for ids in team.Team_member_list.all():
                user_objects.append(ids.id)
    if request.method == 'POST':
        TeamForm = ManageTeamForm(request.user, request.session['org_id'],user_objects, request.POST,instance = TeamForm_info)
        if TeamForm.is_valid():
            team = TeamForm.save(commit=False)
            ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
            team.update_by =  ar_user_insta
            team.update_dt =  datetime.now()
            team.save()
            TeamForm.save_m2m()
            msg = get_object_or_404(Notification, page_name="Manage Team", notification_key="Update")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
            return redirect(settings.BASE_URL + "manage-team")
        else:
            messages.error(request, product_form.error)
        return redirect(settings.BASE_URL + "manage-team")
    else:

        TeamForm = ManageTeamForm(request.user, request.session['org_id'],user_objects,instance=TeamForm_info)
    return render(request, 'admin/manage_team/edit.html',{'date':datetime.now(),"TeamForm":TeamForm,"ids":id,'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL})