from django.shortcuts import HttpResponse
from django.contrib import admin
from django.urls import path
from courses.views import coursePage, LoginView, SignupView, Home, logout_view, checkout, verify_payment, MyCoursesList

def index(request):
    return HttpResponse('i get it')

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('course/<str:slug>/', coursePage, name='coursepage'),
    path('login/', LoginView.as_view(), name='login'),
    path('checkout/<str:slug>/', checkout, name="checkout"),
    path('verify_payment/', verify_payment, name="verify_payment"),
    path('my-courses/', MyCoursesList.as_view(), name='my_courses'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('logout/', logout_view, name='logout'),
]
