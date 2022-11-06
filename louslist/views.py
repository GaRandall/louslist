from django.shortcuts import render, redirect
import requests
from django.urls import reverse
from django.contrib.auth import logout
from django.http import HttpResponseRedirect


# Create your views here.

def home(request):
    response = requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()

    context = {
        'data': response
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


#def LogoutView(request):
 #   logout(request)
  #  return HttpResponseRedirect('')