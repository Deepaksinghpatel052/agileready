from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib import messages
from django.conf import settings
from account.models import AR_organization,Ar_user
from manage_epic_capability.models import AR_EPIC_CAPABILITY
from .forms import Ar_Featurre_Form
from .models import AR_FEATURE
from user_story_view.models import AR_USER_STORY
from agileproject.serializers import Ar_Epic_Serializer,Ar_Feature_Serializer


# Create your views here.
def index(request):
    # org_id=request.session['org_id']

    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])

    ar_feature = AR_FEATURE.objects.filter(ORG_ID=org_ins).order_by("-id")
    return render(request, 'admin/manage_features/index.html',{'ar_feature':ar_feature,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


def add_features(request):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    epic_data = AR_EPIC_CAPABILITY.objects.filter(ORG_ID=org_ins).order_by("-id")
    #####################################
    org_info = AR_organization.objects.filter(id=request.session['org_id'])
    if request.method == "POST":
        ar_featurre_form = Ar_Featurre_Form(org_info,request.POST)
        print('ar_featurre_form')
        print(ar_featurre_form)
        if ar_featurre_form.is_valid():
            created_by_ins = get_object_or_404(Ar_user, pk=request.session['user_id'])
            org_ins = get_object_or_404(AR_organization, id=request.session['org_id'])
            data = ar_featurre_form.save(commit=False)
            # data.CE_ID =  ar_featurre_form.cleaned_data.get('CE_ID')
            data.ORG_ID = org_ins
            data.create_by = created_by_ins
            data.update_by = created_by_ins
            try:
                data.save()
                ar_featurre_form.save_m2m()
                messages.info(request, "Feature added successfully!")
            except:
                messages.error(request, ar_featurre_form.errors)
        else:
            messages.error(request, ar_featurre_form.errors)
    else:
        ar_featurre_form=Ar_Featurre_Form(org_info)
    #####################################
    return render(request, 'admin/manage_features/add-manageenv-feature.html',{'epic_data':epic_data,'ar_featurre_form':ar_featurre_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


def edit_features(request,id):
    #######################################
    ar_feature_form =AR_FEATURE.objects.get(id=id)
    feature_id=ar_feature_form.id
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    org_info = AR_organization.objects.filter(id=str(org_ins.id))
    if request.method == "POST":
        ar_feature_form = Ar_Featurre_Form( data=(request.POST or None),org_info=org_info,instance = ar_feature_form)
        if ar_feature_form.is_valid():
            try:
                ar_feature_form.save()
                messages.info(request, "Feature updated successfully!")
                return redirect(settings.BASE_URL + 'manage-feature/edit-feature/' + id + '')
            except:
                messages.error(request, ar_featurre_form.errors)
        else:
            messages.error(request, ar_featurre_form.errors)
    else:
        ar_feature_form = Ar_Featurre_Form(instance=ar_feature_form,org_info=org_info)
    return render(request, 'admin/manage_features/edit-manageenv-feature.html',{'feature_id':feature_id,'ar_feature_form':ar_feature_form,'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL})


def delete_features(request,id):
    AR_FEATURE.objects.get(id=id).delete()
    messages.info(request, "Features removed!")
    return redirect(settings.BASE_URL + 'manage-feature')

def get_data(request):
    if request.method == "POST":
        check_map = request.POST['check']
        print('check_map[0]')
        print(check_map)
        feature_data = AR_FEATURE.objects.filter(CE_ID=check_map)
        feature = Ar_Feature_Serializer(feature_data, many=True)
        return JsonResponse({'check_project': feature.data})
    return JsonResponse({'check_project':"sorry"})