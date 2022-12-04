from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("search/", views.search, name="search_empty"),
    path("search/<str:key>", views.search, name="search"),
    path("random", views.rand_entry, name="random"),
    path("wiki/", views.entry, name="entry_empty"),
    path("wiki/<str:entry_name>", views.entry, name="entry"),
    path("edit/", views.edit, name="edit_empty"),
    path("edit/<str:entry_name>", views.edit, name="edit")
]
