from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util
import random

class EntryForm(forms.Form):
    entry_name = forms.CharField(label="Entry Name")
    content = forms.CharField(label="Content", widget=forms.Textarea)

def index(request):
    key = request.GET.get('q')

    if key is None:
        return render(request, "encyclopedia/index.html", {
            "title_suffix" : "",
            "heading": "All Pages",
            "entries": util.list_entries()
        })
    else:
        return redirect(reverse(search, args=[key]))

def search(request, key):
    entries = util.list_entries()

    matches = [entry_name for entry_name in entries if key.lower() in entry_name.lower()]

    if len(matches) == 0:
        return render(request, "encyclopedia/entry-not-found.html", {
            "entry_name": key
        })
    if len(matches) == 1:
        return redirect(reverse(entry, args=[matches[0]]))
    else:
        return render(request, "encyclopedia/index.html", {
        "title_suffix" : " Search",
        "heading": "Search Results",
        "entries": matches
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
    if request.method == "GET":
        return render(request, "encyclopedia/add.html", {
            "form": EntryForm()
        })
    elif request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():   
            entry_name = form.cleaned_data["entry_name"]
            content = form.cleaned_data["content"]

            stored_name = [name for name in util.list_entries() if name.lower() == entry_name.lower()]
                
            if len(stored_name) == 0:
                util.save_entry(entry_name, content)
                return redirect(f'wiki/{entry_name}')
            else:
                return render(request, "encyclopedia/add.html", {
                    "error_msg" : f"Page {stored_name[0]} already exists",
                    "form": form
                })
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "encyclopedia/add.html", {
                "error_msg" : f"Form is invalid",
                "form": form
            })

def rand_entry(request):
    if request.method == "GET":
        entry_name = random.choice(util.list_entries())
        return redirect(reverse(entry, args=[entry_name]))


