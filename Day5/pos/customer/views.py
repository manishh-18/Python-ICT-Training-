from django.shortcuts import render,redirect
from .models import Customer

# Create your views here.
def customer(request):
    if request.method == "POST":
        cus_name =  request.POST.get('cus_name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        address = request.POST.get('address')
        cust = Customer(cus_name=cus_name,mobile=mobile,email=email,address=address)
        cust.save()
        return redirect('customer')
    return render(request,'customer.html')