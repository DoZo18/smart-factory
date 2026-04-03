from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('table', views.dashboard, name='table'),
    path('predict', views.dashboard, name='predict'),
]