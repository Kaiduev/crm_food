# Generated by Django 3.0.4 on 2020-04-29 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm_food_app', '0012_auto_20200427_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
    ]
