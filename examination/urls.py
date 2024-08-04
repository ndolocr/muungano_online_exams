from django.urls import path

from examination import views

app_name = "examination_app"

urlpatterns = [
    path('create', views.create_examination, name='create_examination'),
]