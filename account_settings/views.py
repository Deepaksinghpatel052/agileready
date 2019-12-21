from django.shortcuts import render,redirect
from agileproject import settings
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request,"admin/account_settings/index.html",{"BASE_URL":settings.BASE_URL})
    else:
        return redirect(settings.BASE_URL)
