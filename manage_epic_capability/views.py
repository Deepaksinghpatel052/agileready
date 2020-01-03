from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.conf import settings
from account.models import AR_organization,Ar_user
from manage_product.models import AR_product
from .models import AR_EPIC_CAPABILITY
from django.db import IntegrityError
from .forms import Ar_Epic_Capability_Form
from manage_features.models import AR_FEATURE
from django.contrib import messages


# Create your views here.
def index(request):
    # org_id=request.session['org_id']
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    ar_epic_capability = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).order_by("-id")
    return render(request, 'admin/manage_epic_capability/index.html',{'user_name':request.session['user_name'],'ar_epic_capability':ar_epic_capability,'BASE_URL': settings.BASE_URL})

def add_epic_capabilities(request):
    ar_feature = AR_FEATURE.objects.all()
    #####################################
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    if request.method == "POST":
        ar_epic_capability_form = Ar_Epic_Capability_Form(org_info,request.POST)
        if ar_epic_capability_form.is_valid():
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            # updated_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
            data = ar_epic_capability_form.save(commit=False)
            data.created_by=created_by_ins
            data.update_by = created_by_ins
            data.ORG_ID=org_ins
            try:
                data.save()
                messages.info(request, "Epic capability added successfully!")
            except:
                messages.error(request, ar_epic_capability_form.errors)
        else:
            messages.error(request, ar_epic_capability_form.errors)
    else:
        ar_epic_capability_form=Ar_Epic_Capability_Form(org_info)
    #####################################
    return render(request, 'admin/manage_epic_capability/add-manageenv-capabilities.html',{'user_name':request.session['user_name'],'ar_feature':ar_feature,'ar_epic_capability_form':ar_epic_capability_form,'BASE_URL': settings.BASE_URL})

def edit_epic_capabilities(request,id):
    ar_feature = AR_FEATURE.objects.filter(CE_ID=id)
    #######################################
    ar_epic_capability_form = AR_EPIC_CAPABILITY.objects.get(id=id)
    epic_id=ar_epic_capability_form.id
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    if request.method == "POST":
        ar_epic_capability_form = Ar_Epic_Capability_Form( data=(request.POST or None),org_info=org_info,instance = ar_epic_capability_form)
        if ar_epic_capability_form.is_valid():
            # print("hello")
            try:
                ar_epic_capability_form.save()
                messages.info(request, "Epic capability update successfully!")
                return redirect(settings.BASE_URL + 'manage-epic-capabilities/edit-epic-capabilities/' + id + '')
            except:
                messages.error(request, ar_epic_capability_form.errors)
        else:
            messages.error(request, ar_epic_capability_form.errors)
    else:
        ar_epic_capability_form = Ar_Epic_Capability_Form(instance=ar_epic_capability_form,org_info=org_info)
    #######################################
    return render(request, 'admin/manage_epic_capability/edit-manageenv-capabilities.html',{'user_name':request.session['user_name'],'ar_feature':ar_feature,'epic_id':epic_id,'ar_epic_capability_form':ar_epic_capability_form,'BASE_URL': settings.BASE_URL})

def delete_epic_capabilities(request,id):
    # return HttpResponse(id)
    try:
        AR_EPIC_CAPABILITY.objects.get(pk=id).delete()
        messages.info(request, "Epic capability removed!")
    except(TypeError):    
        messages.error(request, "Maybe this capabilities is used in another table so we can not remove that!")
    return redirect(settings.BASE_URL + 'manage-epic-capabilities')