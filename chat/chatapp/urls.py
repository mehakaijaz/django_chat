from django.urls import path
from .views import *

urlpatterns=[
    path("",HomePage,name='home'),
    path('<str:room_name>/<str:username>',MessageView, name='room'),
]