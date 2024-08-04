from django.urls import path

from examination import views

app_name = "examination_app"

urlpatterns = [
    path('create', views.create_examination, name='create_examination'),
    path('view/all', views.view_all_examinations, name='view_all_examinations'),
]