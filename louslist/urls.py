from django.urls import path, register_converter
from . import views, converters
from django.contrib.auth.views import LogoutView

register_converter(converters.DepartmentConverter, 'dID')

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:dept>', views.departments, name='depts'),
    path('<str:dept>/<int:course_num>', views.course, name='course'),
    path('<str:dept>/<int:course_num>/newreview', views.leave_a_review, name='newreview'),
    path('<str:dept>/<int:course_num>/<str:review_id>', views.review_detail, name='reviewdetail')
]
