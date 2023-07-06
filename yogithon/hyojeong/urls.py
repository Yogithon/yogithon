from django.contrib import admin
from django.urls import path
from pet.views import *  # blog.views에서 선언한 모든 것을 가져온다.



urlpatterns = [
  path('admin/', admin.site.urls),
  path('', home, name="home"),
  path('<str:id>', detail, name="detail"),
  path('new/', new, name="new"),
  path('create/', create, name="create"),
]

