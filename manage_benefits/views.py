from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.conf import settings
from .forms import ArManageBenefitsForm
from .models import ArManageBenefits
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


def index(request):
    if product_view.check_permition(request, 'Manage Benefits', 0):
        benefits_edit_status = product_view.check_permition(request, 'Manage Benefits', 1)
        ArManageBenefitsForm_get = ArManageBenefitsForm()
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        get_all_Benefits = ArManageBenefits.objects.filter(ORG_ID=org_ins)
        if request.method == 'POST':
            ArManageBenefitsForm_get = ArManageBenefitsForm(request.POST)
            if ArManageBenefitsForm_get.is_valid():
                Benefit_title = ArManageBenefitsForm_get.cleaned_data.get('Benefits_title')
                use = ArManageBenefitsForm_get.cleaned_data.get('Use_in')
                if use != "":
                    data = use.split(" , ")
                else:
                    data = 0
                if ArManageBenefits.objects.filter(Benefits_title=Benefit_title).filter(ORG_ID=org_ins).exists():
                    msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Exists")
                    msg_data = msg.notification_desc

                    messages.error(request, Benefit_title +" , " + msg_data)
                else:
                    try:
                        ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                        ManageBenefits = ArManageBenefitsForm_get.save(commit=False)
                        ManageBenefits.ORG_ID = org_ins
                        ManageBenefits.created_by = ar_user_insta
                        ManageBenefits.updated_by = ar_user_insta
                        ManageBenefits.save()
                        create_benefite_id = "AR_BENEFITE_"+str(ManageBenefits.id)
                        ArManageBenefits.objects.filter(id=ManageBenefits.id).update(Benefits_id=create_benefite_id)
                        ###########-----------------------------------------
                        if data != 0:
                            for val in data:
                                story_data = AR_USER_STORY.objects.filter(title=str(val))
                                for data in story_data:
                                    STP = data.story_tri_part_text
                                    data = quelity_score(STP)
                                AR_USER_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
                        ###########-----------------------------------------


                        msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Add")
                        msg_data = msg.notification_desc
                        messages.info(request, msg_data)
                    except(TypeError, OverflowError):
                        messages.error(request, "Something was wrong !")
            else:
                messages.info(request, ArManageBenefitsForm_get.errors)
            return redirect(settings.BASE_URL + "manage-benefits")
        msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/manage_benefits/index.html',{'date':datetime.now(),'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'benefits_edit_status':benefits_edit_status,'get_all_Benefits':get_all_Benefits,'ArManageBenefitsForm_get':ArManageBenefitsForm_get,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized",notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})


        # return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL})


def edit(request,id):
    ArManageBenefits_info = get_object_or_404(ArManageBenefits, pk=id)

    use_old = ArManageBenefits_info.Use_in
    if use_old != "":
        data_old = use_old.split(" , ")
    else:
        data_old = 0
    ArManageBenefitsForm_get = ArManageBenefitsForm(instance=ArManageBenefits_info)
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    if request.method == 'POST':
        ArManageBenefitsForm_get = ArManageBenefitsForm(request.POST,instance=ArManageBenefits_info)
        if ArManageBenefitsForm_get.is_valid():
            Benefits_title = ArManageBenefitsForm_get.cleaned_data.get('Benefits_title')
            use = ArManageBenefitsForm_get.cleaned_data.get('Use_in')
            if use != "":
                data = use.split(" , ")
            else:
                data = 0
            if ArManageBenefits.objects.filter(Benefits_title=Benefits_title).filter(ORG_ID=org_ins).filter(~Q(id=id)).exists():
                msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request,Benefits_title +" , " + msg_data)
            else:
                try:
                    ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                    ManageBenefits = ArManageBenefitsForm_get.save(commit=False)
                    ManageBenefits.updated_by = ar_user_insta
                    ManageBenefits.save()
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
                    msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                except(TypeError, OverflowError):
                    messages.error(request, "Something was wrong !")
        else:
            messages.info(request, ArManageBenefitsForm_get.errors)
        return redirect(settings.BASE_URL + "manage-benefits")
    return render(request,'admin/manage_benefits/edit.html',{'date':datetime.now(),'ArManageBenefitsForm_get':ArManageBenefitsForm_get,'id':id,'BASE_URL': settings.BASE_URL})


def remove_benefit(request,id):
    if product_view.check_permition(request, 'Manage Benefits', 1):
        try:
            ManageBenefits = get_object_or_404(ArManageBenefits, pk=id)
            use = ManageBenefits.Use_in
            if use != "":
                data = use.split(" , ")
            else:
                data = 0
            # ManageGoals.delete()
            ManageBenefits.delete()
            # ###########-----------------------------------------
            if data != 0:
                for val in data:
                    story_data = AR_USER_STORY.objects.filter(title=str(val))
                    for data in story_data:
                        STP = data.story_tri_part_text
                        data = quelity_score(STP)
                    AR_USER_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
            # ###########-----------------------------------------
            msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Remove")
            msg_data = msg.notification_desc
            messages.info(request, msg_data)
        except(TypeError, OverflowError):
            msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Remove_error")
            msg_data = msg.notification_desc
            messages.error(request, msg_data)
    else:
        msg = get_object_or_404(Notification, page_name="Manage Benefit", notification_key="Permission")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-benefits')


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