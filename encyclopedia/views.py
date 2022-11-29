from django.shortcuts import render, redirect
from django.urls import reverse

from . import util
import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry_name):
    content = util.get_entry(entry_name)

    if content is not None:
        return render(request, "encyclopedia/entry.html", {
            "entry_name": entry_name,
            "entry" : content
        })
    else:
        return render(request, "encyclopedia/entry-not-found.html", {
            "entry_name": entry_name
        })

def add(request):
    return render(request, "encyclopedia/add.html")

def rand_entry(request):
    if request.method == "GET":
        entry_name = random.choice(util.list_entries())
        return redirect(reverse(entry, args=[entry_name]))


