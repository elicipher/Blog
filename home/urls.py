from django.urls import path
from .views import detail , home , category

urlpatterns = [
    path("",home , name="home"),
    path("home/page/<int:page>/",home , name="home"),
    path("article/<slug:slug>/",detail , name="detail"),
    path("category/<slug:slug>/",category , name="category"),
    path("category/<slug:slug>/page/<int:page>/",category , name="category"),
]