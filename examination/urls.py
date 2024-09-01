from django.urls import path

from examination import views

app_name = "examination_app"

urlpatterns = [
    path('create', views.create, name='create'),
    path('view/all', views.view_all, name='view_all'),
]