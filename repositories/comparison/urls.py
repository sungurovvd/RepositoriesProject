from django.urls import path
from .views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('reps/', RepList.as_view(), name = 'repositories'),

]