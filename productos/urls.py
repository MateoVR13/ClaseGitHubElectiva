from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('guitarra-esp-ltd/', views.guitarra_esp_ltd, name='guitarra_esp_ltd'),
    path('eii-eclipse/', views.eii_eclipse, name='eii_eclipse'),
    path('eii-tb7/', views.eii_tb7, name='eii_tb7'),
]
