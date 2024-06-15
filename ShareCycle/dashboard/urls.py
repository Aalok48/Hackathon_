from . import views
from django.urls import path

urlpatterns = [
    path('',views.index, name="welcome"),
    path('dashboard/', views.dashboard, name='dashboard'),
]
