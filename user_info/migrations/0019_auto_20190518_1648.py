# Generated by Django 2.1.7 on 2019-05-18 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0018_auto_20190518_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal_management',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to='users_profile/'),
        ),
    ]
