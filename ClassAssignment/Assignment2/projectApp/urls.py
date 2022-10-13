from django.urls import path
#now import the views.py file into this code
from . import views
from .views import GeeksList, GeeksCreate, GeeksDetailView, GeeksUpdateView, GeeksDeleteView, GeeksFormView

urlpatterns=[
  path('', GeeksFormView.as_view()),
  path('home_view_form/', views.home_view_form),
  path('home_view_img/', views.home_view_img),
  path('home_view_model/', views.home_view_model),
  path('formset_view/', views.formset_view),
  path('modelformset_view/', views.modelformset_view),
  path('geeks_template_view/', views.geeks_template_view),
  path('geeks_time_view/', views.geeks_time_view),
  path('list_view/', views.list_view),
  path('as_view/', GeeksList.as_view()),
  path('detail_view/<id>',views.detail_view),
  path('update_view/<id>',views.update_view),
  path('<id>/delete', views.delete_view),
  path('create_view/', GeeksCreate.as_view()),
  path('<pk>/', GeeksDetailView.as_view()),
  path('<pk>/update', GeeksUpdateView.as_view()),
  path('<pk>/delete/', GeeksDeleteView.as_view()),
]

