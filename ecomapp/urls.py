from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.base, name='base'),
    path('',views.home, name = 'home'),
]