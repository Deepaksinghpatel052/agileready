from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth.models import User,auth
from agileproject import settings
from account.models import AR_organization
from manage_product.models import AR_product,AR_team
from manage_backlogs.models import AR_BACKLOG
from user_story_view.models import AR_USER_STORY
from manage_iterations.models import AR_ITERATIONS

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
    # return HttpResponse(request.session['org_id'])
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    team = AR_team.objects.filter(ORG_id=org_ins).count()
    product = AR_product.objects.filter(ORG_ID=org_ins).count()
    backlog = AR_BACKLOG.objects.filter(ORG_ID=org_ins).count()
    user_storyes = AR_USER_STORY.objects.filter(ORG_id=org_ins).count()
    itearations = AR_ITERATIONS.objects.filter(ORG_ID=org_ins).count()

    return render(request,"admin/dashboard/index.html",{'itearations':itearations,'user_storyes':user_storyes,'team':team,'product':product,'backlog':backlog,'user_name':request.session['user_name'], "BASE_URL":settings.BASE_URL})

