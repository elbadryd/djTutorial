from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import ProductForm
from .models import Product

# Create your views here.
# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'title': obj.title,
#         'description': obj.description,
#         'price': obj.price
#     }
#     return render(request, "product/detail.html", context)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "product/create.html", context)

def dynamic_lookup_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    context = {
        "object": obj
        }
    return render(request, "product/detail.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "product/delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "product/list.html", context)