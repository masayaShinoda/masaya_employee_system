from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.urls import reverse
from .models import LeaveBalance, Leave

from django.core import serializers
import json

from datetime import date
import calendar

from .forms import BookLeaveForm


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        try:
            leave_balance = serializers.serialize('json', [LeaveBalance.objects.all().get(user=request.user), ])
        except LeaveBalance.DoesNotExist:
            leave_balance = None
        try:
            leave = serializers.serialize('json', Leave.objects.all().filter(user=request.user))
        except Leave.DoesNotExist:
            leave = None

        # this_month = date.today().month
        this_year = date.today().year

        html_calendar = calendar.HTMLCalendar()

        months_calendar_this_year = []

        for month in range(1,13):
            months_calendar_this_year.append(html_calendar.formatmonth(this_year, month))
        
        national_holidays = (
            {'International New Year Day': date(this_year, 1, 1).strftime("%Y-%m-%d")},
            {'Victory Day over Genocide': date(this_year, 1, 7).strftime("%Y-%m-%d")},
            {'International Women\'s Day': date(this_year, 3, 8).strftime("%Y-%m-%d")},
            {'Khmer New Year': date(this_year, 4, 14).strftime("%Y-%m-%d")},
            {'Khmer New Year': date(this_year, 4, 15).strftime("%Y-%m-%d")},
            {'Khmer New Year': date(this_year, 4, 16).strftime("%Y-%m-%d")},
            {'International Labor Day': date(this_year, 5, 1).strftime("%Y-%m-%d")},
            {'Visak Bochea Day': date(this_year, 5, 4).strftime("%Y-%m-%d")},
            {'Royal Plowing Ceremony': date(this_year, 5, 8).strftime("%Y-%m-%d")},
            {'King Norodom Sihamoni\'s Birthday': date(this_year, 5, 14).strftime("%Y-%m-%d")},
            {'Queen Monineath\'s Birthday': date(this_year, 6, 18).strftime("%Y-%m-%d")},
            {'Constitutional Day': date(this_year, 9, 24).strftime("%Y-%m-%d")},
            {'Pchum Ben Festival': date(this_year, 10, 13).strftime("%Y-%m-%d")},
            {'Pchum Ben Festival': date(this_year, 10, 14).strftime("%Y-%m-%d")},
            {'Pchum Ben Festival': date(this_year, 10, 15).strftime("%Y-%m-%d")},
            {'Respect the spirit of the late King Father': date(this_year, 10, 15).strftime("%Y-%m-%d")},
            {'Coronation Day of King Sihamoni': date(this_year, 10, 29).strftime("%Y-%m-%d")},
            {'National Independence Day': date(this_year, 11, 9).strftime("%Y-%m-%d")},
            {'Water Festival': date(this_year, 11, 26).strftime("%Y-%m-%d")},
            {'Water Festival': date(this_year, 11, 27).strftime("%Y-%m-%d")},
            {'Water Festival': date(this_year, 11, 28).strftime("%Y-%m-%d")},
        )


        context = {
            'metadata': {
                'author': 'Masaya Shida',
                'page_title': 'Home',
            },
            'data': {
                'leave_balance': leave_balance,
                'leave': leave,
                'months_calendar_this_year': months_calendar_this_year,
                'national_holidays': json.dumps(national_holidays),
                'book_leave_form': BookLeaveForm(),
            },
            'misc': {
            },
        }

        return render(request, "employee_system/index.html", context)

    # If user is not signed in and requests index page, redirect to login
    else:
        return HttpResponseRedirect(reverse("login"))


def book_leave(request):
    if request.user.is_authenticated:
        form = BookLeaveForm(request.POST)
        if form.is_valid():
            leave = Leave(
                user = request.user,
                leave_start = form.cleaned_data['leave_start'],
                leave_until = form.cleaned_data['leave_until'],
                leave_type = form.cleaned_data['leave_type'],
                leave_reason = form.cleaned_data['leave_reason'],
            ) # Leave model
            leave.save()

            return HttpResponseRedirect(reverse("index"))
        # Todo: handle bad submissions


def login_view(request):
    # If user is already signed in and requests login page, redirect to index
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    else:
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
    return HttpResponseRedirect(reverse("login"))

# def book_leave(request):
#     # If user is already signed in and requests login page, redirect to index
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             # store form data as variables
#             date_start = request.POST["date_start"]
#             date_end = request.POST["date_end"]