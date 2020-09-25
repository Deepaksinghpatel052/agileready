from django.shortcuts import render,HttpResponse,get_object_or_404,redirect
from django.conf import settings
from .forms import ArTestactSetForm
from .models import ArTestactSet
from account.models import AR_organization,Ar_user,Notification
from django.contrib import messages
from django.db.models import Q
from manage_product import views as product_view
from django.http import HttpResponse,JsonResponse
from test_story_view.models import AR_TEST_STORY
from datetime import datetime
from agileproject.serializers import ArUserStoryViewSerializer
from user_story_view.user_story_score.readiness_quality_score import quelity_score
# Create your views here.


def index(request):
    #
    ArTestactSetForm_get = ArTestactSetForm()
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    get_all = ArTestactSet.objects.filter(ORG_ID=org_ins)
    if request.method == 'POST':
        ArTestactSetForm_get = ArTestactSetForm(request.POST)
        if ArTestactSetForm_get.is_valid():
            member_product_list = ArTestactSetForm_get.cleaned_data.get('member_product_list')
            use = ArTestactSetForm_get.cleaned_data.get('Use_in')
            if use != "":
                data = use.split(" , ")
            else:
                data = 0
            if ArTestactSet.objects.filter(member_product_list=member_product_list).filter(ORG_ID=org_ins).exists():
                msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request, member_product_list +" , " + msg_data)
            else:
                try:
                    ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                    ArTestactSetdata = ArTestactSetForm_get.save(commit=False)
                    ArTestactSetdata.ORG_ID = org_ins
                    ArTestactSetdata.created_by = ar_user_insta
                    ArTestactSetdata.updated_by = ar_user_insta
                    ArTestactSetdata.save()
                    # create_benefite_id = "AR_BENEFITE_"+str(ManageBenefits.id)
                    # ArManageBenefits.objects.filter(id=ManageBenefits.id).update(Benefits_id=create_benefite_id)
                    # ###########-----------------------------------------
                    if data != 0:
                        for val in data:
                            story_data = AR_TEST_STORY.objects.get(title=str(val))
                            STP = story_data.story_tri_part_text
                            data = quelity_score(STP)
                            AR_TEST_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
                    # ###########-----------------------------------------


                    msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Add")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                except(TypeError, OverflowError):
                    messages.error(request, "Something was wrong !")
        else:
            messages.info(request, ArTestactSetForm_get.errors)
        return redirect(settings.BASE_URL + "manage-testact-set")

    msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Not_Remove")
    Not_Remove_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Remove Request")
    Remove_Request_msg = msg.notification_desc
    msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Remove_Success")
    Remove_done_msg = msg.notification_desc
    # return render(request, 'admin/manage_benefits/index.html',{'date':datetime.now(),'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'benefits_edit_status':benefits_edit_status,'get_all_Benefits':get_all_Benefits,'ArManageBenefitsForm_get':ArManageBenefitsForm_get,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})

    return render(request, 'admin/manage_testact_set/index.html',{'date':datetime.now(),'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'get_all':get_all,'ArTestactSetForm_get':ArTestactSetForm_get,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


        # return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL})



def edit(request,id):
    ArTestactSet_info = get_object_or_404(ArTestactSet, pk=id)

    use_old = ArTestactSet_info.Use_in
    if use_old != "":
        data_old = use_old.split(" , ")
    else:
        data_old = 0
    ArTestactSetForm_get = ArTestactSetForm(instance=ArTestactSet_info)
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    if request.method == 'POST':
        ArTestactSetForm_get = ArTestactSetForm(request.POST,instance=ArTestactSet_info)
        if ArTestactSetForm_get.is_valid():
            member_product_list = ArTestactSetForm_get.cleaned_data.get('member_product_list')
            use = ArTestactSetForm_get.cleaned_data.get('Use_in')
            if use != "":
                data = use.split(" , ")
            else:
                data = 0
            if ArTestactSet.objects.filter(member_product_list=member_product_list).filter(ORG_ID=org_ins).filter(~Q(id=id)).exists():
                msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request,member_product_list +" , " + msg_data)
            else:
                try:
                    ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
                    ArTestactSetdata = ArTestactSetForm_get.save(commit=False)
                    ArTestactSetdata.updated_by = ar_user_insta
                    ArTestactSetdata.save()
                    # # ###########-----------------------------------------
                    if data_old != 0:
                        for val_old in data_old:
                            # return HttpResponse(val_old)
                            story_data = AR_TEST_STORY.objects.filter(title=str(val_old))
                            STP = story_data[0].story_tri_part_text
                            title = story_data[0].title
                            data_val = quelity_score(STP)
                            # return HttpResponse(data_val)
                            AR_TEST_STORY.objects.filter(title=title).update(readiness_quality_score=data_val[0])
                    # # ###########-----------------------------------------
                    # ###########-----------------------------------------
                    if data != 0:
                        for val in data:
                            # return HttpResponse(val)
                            story_data = AR_TEST_STORY.objects.filter(title=str(val))
                            STP = story_data[0].story_tri_part_text
                            title = story_data[0].title
                            data_get = quelity_score(STP)
                            # return HttpResponse(data_get)
                            AR_TEST_STORY.objects.filter(title=title).update(readiness_quality_score=data_get[0])
                    # ###########-----------------------------------------
                    msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Update")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                except(TypeError, OverflowError):
                    messages.error(request, "Something was wrong !")
        else:
            messages.info(request, ArTestactSetForm_get.errors)
        return redirect(settings.BASE_URL + "manage-testact-set")
    return render(request,'admin/manage_testact_set/edit.html',{'date':datetime.now(),'ArTestactSetForm_get':ArTestactSetForm_get,'id':id,'BASE_URL': settings.BASE_URL})
#

#
def remove_Testact_Set(request,id):
    try:
        ArTestactSetvalue = get_object_or_404(ArTestactSet, pk=id)
        use = ArTestactSetvalue.Use_in
        if use != "":
            data = use.split(" , ")
        else:
            data = 0
        # ManageGoals.delete()
        ArTestactSetvalue.delete()
        # # ###########-----------------------------------------
        if data != 0:
            for val in data:
                story_data = AR_TEST_STORY.objects.get(title=str(val))
                STP = story_data.story_tri_part_text
                data = quelity_score(STP)
                AR_TEST_STORY.objects.filter(title=val).update(readiness_quality_score=data[0])
        # # ###########-----------------------------------------
        msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Remove")
        msg_data = msg.notification_desc
        messages.info(request, msg_data)
    except(TypeError, OverflowError):
        msg = get_object_or_404(Notification, page_name="Manage Testact", notification_key="Remove_error")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'manage-testact-set')
#
#
def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        print(check_map)
        if check_map == "" :
            gole_val=0
        else:
            result = AR_TEST_STORY.objects.filter(story_tri_part_text__icontains=check_map)
            gole_data = ArUserStoryViewSerializer(result, many=True)
            gole_val=gole_data.data
        return JsonResponse({'check_project': gole_val})