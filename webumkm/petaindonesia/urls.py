from django.urls import path
from . import views, view_peta

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('welcome/', views.welcome, name='welcome_alt'),
    path('petasatu/', view_peta.petasatu, name='petasatu'),
    path('petadua/', view_peta.petadua, name='petadua'),
]
