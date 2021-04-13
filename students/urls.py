from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('students/', StudentListView.as_view()),
    path('students/<int:pk>', StudentView.as_view()),
]
