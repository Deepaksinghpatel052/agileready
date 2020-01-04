from django.shortcuts import render
from django.conf import settings
from manage_product.models import AR_product
from manage_epic_capability.models import AR_EPIC_CAPABILITY

# Create your views here.
def index(request):
    # epic = AR_EPIC_CAPABILITY.objects.all()
    product_data = AR_product.objects.filter(ORG_ID=request.session['org_id'])
    # for PROJECT_ID in AR_EPIC_CAPABILITY.objects.all():
    # print('product_data.epic_set.all()')
    # print(product_data)
    # print(product_data[0].project_by_epic.all())
    # # print(epic.PROJECT_ID.all())
    #
    # # for aParent in AR_product.objects.all():
    # #     print("{0} --> {1}".format(aParent, aParent.child_set.all()))
    #
    # # epic = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=request.session['org_id'])
    # epic = AR_EPIC_CAPABILITY.objects.all().select_related("PROJECT_ID").order_by("PROJECT_ID")
    # # epic = AR_EPIC_CAPABILITY.objects.all()
    # for data in product_data:
    #     get=AR_EPIC_CAPABILITY.objects.all().filter(PROJECT_ID=data.id)
    #
    #     # print(get)
    #
    # # print(product_data[0].Team_parent.all())
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


    return render(request, 'admin/product_view/index.html',{'product_data':product_data,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})
