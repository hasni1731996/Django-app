# Generated by Django 2.1.7 on 2019-04-30 06:22

from django.db import migrations, models
import user_info.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0008_auto_20190429_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_Register',
            fields=[
                ('id', models.UUIDField(default=user_info.models.generateUUID, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
