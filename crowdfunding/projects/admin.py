from django.contrib import admin
from .models import Project, Pledge, Categories, Images

# Register your models here.
admin.site.register(Project)
admin.site.register(Pledge)
admin.site.register(Categories)
admin.site.register(Images)