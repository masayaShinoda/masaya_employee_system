from django.contrib import admin
from .models import MyUser, LeaveBalance, Leave

# Register your models here.
admin.site.register(MyUser)
admin.site.register(LeaveBalance)
admin.site.register(Leave)