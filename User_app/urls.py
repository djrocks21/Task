
from django.contrib import admin
from django.urls import path
from User_app import views 
from User_app.views import *


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register/', views.Register),
    path('login/', views.login_page),

        

]













