from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="home"),
    path('shop/', views.shop,name="shop"),
    path('product/', views.product,name="product"),

]