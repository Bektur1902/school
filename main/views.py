from django.shortcuts import render
from django.views.generic import ListView
from .models import News


# Create your views here.


class HomeSchool(ListView):
    model = News
    template_name = 'main/nav.html'
    context_object_name = 'news'

class Days(ListView):
    model = News
    template_name = 'main/days.html'
    context_object_name = 'news'

