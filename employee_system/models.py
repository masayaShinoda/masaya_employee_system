from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.core.validators import MinValueValidator


# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField('email_address', max_length=254, blank=False)
    dept_manager = models.BooleanField(default=False, verbose_name="Department Manager")


class LeaveBalance(models.Model):
    user = models.ForeignKey(MyUser, verbose_name=("user"), on_delete=models.CASCADE)

    starting_leave_annual = models.PositiveIntegerField(verbose_name='Starting Balance - Annual Leave', default=18)
    planned_leave_annual = models.PositiveIntegerField(verbose_name='Planned - Annual Leave', default=0)
    used_leave_annual = models.PositiveIntegerField(verbose_name='Used Balance - Annual Leave', default=0)
    
    starting_leave_sick = models.PositiveIntegerField(verbose_name='Starting Balance - Sick Leave', default=100)
    planned_leave_sick = models.PositiveIntegerField(verbose_name='Planned - Sick Leave', default=0)
    used_leave_sick = models.PositiveIntegerField(verbose_name='Used Balance - Sick Leave', default=0)

    starting_leave_work_home = models.PositiveIntegerField(verbose_name='Starting Balance - Work From Home', default=20)
    planned_leave_work_home = models.PositiveIntegerField(verbose_name='Planned - Work From Home', default=0)
    used_leave_work_home = models.PositiveIntegerField(verbose_name='Used Balance - Work From Home', default=0)

    starting_leave_maternity = models.PositiveIntegerField(verbose_name='Starting Balance - Maternity Leave', default=0)
    planned_leave_maternity = models.PositiveIntegerField(verbose_name='Planned - Maternity Leave', default=0)
    used_leave_maternity = models.PositiveIntegerField(verbose_name='Used Balance - Maternity Leave', default=0)


    def __str__(self):
        return f"""
        {self.id}. {self.user.username}'s Remaining Balance: Annual: {self.starting_leave_annual - self.used_leave_annual} | Sick: {self.starting_leave_sick - self.used_leave_sick} | Home: {self.starting_leave_work_home - self.used_leave_work_home} | Maternity: {self.starting_leave_maternity - self.used_leave_maternity}
        """

class Leave(models.Model):
    user = models.ForeignKey(MyUser, verbose_name=("user"), on_delete=models.CASCADE)
    
    LEAVE_TYPES = (
        ("Annual Leave", "Annual Leave"),
        ("Sick Leave", "Sick Leave"),
        ("Work From Home", "Work From Home"),
        ("Maternity Leave", "Maternity Leave"),
    )

    leave_type = models.CharField(max_length=32, choices=LEAVE_TYPES, default="Annual Leave")
    leave_date = models.DateField(validators=[MinValueValidator(datetime.date.today)])


    def __str__(self):
        return f"""
        {self.id}. {self.user.username} ({self.leave_type}) {self.leave_date}
        """