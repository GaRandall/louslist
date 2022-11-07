from django.contrib import admin
from .models import Dept,Subject

class DeptAdmin(admin.ModelAdmin):
    fields = ['subject']

class SubjectAdmin(admin.ModelAdmin):
    fields = ['course_number','instructor','semester_code','course_section','subject','catalog_number','description','units','component','class_capacity','wait_list','wait_cap','enrollment_total','enrollment_available','topic','meetings']

admin.site.register(Dept, DeptAdmin)
admin.site.register(Subject, SubjectAdmin)
# Register your models here.
