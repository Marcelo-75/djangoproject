from django.urls import path, include
#from rest_framework import routers
# from .api import HeladoViewSet
from .views import index, register, profile, login_view, salir

# router = routers.DefaultRouter()
# router.register('api', HeladoViewSet, 'core')

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'), # revisar q cuando esta logueado Admin no anda
    path('login/', login_view, name='login'),
    path('salir/', salir, name='salir'),
    # path('api/', include(router.urls)),
]

