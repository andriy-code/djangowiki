from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.article, name="article"),
    path("add", views.add, name="add"),
    path("randomarticle", views.randomarticle, name="randomarticle"),
    path("search/", views.search, name="search"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("edit", views.save, name="save")
]
