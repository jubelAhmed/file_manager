from django.urls import path

from . import views

urlpatterns = [
    path('upload/', views.index, name='upload'),
    path('list/', views.display_list, name='file_list'),
]