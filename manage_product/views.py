from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from agileproject import settings
from .forms import ProductForm
from django.contrib import messages
from account.models import Ar_user,AR_organization
from django.contrib.auth.decorators import login_required
from .models import AR_product
# Create your views here.
@login_required
def index(request):
    org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
    all_project_get = {}
    if AR_product.objects.filter(ORG_ID=org_ins).exists():
        all_project_get = AR_product.objects.filter(ORG_ID=org_ins).order_by("-id")
    else:
        all_project_get = {}
    return render(request, 'admin/manage_product/index.html', {'user_name':request.session['user_name'],'BASE_URL':settings.BASE_URL,"all_project_get":all_project_get})

@login_required
def add_product(request):
    # product_form = ProductForm(request.POST or None,request.session['org_id'])
    if request.method == 'POST':
        product_form = ProductForm(request.user,request.session['org_id'], request.POST)
        status = product_form.is_valid()
        if product_form.is_valid():
            org_ins = get_object_or_404(AR_organization, pk=request.session['org_id'])
            ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
            product = product_form.save(commit=False)
            product.ORG_ID = org_ins
            product.create_by = ar_user_insta
            product.update_by = ar_user_insta
            product.save()
            product_form.save_m2m()
            messages.info(request, "Product add successfully.")
        else:
            messages.info(request, product_form.error)
        return redirect(settings.BASE_URL + "manage-products/add-product")
    else:
        product_form = ProductForm(request.user,request.session['org_id'])
    return render(request, 'admin/manage_product/add_project.html', {'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL,'product_form':product_form})

@login_required
def remove_product(request,id):
    project = get_object_or_404(AR_product, pk=id)
    project.delete()
    messages.info(request, "Product remove successfully.")
    return redirect(settings.BASE_URL+'manage-products')

@login_required
def edit_product(request,id):
    product_info = get_object_or_404(AR_product, pk=id)
    if request.method == 'POST':
        product_form = ProductForm(request.user, request.session['org_id'], request.POST,instance = product_info)
        if product_form.is_valid():
            product = product_form.save(commit=False)
            ar_user_insta = get_object_or_404(Ar_user, pk=request.session['user_id'])
            product.update_by = ar_user_insta
            product.save()
            product_form.save_m2m()
            messages.info(request, "Product updase successfully.")
        else:
            messages.error(request, product_form.error)
        return redirect(settings.BASE_URL + "manage-products")
    else:
        product_form = ProductForm(request.user, request.session['org_id'],instance=product_info)
    return render(request, 'admin/manage_product/edit_project.html',{'user_name':request.session['user_name'],'BASE_URL': settings.BASE_URL, 'product_form': product_form})
