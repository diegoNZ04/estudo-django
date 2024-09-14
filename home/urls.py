from django.urls import path
from home import views

urlpatterns = [
    path('ver_home/', views.ver_home, name="ver_home"),
    
    path('inserir_item/', views.inserir_item, name="inserir_item")
]
