from django.urls import path
from . import views

urlpatterns = [
  path('', views.ExerciseListCreate.as_view(), name="exercise-view-create"),
]