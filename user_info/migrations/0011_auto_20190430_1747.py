# Generated by Django 2.1.7 on 2019-04-30 12:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0010_patient_register_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_register',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='portal_management',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
