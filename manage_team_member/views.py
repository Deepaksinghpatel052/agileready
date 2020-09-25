from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.http import JsonResponse, HttpResponse
from django.conf import settings
from account.models import Ar_user,AR_organization,ArUserProfile,Notification
from .forms import ManageTeamMemberForm
from manage_product.models import AR_team
from datetime import datetime
from manage_product import views as product_view

# Create your views here.
@login_required
def index(request):
    if product_view.check_permition(request, 'Manage Team Members', 0):
        check_edit_permition = product_view.check_permition(request, 'Manage Team Members', 1)
        user1 = Ar_user.objects.filter(org_id=request.session['org_id']).order_by("user_name")
        get_current_user = Ar_user.objects.get(id=request.session['user_id'])
        msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_teams_members/index.html',{"user_id":request.session['user_id'],'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'check_edit_permition':check_edit_permition,'date':datetime.now(),'user':user1,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL,"get_current_user":get_current_user})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


def update_root_user(request,id):
    if Ar_user.objects.filter(id=id).exists():
        Ar_user.objects.filter(id=request.session['user_id']).update(user_type="User")
        Ar_user.objects.filter(id=id).update(user_type="Root")
        msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="change_root_user")
        msg_data = msg.notification_desc
        messages.info(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-team-member')

@login_required
def edit_team_member(request,id):
    user = Ar_user.objects.get(id=id)
    profile = ArUserProfile.objects.filter(ORG_ID=request.session['org_id'])
    member_form = Ar_user.objects.get(id=id)
    member_id=member_form.id
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    if request.method == "POST":
        user_name = request.POST["user_name"]
        city = request.POST["city"]
        state = request.POST["state"]
        zip = request.POST["zip"]
        country = request.POST["country"]
        phone = request.POST["phone"]
        status=request.POST["status"]
        if zip == "":
            zip = 0
        if Ar_user.objects.filter(id=id).exists():
            Ar_user.objects.filter(id=id).update(user_name=user_name, city=city,state=state,zip=zip,country=country, phone=phone,status=status)
            msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="Update")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        member_form = ManageTeamMemberForm(data=(request.POST or None), org_info=org_info, instance=member_form)
        if member_form.is_valid():
            try:
                team = member_form.save(commit=False)
                ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                team.update_by = ar_user_insta
                team.update_dt = datetime.now()
                member_form.save_m2m()
                return redirect(settings.BASE_URL + 'manage-team-member')
            except:
                messages.error(request,  member_form.errors)
        else:
            messages.error(request,  member_form.errors)
    else:
        member_form = ManageTeamMemberForm(instance=member_form,org_info=org_info)
    return render(request, 'admin/manage_teams_members/edit.html',{'profile':profile,'user':user,'date':datetime.now(),'member_edit':"value",'member_id':member_id,'member_edit_form':member_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


@login_required
def delete_team_member(request,id):
    if product_view.check_permition(request, 'Manage Team Members', 1):
        try:
            user_val = Ar_user.objects.get(pk=id)
            user_id = user_val.user_id
            Ar_user.objects.get(pk=id).delete()
            user = User.objects.filter(id=user_id)
            user.delete()
            msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        except(TypeError):
            msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="Manage Team Members", notification_key="Permission")
        msg_data = msg[0].notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-team-member')