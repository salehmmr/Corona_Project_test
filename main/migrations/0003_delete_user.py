# Generated by Django 3.1.3 on 2020-11-11 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_user_created_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
