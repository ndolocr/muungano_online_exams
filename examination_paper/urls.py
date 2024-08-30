from django.urls import path

from examination_paper import views

urlpatterns = [
    path('create', views.create, name='create_examination_paper'),
]