# Generated by Django 4.1.5 on 2023-01-21 00:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_funding_deadline_project_is_funded_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pledge',
            name='pledge_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
