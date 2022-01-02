from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name='home.html'
    
class BlogDetailView(DetailView):
    # DetailView will provide a context object we can use in our template called either object or the lowercased name of the model (in this case, post)
    model=Post
    template_name='post_detail.html'
    #context_object_name="..." allows for manual renaming of the context object for use in HTML.

class BlogCreateView(CreateView):
    model=Post
    template_name="post_new.html"
    fields=["title","author","body"]
    # Exposes these fields to the form to be created.
    # Each entry will be added to the Post database model as new entries.

class BlogUpdateView(UpdateView):
    model=Post
    template_name='post_edit.html'
    fields=['title','body']
    
class BlogDeleteView(DeleteView):
    model=Post
    template_name='post_delete.html'
    success_url=reverse_lazy('home')
    # reverse_lazy so that it won't execute the URL direct until our view has finisshed deleting blog posts.
    
    
    