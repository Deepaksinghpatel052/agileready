from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from .forms import ArRoleForm
from .models import ArRole
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
    if product_view.check_permition(request, 'Manage Roles', 0):
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
        role_data = ArRole.objects.filter(ORG_ID=org_ins)
        role_edit_status = product_view.check_permition(request, 'Manage Roles', 1)
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        ArManageRolesForm_get = ArRoleForm()
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        get_all_role = ArRole.objects.filter(ORG_ID=org_ins)
        if request.method == 'POST':
            ArManageRolesForm_get = ArRoleForm(request.POST)
            if ArManageRolesForm_get.is_valid():
                title = ArManageRolesForm_get.cleaned_data.get('title')
                use = ArManageRolesForm_get.cleaned_data.get('use')
                if use != "":
                    data = use.split(" , ")
                else:
                    data = 0
                if ArRole.objects.filter(title=title).filter(ORG_ID=org_ins).exists():
                    msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, title +" , " + msg_data)
                else:
                    try:
                        ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                        ManageRole = ArManageRolesForm_get.save(commit=False)
                        ManageRole.ORG_ID = org_ins
                        ManageRole.create_by = ar_user_insta
                        ManageRole.update_by = ar_user_insta
                        ManageRole.save()
                        create_role_id = "AR_ROLE_"+str(ManageRole.id)
                        ArRole.objects.filter(id=ManageRole.id).update(role_id=create_role_id)
                        # ###########-----------------------------------------
                        if data != 0:
                            for val in data:
                                story_data = AR_USER_STORY.objects.filter(title=str(val))
                                for data in story_data:
                                    STP = data.story_tri_part_text
                                    data = quelity_score(STP)
                                AR_USER_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
                        # ###########-----------------------------------------

                        msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                    except(TypeError, OverflowError):
                        messages.error(request, "Something was wrong !")
            else:
                messages.error(request, ArManageRolesForm_get.errors)
            return redirect(settings.BASE_URL + "manage-role")
        msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_roles/index.html',{'date':datetime.now(),'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'role_data':role_data,'role_edit_status':role_edit_status,'get_all_role':get_all_role,'ArManageRolesForm_get':ArManageRolesForm_get,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized",notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

        # return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL})


@login_required
def edit_role(request,id):
    if product_view.check_permition(request, 'Manage Roles', 1):
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])

        ArRole_info = get_object_or_404(ArRole, pk=id)

        use_old = ArRole_info.use
        if use_old != "":
            data_old = use_old.split(" , ")
        else:
            data_old = 0

        Ar_Role = ArRole.objects.filter(ORG_ID=org_ins)
        role_form = ArRole.objects.get(id=id)
        role_id=role_form.id
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        if request.method == "POST":
            role_form = ArRoleForm( data=(request.POST or None),instance = role_form)
            if role_form.is_valid():
                title = role_form.cleaned_data.get('title')
                use = role_form.cleaned_data.get('use')
                if use != "":
                    data = use.split(" , ")
                else:
                    data = 0
                if ArRole.objects.filter(title=title).filter(ORG_ID=org_ins).exists():
                    msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Exists")
                    msg_data = msg.notification_desc
                    messages.error(request, title +" , " + msg_data)
                else:
                    try:
                        role_form.save()
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

                        msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Update")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                        return redirect(settings.BASE_URL + 'manage-role')
                    except:
                        messages.error(request,  role_form.errors)
            else:
                messages.error(request,  role_form.errors)
        else:
            role_form = ArRoleForm(instance=role_form)
        return render(request, 'admin/manage_roles/edit.html',{'date':datetime.now(),'role_edit':"value",'Ar_Role':Ar_Role,'role_id':role_id,'role_form':role_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized",notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

        # return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL})


@login_required
def remove_role(request,id):
    if product_view.check_permition(request, 'Manage Roles', 1):
        try:
            role = get_object_or_404(ArRole, pk=id)
            use = role.use
            if use != "":
                data = use.split(" , ")
            else:
                data = 0
            role.delete()
            # ###########-----------------------------------------
            if data != 0:
                for val in data:
                    story_data = AR_USER_STORY.objects.filter(title=str(val))
                    for data in story_data:
                        STP = data.story_tri_part_text
                        data = quelity_score(STP)
                    AR_USER_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
            # ###########-----------------------------------------
            msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        except(TypeError):
            msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
        return redirect(settings.BASE_URL + 'manage-role')
    else:
        msg = get_object_or_404(Notification, page_name="Manage Role", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
        return redirect(settings.BASE_URL + 'manage-role')


def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        print(check_map)
        if check_map == "" :
            role_val=0
        else:
            result = AR_USER_STORY.objects.filter(story_tri_part_text__icontains=check_map)
            role_data = ArUserStoryViewSerializer(result, many=True)
            role_val=role_data.data
        return JsonResponse({'check_project': role_val})
