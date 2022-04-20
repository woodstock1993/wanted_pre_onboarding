from .import models, serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from wanted_pre_onboarding.users.models import User as user_model
# from django.contrib.auth import authenticate, login

from . import models
from .forms import CreateProductForm, UpdateProductForm


# Create your views here
def index(request):
    if request.user.is_authenticated:
        products = models.Product.objects.all().order_by("-create_at")
        serializer = serializers.ProductSerializer(products, many=True)
        print(serializer.data)
        return render(request, 'posts/main.html', {"products": serializer.data})

def product_create(request):
    if request.method == 'GET':
        form = CreateProductForm()
        return render(request, 'posts/product_create.html', {"form": form})
        
    elif request.method == 'POST':
        if request.user.is_authenticated:
            user_id = get_object_or_404(user_model, pk=request.user.id)

            form = CreateProductForm(request.POST)
            
            if form.is_valid():
                post = form.save(commit=False) # 데이터 DB 저장안됨
                post.user_id = user_id
                post.save() # 이 때 저장
            else:
                print(form.errors)

            return render(request, 'posts/index.html')

        else:
            return render(request, 'users/main.html')
    
def product_update(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(models.Product, pk=product_id)
        if request.user != product.product_writer:
            return redirect(reverse('posts:index'))
        
        if request.method == 'GET':
            form = UpdateProductForm(instance=product)
            return render(
                request,
                'posts/product_update.html',
                {"form": form, "product":product }
            )
        elif request.method == 'POST':
            form = UpdateProductForm(request.POST)
            if form.is_valid():
                product.product_name = form.cleaned_data['product_name']
                product.product_writer = form.cleaned_data['product_writer']
                product.description = form.cleaned_data['description']
                product.funding_end_date = form.cleaned_data['funding_end_date']
                product.save()

            return redirect(reverse('posts:index'))

    else:
        return render(request, 'users/main.html')

def product_delete(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(models.Product, pk=product_id)
        if request.user == product.product_writer:
            product.delete()
        return redirect(reverse('posts:index'))
    else:
        return render(request, 'users/main.html')

def search(request):
    if request.user.is_authenticated:
        if request.method == "GET":
            searchKeyword = request.GET.get("search", "")
            user = get_object_or_404(user_model, pk=request.user.id)
            products = models.Product.objects.all().filter(Q(product_name__contains=searchKeyword)).order_by("-create_at")

            serializer = serializers.ProductSerializer(products, many=True)
            print(serializer.data)
            return render(request, 'posts/main.html', {"products": serializer.data})
        
        else:
            return render(request, "users/main.html")