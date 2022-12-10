# Generated by Django 4.1 on 2022-12-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_system', '0005_leavebalance_used_leave_annual_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavebalance',
            name='used_leave_annual',
            field=models.PositiveIntegerField(default=0, verbose_name='Used Balance - Annual Leave'),
        ),
        migrations.AlterField(
            model_name='leavebalance',
            name='used_leave_sick',
            field=models.PositiveIntegerField(default=0, verbose_name='Used Balance - Sick Leave'),
        ),
        migrations.AlterField(
            model_name='leavebalance',
            name='used_leave_work_home',
            field=models.PositiveIntegerField(default=0, verbose_name='Used Balance - Work From Home'),
        ),
    ]
