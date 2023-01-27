from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Categories(models.Model):
    category_name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.category_name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    # image = models.ForeignKey(Images,on_delete=models.CASCADE,related_name="project_images",blank=True,null=True)
    is_open = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True) 
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    is_funded = models.BooleanField()
    funding_deadline = models.DateTimeField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    min_age = models.IntegerField()
    min_minutes = models.IntegerField()
    max_minutes = models.IntegerField()
    # images = models.ManyToManyField(Images, related_name= 'project_images', blank=True) #How can I move images above?
    categories = models.ManyToManyField(Categories, related_name = 'project_categories', blank=True)
    # pledges_total = models.IntegerField()
    def __str__(self) -> str:
        return self.title

class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,       #This is important for when projects are deleted. If model(project) is cancelled, all pledges are deleted
        related_name='pledges'
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='supporter_pledges'
    )
    pledge_date = models.DateTimeField(auto_now_add=True) #TO

class Images(models.Model):
    image_url = models.URLField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project_images",
        blank=True,null=True)
    def __str__(self) -> str:
        return self.project