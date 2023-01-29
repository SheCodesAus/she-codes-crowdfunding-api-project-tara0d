from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    # path('images/', views.ImagesList.as_view()),
    path('categories/', views.CategoriesList.as_view()),
    path('projects/<int:pk>/like/', views.Liked.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)