from django import forms
from django.shortcuts import render, redirect
from django.urls import reverse

from . import util
import random

class EntryForm(forms.Form):
    entry_name = forms.CharField(label="Entry Name")
    content = forms.CharField(label="Content", widget=forms.Textarea)

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
    if request.method == "GET":
        return render(request, "encyclopedia/add.html", {
            "form": EntryForm()
        })
    elif request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():   
            entry_name = form.cleaned_data["entry_name"]
            content = form.cleaned_data["content"]
            util.save_entry(entry_name,content)
            return redirect(f'/{entry_name}')
        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "encyclopedia/add.html", {
                "form": form
            })

def rand_entry(request):
    if request.method == "GET":
        entry_name = random.choice(util.list_entries())
        return redirect(reverse(entry, args=[entry_name]))


