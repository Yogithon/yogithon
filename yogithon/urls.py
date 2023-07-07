from django.contrib import admin
from django.urls import path
from . import views

app_name = "yogithon"

urlpatterns = [
    path('', views.main, name="home"),
    path('detail/<int:pk>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('login/github/', views.github_login, name='github-login'),
    path('login/github/callback/', views.github_login_callback, name='github-callback'),

]