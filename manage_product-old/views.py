from django.shortcuts import render,HttpResponse
from agileproject import settings
# Create your views here.

def index(request):
    return render(render(request, 'admin/manage_product/index.html', {'BASE_URL':settings.BASE_URL}))