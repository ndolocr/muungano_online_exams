from django.urls import path

from examination_paper import views

app_name = "examination_paper_app"

urlpatterns = [
    path('create', views.create, name='create'),
]