# Generated by Django 4.1.5 on 2023-01-26 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_customuser_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.CharField(default='This is an empty bio', max_length=300),
            preserve_default=False,
        ),
    ]