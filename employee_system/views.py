from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from .models import LeaveBalance

from django.core import serializers

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        leave_balance = serializers.serialize('json', [LeaveBalance.objects.all().get(user=request.user), ])
    else:
        leave_balance = None


    context = {
        'metadata': {
            'author': 'Masaya Shida',
            'page_title': 'Home',
        },
        'data': {
            'leave_balance': leave_balance,
        },
        'misc': {
        },
    }

    return render(request, "employee_system/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign the user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if auth is successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "employee_system/login.html", {
                "message": "Invalid username or password. Please try again."
            })

    else:
        return render(request, "employee_system/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))