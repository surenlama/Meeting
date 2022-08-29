
from django.contrib import admin
from django.urls import path
from .views import VideoCreateView

app_name = 'meet'

urlpatterns = [
    path('create/', VideoCreateView.as_view(),name="create"),

]
