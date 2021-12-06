from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomaPageView(TemplateView):
    template_name = 'home.html'
