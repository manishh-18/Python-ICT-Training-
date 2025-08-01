from django.shortcuts import render , redirect
from newapp.models import test

# Create your views here.
from  django.http import HttpResponse
def home(request):
   data = test.objects.all() #to get all data from table to django
   dict_on={
       'data':data,
   }
   # return HttpResponse('welcomefhfhfh')
   if request.method == 'POST':
        var1 = request.POST.get('name')
        var2 = request.POST.get('number')
        test_instance = test(name=var1, number=var2)
        test_instance.save()
        return redirect('url_home')
   return render(request,'home.html',dict_on)