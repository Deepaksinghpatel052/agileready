from django.shortcuts import render, HttpResponse,get_object_or_404
from django.conf import settings
from ar_user_story.forms import Ar_User_Story_Form
from account.models import Ar_user,AR_organization
from .models import AR_USER_STORY,AR_FEATURE,AR_ITERATIONS,AR_US_TYPE,AR_US_STATUS,AR_US_POINTS
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    ar_user_story = AR_USER_STORY.objects.all()
    print(ar_user_story)
    return render(request, 'admin/user_story_view/user-story-view.html',{'user_name':request.session['user_name'],'ar_user_story':ar_user_story,'BASE_URL': settings.BASE_URL})

def add_user_story_view(request):
    if request.method == "POST":
        ar_user_story_form = Ar_User_Story_Form(request.POST)
        if ar_user_story_form.is_valid():
            feature_ins = get_object_or_404(AR_FEATURE)
            pints_ins = get_object_or_404(AR_US_POINTS)
            status_ins = get_object_or_404(AR_US_STATUS)
            type_ins = get_object_or_404(AR_US_TYPE)
            iterations_ins = get_object_or_404(AR_ITERATIONS, pk=str(1))
            data = ar_user_story_form.save(commit=False)
            data.ft_id= feature_ins
            data.itr_id = iterations_ins
            data.usp_id = pints_ins
            data.uss_id = status_ins
            data.ust_id = type_ins
            data.save()
            #####################
            # product_form.is_valid()
            # org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            # ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
            # product = product_form.save(commit=False)
            # product.ORG_ID = org_ins
            # product.create_by = ar_user_insta
            # product.update_by = ar_user_insta
            # product.save()
            #####################
    else:
        ar_user_story_form=Ar_User_Story_Form()

    return render(request, 'admin/dashboard/user_story_view/add-user-story-view.html',{'user_name':request.session['user_name'],'ar_user_story_form':ar_user_story_form,'BASE_URL': settings.BASE_URL})

def edit_user_story_view(request,id):
    ar_user_story_form = AR_USER_STORY.objects.get(id=id)
    user_id=ar_user_story_form.id

    if request.method == "POST":
        ar_user_story_form = Ar_User_Story_Form(request.POST, instance = ar_user_story_form)
        if ar_user_story_form.is_valid():
            print("hello")
            ar_user_story_form.save()
        else:
            print("error")
    else:
        ar_user_story_form = Ar_User_Story_Form(instance=ar_user_story_form)
    return render(request, 'admin/dashboard/user_story_view/edit-user-story-view.html',{'user_id':user_id,'ar_user_story_form':ar_user_story_form,'BASE_URL': settings.BASE_URL})

def delete_user_story_view(request,id):
    AR_USER_STORY.objects.get(id=id).delete()
    return render(request, 'admin/dashboard/user_story_view/user-story-view.html', {'BASE_URL': settings.BASE_URL})