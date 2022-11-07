from django.db import models
from django.contrib.auth.models import AbstractUser


#class User(AbstractUser):
#    courses=


class Dept(models.Model):
    subject = models.CharField(max_length=200,primary_key=True, db_column='subject_id')


class Subject(models.Model):
    instructor = models.CharField(max_length=200)
    course_number = models.IntegerField(primary_key=True,db_column='subj_id')
    semester_code = models.IntegerField()
    course_section = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    catalog_number = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    component = models.CharField(max_length=200)
    class_capacity = models.IntegerField()
    wait_list = models.IntegerField()
    wait_cap = models.IntegerField()
    enrollment_total = models.IntegerField()
    enrollment_available = models.IntegerField()
    topic = models.CharField(max_length=200)
    meetings = models.CharField(max_length=200)


class Review(models.Model):
    review_id = models.IntegerField(primary_key=True)
    course_id = models.CharField(max_length=8)
    overall_rating = models.IntegerField()
    difficulty_rating = models.IntegerField()
    user_email = models.CharField(max_length=50)
    review_title = models.CharField(max_length=200)
    review_text = models.CharField(max_length=600)
