# Generated by Django 2.1.7 on 2019-05-17 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0015_auto_20190518_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portal_management',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
