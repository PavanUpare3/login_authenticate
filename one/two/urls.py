from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.showform, name = 'signup'),
    path('login/', views.loginShow, name='login'),
    path('profile/', views.profiless, name='profile'),
]
