# Generated by Django 4.1.5 on 2023-01-23 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_bio_customuser_developer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
