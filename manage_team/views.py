from django.shortcuts import render,get_object_or_404,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from agileproject import settings
from account.models import Ar_user,AR_organization
from .forms import ManageTeamForm
from manage_product.models import AR_team
from django.contrib import messages
import django
from datetime import datetime
from django.db import IntegrityError
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@login_required
def index(request):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    if AR_team.objects.filter(ORG_id=org_ins).exists():
        AR_team_get = AR_team.objects.filter(ORG_id=org_ins).order_by("-id")
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
                team.save()
                TeamForm.save_m2m()
                messages.info(request, "Team added successfully!")
            except IntegrityError:
                messages.error(request, "The team name is alread exists!")
            return redirect(settings.BASE_URL+"manage-team")
    TeamForm = ManageTeamForm(request.user, request.session['org_id'],user_objects)
    return render(request, 'admin/manage_team/index.html', {'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL,'TeamForm':TeamForm,'team_get':AR_team_get})

@login_required
def remove_team(request,id):
    team = get_object_or_404(AR_team, pk=id)
    team.delete()
    messages.info(request, "Team removed successfully!")
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
            messages.info(request, "Team updated successfully!")
        else:
            messages.error(request, product_form.error)
        return redirect(settings.BASE_URL + "manage-team")
    else:

        TeamForm = ManageTeamForm(request.user, request.session['org_id'],user_objects,instance=TeamForm_info)
    return render(request, 'admin/manage_team/edit.html',{"TeamForm":TeamForm,"ids":id,'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL})