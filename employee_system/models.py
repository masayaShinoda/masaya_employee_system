from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUser(AbstractUser):
    email = models.EmailField('email_address', max_length=254, blank=False)

class LeaveBalance(models.Model):
    user = models.ForeignKey(MyUser, verbose_name=("user"), on_delete=models.CASCADE)

    leave_annual = models.PositiveIntegerField(verbose_name='Annual Leave', default=18)
    leave_sick = models.PositiveIntegerField(verbose_name='Sick Leave', default=100)
    leave_work_home = models.PositiveIntegerField(verbose_name='Work From Home', default=20)
    leave_maternity = models.PositiveIntegerField(verbose_name='Maternity Leave', default=0)

    def __str__(self):
        return f"""
        {self.id}. [{self.user.username}]: Annual: {self.leave_annual} | Sick: {self.leave_sick} | Home: {self.leave_work_home} | Maternity: {self.leave_maternity}
        """