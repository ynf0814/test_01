from django.urls import path
from polls import views

urlpatterns=[
    path('', views.index),
    path('create/', views.create),
    path('read/<id>/', views.read),
    path('lotto/', views.lotto)
]