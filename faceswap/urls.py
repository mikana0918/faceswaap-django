from django.urls import path, include
from . import views


app_name='faceswap'

urlpattern = [
    path('about/', views.index),
]