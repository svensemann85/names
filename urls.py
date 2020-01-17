from django.urls import path
from . import views

urlpatterns = [
    path('api/name/',
    views.NameListCreate.as_view()),
    path('api/rating/',
    views.RatingListCreate.as_view()),
]