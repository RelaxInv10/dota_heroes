from django.urls import path
from . import views

app_name = 'description'

urlpatterns = [
    path('heroes/', views.heroes, name='heroes'),
    path('heroes/<int:pk>/', views.hero_datail, name='hero_datail'),
]