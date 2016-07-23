
from django.conf.urls import url
from django.contrib import admin
from main import views 

urlpatterns = [
   url(r'^sabado-ubuntu$',views.Sabado.as_view())
]
