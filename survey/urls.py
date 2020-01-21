from django.urls import path
from . import views

urlpatterns = [
    path('survey-new', views.survey_new, name='survey-new'),
]
