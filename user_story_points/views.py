from django.shortcuts import render,get_object_or_404,redirect
from django.conf import settings
from .models import ArUserStoryPoints
from .forms import ArStoryPointForm
from account.models import AR_organization,Ar_user,ArShowcolumns,Notification
from manage_product.models import AR_product
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from django.contrib import messages
from manage_product import views as product_view
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    if product_view.check_permition(request, 'Manage User Story Points', 0):
        check_edit_permition = product_view.check_permition(request, 'Manage User Story Points', 1)
        org_info = AR_organization.objects.filter(id=request.session['org_id'])
        ar_story_point_form = ArStoryPointForm(org_info)
        org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
        story_point = ArUserStoryPoints.objects.filter(ORG_ID=org_ins).order_by("-id").filter(~Q(Point_Key = 'None'))
        msg = get_object_or_404(Notification, page_name="Manage User Story Points", notification_key="Not_Remove")
        Not_Remove_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage User Story Points", notification_key="Remove Request")
        Remove_Request_msg = msg.notification_desc
        msg = get_object_or_404(Notification, page_name="Manage User Story Points", notification_key="Remove_Success")
        Remove_done_msg = msg.notification_desc
        return render(request, 'admin/user_story_points/index.html',{'date':datetime.now(),'Remove_done_msg':Remove_done_msg,'Remove_Request_msg':Remove_Request_msg,'Not_Remove_msg':Not_Remove_msg,'check_edit_permition':check_edit_permition,'ar_story_point_form':ar_story_point_form,'story_point':story_point,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    else:
        msg = get_object_or_404(Notification, page_name="Authorized", notification_key="Error")
        error_data = msg.notification_desc
        return render(request, 'admin/dashboard/no_permssion.html', {'BASE_URL': settings.BASE_URL,'error_message':error_data})

def add_story_point(request):
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    if request.method == "POST":
        ar_story_point_form = ArStoryPointForm(org_info,request.POST)
        if ar_story_point_form.is_valid():
            Point_Key = ar_story_point_form.cleaned_data.get('Point_Key')
            if ArUserStoryPoints.objects.filter(Point_Key=Point_Key).filter(ORG_ID=org_ins).exists():
                msg = get_object_or_404(Notification, page_name="Manage User Story Points",
                                        notification_key="Exists")
                msg_data = msg.notification_desc
                messages.error(request,msg_data)
            else:
                created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
                org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
                data = ar_story_point_form.save(commit=False)
                data.create_by=created_by_ins
                data.update_by = created_by_ins
                data.ORG_ID=org_ins
                data.save()
                try:
                    data.save()
                    msg = get_object_or_404(Notification, page_name="Manage User Story Points",
                                            notification_key="Add")
                    msg_data = msg.notification_desc
                    messages.info(request, msg_data)
                    return redirect(settings.BASE_URL + 'story-points')
                except:
                    messages.error(request, ar_story_point_form.errors)
        else:
            messages.error(request, ar_story_point_form.errors)
    else:
        ar_story_point_form=ArStoryPointForm(org_info)
    return redirect(settings.BASE_URL + 'story-points')



def edit_story_point(request,id):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    Ar_User_Story_Points = ArUserStoryPoints.objects.filter(ORG_ID=request.session['org_id'])
    Ar_User_Story_Points_form = ArUserStoryPoints.objects.get(id=id)
    story_point_id=Ar_User_Story_Points_form.id
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    if request.method == "POST":
        Ar_User_Story_Points_form = ArStoryPointForm( data=(request.POST or None),org_info=org_info,instance = Ar_User_Story_Points_form)
        if Ar_User_Story_Points_form.is_valid():
            try:
                Ar_User_Story_Points_form.save()
                msg = get_object_or_404(Notification, page_name="Manage User Story Points",
                                        notification_key="Update")
                msg_data = msg.notification_desc
                messages.info(request, msg_data)
                return redirect(settings.BASE_URL + 'story-points')
            except:
                messages.error(request,  Ar_User_Story_Points_form.errors)
        else:
            messages.error(request,  Ar_User_Story_Points_form.errors)
    else:
        Ar_User_Story_Points_form = ArStoryPointForm(instance=Ar_User_Story_Points_form,org_info=org_info)
    return render(request, 'admin/user_story_points/index.html',
                  {'date':datetime.now(),'ar_story_point_form': Ar_User_Story_Points_form, 'story_point': Ar_User_Story_Points,
                   'user_name': request.session['user_name'],'point':"value",'story_point_id':story_point_id, 'BASE_URL': settings.BASE_URL})


def delete_story_point(request,id):
    try:
        ArUserStoryPoints.objects.get(pk=id).delete()
        msg = get_object_or_404(Notification, page_name="Manage User Story Points", notification_key="Remove")
        msg_data = msg.notification_desc
        messages.info(request, msg_data)
    except(TypeError):
        msg = get_object_or_404(Notification, page_name="Manage User Story Points", notification_key="Remove_error")
        msg_data = msg.notification_desc
        messages.error(request, msg_data)
    return redirect(settings.BASE_URL + 'story-points')