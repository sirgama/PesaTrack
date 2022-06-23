from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing, name='landing'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('expenses/', views.expenses, name='expenses'),
    path('search/', views.search, name='search'),
]

    
    