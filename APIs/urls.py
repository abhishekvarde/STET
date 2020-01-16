from django.urls import path, include
from APIs import views
# from rest_framework import serializers

urlpatterns = [
    path('login/', views.user_login, name="user_login"),
    path('register/', views.user_register, name="user_register"),
    path('get_profile/', views.get_profile, name="get_profile"),
    path('save_form/', views.save_form, name="save_form"),
    path('get_form/', views.get_form, name="get_form"),
    # path('fun/', views.fun, name="fun"),
]
