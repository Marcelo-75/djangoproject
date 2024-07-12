from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('salir/', views.salir, name='salir'),
]
