# urls.py

from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='sign-up'),
    path('about/', views.about, name='about-us'),
    path('faq/', views.faq, name='faq'),




]
