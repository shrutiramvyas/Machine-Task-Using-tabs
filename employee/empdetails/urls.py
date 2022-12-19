from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('albert',views.albert,name="Albert"),
    path('nikola',views.nikola,name="Nikola"),
    path('raman',views.raman,name="Raman")
    # path('update',views.update,name="update")
]