# Generated by Django 4.1.5 on 2023-01-21 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_pledge_pledge_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='max_age',
        ),
    ]