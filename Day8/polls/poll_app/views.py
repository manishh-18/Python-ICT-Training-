from django.shortcuts import render, redirect
from .models import User, PollResponse

def poll_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        choice = request.POST.get("choice")

        user = User.objects.create(name=name, email=email)
        PollResponse.objects.create(user=user, choice=choice)

        return redirect('thank_you')

    return render(request, 'poll_app/form.html')

def thank_you(request):
    return render(request, 'poll_app/thank_you.html')
