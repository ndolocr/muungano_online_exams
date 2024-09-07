from django.urls import path

from examination_paper import views

app_name = "examination_paper_app"

urlpatterns = [
    path('create', views.create, name='create'),
    path('view/all', views.view_all, name='view_all'),
    path('view/<int:pk>', views.view_single, name='view_single'),
    path('create/insturctions/<int:pk>', views.create_instructions, name='create_instructions'),
    path('create/insturctions/post', views.create_instructions_post, name='create_instructions_post'),
]