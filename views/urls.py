from django.urls import path, include
from .views import ListUsers

urlpatterns = [
    path('hello', ListUsers),
]
