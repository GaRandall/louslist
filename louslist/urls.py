from django.urls import path, register_converter
from . import views, converters
from django.contrib.auth.views import LogoutView

register_converter(converters.DepartmentConverter, 'dID')

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:dept>', views.departments, name='depts')
]
