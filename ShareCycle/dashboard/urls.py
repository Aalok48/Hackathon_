from . import views
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index, name="welcome"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('additem/', csrf_exempt(views.add_item), name='add_item')
]
