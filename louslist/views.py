from django.shortcuts import render, redirect
import requests
from django.http import HttpResponseRedirect
from .forms import NewReviewForm
from .models import Dept, Subject, Review, UniqueUser
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    resp = requests.get('http://luthers-list.herokuapp.com/api/deptlist/?format=json').json()
    # for key in resp:
    #    dep = Dept(key['subject'])
    #    dep.save()
    # for x in Dept.objects.all():
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


def course(request, dept, course_num):
    review_total = 0
    difficulty_total = 0
    count = 0
    relevant_reviews = Review.objects.filter(course_id=dept + str(course_num))
    for review in relevant_reviews:
        count += 1
        review_total += review.overall_rating
        difficulty_total += review.difficulty_rating
    if count > 0:
        review_avg_string = str(review_total / count)
        difficulty_avg_string = str(difficulty_total / count)
    else:
        review_avg_string = "No reviews"
        difficulty_avg_string = "No reviews"
    context = {
        'reviews': relevant_reviews,
        'dept': dept,
        'course_num': course_num,
        'review_avg': review_avg_string,
        'difficulty_avg': difficulty_avg_string,
        'review_count': count
    }
    return render(request, 'louslist/course.html', context)


def leave_a_review(request, dept, course_num):
    submitted = False
    if request.method == "POST":
        form = NewReviewForm(request.POST)
        if form.is_valid():
            course_id = dept + str(course_num)
            overall_rating = form.cleaned_data['overall_rating']
            difficulty_rating = form.cleaned_data['difficulty_rating']
            user_name = form.cleaned_data['user_name']
            user_email = form.cleaned_data['user_email']
            review_title = form.cleaned_data['review_title']
            review_text = form.cleaned_data['review_text']
            review_date = timezone.now()
            new_review = Review(course_id=course_id, overall_rating=overall_rating, difficulty_rating=difficulty_rating,
                                user_name=user_name, user_email=user_email, review_title=review_title,
                                review_text=review_text, review_date=review_date)
            new_review.save()
            return HttpResponseRedirect('/' + str(dept) + '/' + str(course_num) + '/newreview?submitted=True')
    else:
        form = NewReviewForm
        if 'submitted' in request.GET:
            submitted = True
    context = {
        'dept': dept,
        'course_num': course_num,
        'form': form,
        'submitted': submitted
    }
    return render(request, 'louslist/newReview.html', context)


def review_detail(request, dept, course_num, review_id):
    the_review = Review.objects.filter(id=review_id)[0]
    context = {
        'dept': dept,
        'course_num': course_num,
        'review_id': review_id,
        'review': the_review
    }
    return render(request, 'louslist/reviewDetail.html', context)

def add_user(request):
    obj, created = UniqueUser.objects.get_or_create(
        userID = request.user,
        userName = request.user.username,
        userEmail = request.user.email,
    )
    return HttpResponseRedirect(reverse('home'))

# def LogoutView(request):
#   logout(request)
#  return HttpResponseRedirect('')
