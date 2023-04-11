from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Categories(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self) -> str:
        return self.category_name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    is_open = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True) 
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='owner_projects'
    )
    funding_deadline = models.DateTimeField()
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    min_age = models.IntegerField()
    min_minutes = models.IntegerField()
    max_minutes = models.IntegerField()
    categories = models.ManyToManyField(Categories, related_name = 'project_categories', blank=True)
    favourited_by = models.ManyToManyField(User, related_name="favourites", blank=True)
    thumbnail_image = models.URLField()

    def __str__(self) -> str:
        return self.title

    @property
    def total_pledged(self):
        total = 0
        for pledge in self.pledges.all():
            total += pledge.amount
        return total

    @property
    def is_funded(self):
        return self.goal <= self.total_pledged

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

    def __str__(self) -> str:
        return str(self.project)

class Images(models.Model):
    image_url = models.URLField()
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project_images",
        )

    class Meta:
        verbose_name_plural = "images"

    def __str__(self) -> str:
        return str(self.project)