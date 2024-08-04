from django.urls import path

from examination_body import views

app_name = "examination_body_app"

urlpatterns = [
    path('create', views.create_examination_body, name='create_examination_body'),
    path('view/all', views.view_all_examination_body, name='view_all_examination_body')
]