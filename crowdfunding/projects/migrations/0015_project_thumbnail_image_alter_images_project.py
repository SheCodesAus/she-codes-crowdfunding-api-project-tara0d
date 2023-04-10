# Generated by Django 4.1.5 on 2023-02-20 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_project_favourited_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='thumbnail_image',
            field=models.URLField(default='https://www.cdc.gov/healthypets/images/pets/cute-dog-headshot.jpg?_=42445'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='images',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_images', to='projects.project'),
        ),
    ]
