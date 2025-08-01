from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def product(request):
    if request.method == "POST":
        pro_name =  request.POST.get('pro_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        discount = request.POST.get('discount')
        pro = Product(pro_name=pro_name,price=price,quantity=quantity,discount=discount)
        pro.save()
        return redirect('product')
    return render(request,'product.html')