from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView,View, UpdateView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

class RepList(ListView):
    model = Repository
    ordering = '-date'
    context_object_name = 'rep'
    paginate_by = 10
    template_name = 'repositories.html'


class PackageList(ListView):
    model = Package
    ordering = '-date'
    context_object_name = 'pac'
    paginate_by = 10
    template_name = 'packages.html'
# Create your views here.
