from .views import RegistrationView, UsernameValidationView, EmailValidationView, LoginView,LogoutView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('register',RegistrationView.as_view(),name="register"),
    path('login',LoginView.as_view(),name="login"),
    path('validate-username',csrf_exempt(UsernameValidationView.as_view()), name="validate-username"),
    path('validate-email',csrf_exempt(EmailValidationView.as_view()), name="validate_email"),
    path('logout',LogoutView.as_view(),name="logout"),

]
