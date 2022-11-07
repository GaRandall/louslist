from django.shortcuts import render, redirect
import requests
from django.urls import reverse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
import json
from .models import Dept, Subject


# Create your views here.

def home(request):
    resp = requests.get('http://luthers-list.herokuapp.com/api/deptlist/?format=json').json()
    #for key in resp:
    #    dep = Dept(key['subject'])
    #    dep.save()
    #for x in Dept.objects.all():
    #    print(x.subject)
    #    res = requests.get("http://luthers-list.herokuapp.com/api/dept/" + x.subject + "/?format=json").json()
    #    for a in res:
    #        sub = Subject(a['instructor'], a['course_number'], a['semester_code'], a['course_section'], a['subject'],
    #                      a['catalog_number'], a['description'], a['units'], a['component'], a['class_capacity'],
    #                      a['wait_list'], a['wait_cap'], a['enrollment_total'], a['enrollment_available'], a['topic'],
    #                      a['meetings'])
    #        sub.save()
    context = {
        'data': resp
    }
    return render(request, 'louslist/index.html', context)


def departments(request, dept):
    print(request.path_info)

    data = requests.get("http://luthers-list.herokuapp.com/api/dept/" + dept.upper() + "/?format=json").json()

    context = {
        'data': data,
        'subject': dept
    }
    return render(request, 'louslist/subject.html', context)

# def LogoutView(request):
#   logout(request)
#  return HttpResponseRedirect('')
