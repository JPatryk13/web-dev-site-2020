from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hire_me', views.hire_me, name='hire_me')
]
