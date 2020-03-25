from django.urls import path

from user import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('create/', views.create, name='create_user')
]