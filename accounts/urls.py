
from django.urls import path,include
from .views import *

urlpatterns = [
    path('get/',RegisterViews.as_view()),
]
