from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home, name="home"),
    path('search/', views.search_meaning, name='search_meaning'),
    path('history/', views.search_history, name='search_history'),
    path('clear-history/', views.clear_search_history, name='clear_history'),
]