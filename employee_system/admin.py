from django.contrib import admin
from .models import MyUser, LeaveBalance

# Register your models here.
admin.site.register(MyUser)
admin.site.register(LeaveBalance)