from django.shortcuts import render, HttpResponse
from django.conf import settings
from ar_user_story.forms import Ar_User_Story_Form

# Create your views here.
def index(request):
    return render(request, 'admin/dashboard/user_story_view/user-story-view.html',{'BASE_URL': settings.BASE_URL})

def add_user_story_view(request):
    if request.method == "POST":
        ar_user_story_form = Ar_User_Story_Form(request.POST)
        if ar_user_story_form.is_valid():
            # owner = form.cleaned_data.get('owner')
            # ar_user = form.cleaned_data.get('ar_user')
            # title = form.cleaned_data.get('title')
            # user = User.objects.create_user(username=email, email=email, first_name=first_name, password=password)
            # user.save()
            ar_user_story_form.save()

            author="Save"
            return HttpResponse(author)


    else:
        ar_user_story_form=Ar_User_Story_Form()
        author="author"
    #########################################################
    #########################################################
    return render(request, 'admin/dashboard/user_story_view/add-user-story-view.html',{'author':author,'ar_user_story_form':ar_user_story_form,'BASE_URL': settings.BASE_URL})
    # return render(request, 'admin/dashboard/user_story_view/add-user-story-view.html',{'BASE_URL': settings.BASE_URL})

def edit_user_story_view(request):
    ar_user_story_form = Ar_User_Story_Form()
    return render(request, 'admin/dashboard/user_story_view/edit-user-story-view.html',{'ar_user_story_form':ar_user_story_form,'BASE_URL': settings.BASE_URL})

