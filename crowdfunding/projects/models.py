from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True) 
    owner = models.CharField(max_length=200) #Will need to update this to a foreign key to link to other model in database

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,       #This is important for when projects are deleted. If model(project) is cancelled, all pledges are deleted
        related_name='pledges'
    )
    supporter = models.CharField(max_length=200)    #Will need to be updated when user model created
