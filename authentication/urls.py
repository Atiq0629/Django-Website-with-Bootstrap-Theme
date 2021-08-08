from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.authlogin, name='login'),
    path('registration/', views.authregistration, name='registration'),
    path('forget-password/', views.forgetpassword, name='forgetpassword'),
    path('logout/', views.authlogout, name='authlogout')
    
]