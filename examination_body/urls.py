from django.urls import path

from examination_body import views

app_name = "examination_body_app"

urlpatterns = [
    path('create', views.create, name='create'),
    path('view/all', views.view_all, name='view_all'),
    path('update/<int:pk>', views.update, name='update'),
    path('update/post', views.update_post, name='update_post'),
]