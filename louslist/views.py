from django.shortcuts import render
import requests
from django.urls import reverse


# Create your views here.

def home(request):
    response = requests.get('http://luthers-list.herokuapp.com/api/dept/CS/?format=json').json()

    context = {
        'data': response
    }
    return render(request, 'louslist/index.html', context)


def departments(request):
    print(request.path_info)
    path = request.path_info
    department = path[1:].upper()

    data = requests.get("http://luthers-list.herokuapp.com/api/dept/" + department + "/?format=json").json()

    context = {
        'data': data,
        'subject': department
    }
    return render(request, 'louslist/subject.html', context)
