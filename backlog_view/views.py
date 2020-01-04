from django.shortcuts import render
from django.conf import settings
from manage_backlogs.models import AR_BACKLOG
from manage_backlogs.forms import Ar_Backlog_Form
from account.models import AR_organization
from manage_epic_capability.models import AR_EPIC_CAPABILITY

# Create your views here.
def index(request):
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    backlog_data = AR_BACKLOG.objects.filter(ORG_ID=request.session['org_id'])
    ar_backlog_form = Ar_Backlog_Form(org_info)
    #
    # # epic = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=request.session['org_id'])
    # epic = AR_EPIC_CAPABILITY.objects.all().select_related("PROJECT_ID").order_by("PROJECT_ID")
    # # epic = AR_EPIC_CAPABILITY.objects.all()
    # for data in product_data:
    #     get=AR_EPIC_CAPABILITY.objects.all().filter(PROJECT_ID=data.id)
    #
    #     print(get)
    #
    # print(product_data[0].Team_parent.all())
    #
    # # print('epic.data')
    # # print(epic[0].PROJECT_ID.id)
    #
    #
    # # print(epic[1].PROJECT_ID.id)
    # # print(epic[2].PROJECT_ID.id)
    # # print(product_data[0].Procduct_name)
    # # print(epic.data)
    #
    # ########################################
    # # ar_backlog = AR_BACKLOG.objects.filter(ORG_ID=request.session['org_id'])
    # # print(ar_backlog[0].BL_STATUS.bl_status_desc)
    # ########################################


    # return render(request, 'admin/product_view/index.html',{'epic':epic,'product_data':product_data,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
    return render(request, 'admin/backlog_view/index.html',{'ar_backlog_form':ar_backlog_form,'backlog_data':backlog_data,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
