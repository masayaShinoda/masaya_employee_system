# Generated by Django 4.1 on 2022-12-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_system', '0006_alter_leavebalance_used_leave_annual_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavebalance',
            name='planned_leave_annual',
            field=models.PositiveIntegerField(default=0, verbose_name='Planned - Annual Leave'),
        ),
        migrations.AddField(
            model_name='leavebalance',
            name='planned_leave_maternity',
            field=models.PositiveIntegerField(default=0, verbose_name='Planned - Maternity Leave'),
        ),
        migrations.AddField(
            model_name='leavebalance',
            name='planned_leave_sick',
            field=models.PositiveIntegerField(default=0, verbose_name='Planned - Sick Leave'),
        ),
        migrations.AddField(
            model_name='leavebalance',
            name='planned_leave_work_home',
            field=models.PositiveIntegerField(default=0, verbose_name='Planned - Work From Home'),
        ),
    ]