from django.urls import path
from petaindonesia import views, view_peta

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('welcome/', views.welcome, name='welcome_alt'),
    path('petasatu/', view_peta.petasatu, name='petasatu'),
    path('petadua/', view_peta.petadua, name='petadua'),
    path('petakampus/', view_peta.petakampus, name='petakampus'),
    path('petaindonesia/provinsi/', view_peta.peta_provinsi, name='peta_provinsi'),
    path('petaindonesia/petani_jawa/', view_peta.petani_jawa, name='petani_jawa'),
]
