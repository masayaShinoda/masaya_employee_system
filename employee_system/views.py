from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def index(request):
    context = {
        'metadata': {
            "author": "Masaya Shida",
            'page_title': 'Home',
        }
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