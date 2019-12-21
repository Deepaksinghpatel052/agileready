from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from agileproject import settings
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def logout(request):
    del request.session['user_id']
    del request.session['org_id']
    del request.session['user_name']
    auth.logout(request)
    return redirect(settings.BASE_URL)
@login_required
def index(request):
    return render(request,"admin/dashboard/index.html",{'user_name':request.session['user_name'], "BASE_URL":settings.BASE_URL})

