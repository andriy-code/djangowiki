from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django import forms
import random
from . import util



def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

class newPageForm(forms.Form):
    article = forms.CharField(label="Name")
    content = forms.CharField(label="", widget=forms.Textarea)


def add(request):
    if request.method == "POST":
        form = newPageForm(request.POST)
        if form.is_valid() :
            article = form.cleaned_data["article"]
            content = form.cleaned_data["content"]
            old_content=util.get_entry(article)
            if old_content==None:
                util.save_entry(article, content)
                return HttpResponseRedirect(f"/wiki/{article}")
            else:
                return render(request, "./encyclopedia/add.html", {
                    "form": form
                     })
    else:
     return render(request, "encyclopedia/add.html", {
            "form": newPageForm()
    })


def article(request, name):
    content = util.get_entry(name)
    return render(request, "encyclopedia/article.html", {
            "name": name,
            "content": content
            })

def randomarticle(request):
    pages = util.list_entries()
    any = random.choice(pages)
    return HttpResponseRedirect(f"/wiki/{any}")

def search(request):
    search_list = []
    if request.method == "POST":
        form = request.POST
        entry_list = util.list_entries()
        wiki_entry_list = []
        for wiki in entry_list:
            wiki_entry_list.append(wiki.lower())
            if form['q'].lower() in wiki_entry_list:
                return HttpResponseRedirect(f"/wiki/{form['q']}")
            else:
                for wiki in entry_list:
                    if wiki.lower().find(form['q']) != -1:
                       search_list.append(wiki)
                return render(request, "encyclopedia/search.html", {
                    "entries": search_list
                })
def edit(request, name):
    content = util.get_entry(name)
    return render(request, "encyclopedia/edit.html", {
        "form": newPageForm({'article':name, 'content':content })
    })

def save(request):
    if request.method == "POST":
        form = newPageForm(request.POST)
        if form.is_valid() :
            article = form.cleaned_data["article"]
            content = form.cleaned_data["content"]
            util.save_entry(article, content)
            old_content=util.get_entry(article)
            return HttpResponseRedirect(f"/wiki/{article}")
            


