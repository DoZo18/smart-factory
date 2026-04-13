from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('table', views.data_table, name='table'),
    path('form', views.form_view, name='form'),
    path('predict', views.predict_page,name = 'predict')

]
