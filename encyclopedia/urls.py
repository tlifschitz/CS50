from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add, name="add"),
    path("random", views.rand_entry, name="random"),
    path("<str:entry_name>", views.entry, name="entry")
]
