from django.urls import path
#now import the views.py file into this code
from . import views
from .views import hello_books

urlpatterns=[
  path('', hello_books),
]

