from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name='home.html'
    
class BlogDetailView(DetailView):
    # DetailView will provide a context object we can use in our template called either object or the lowercased name of the model (in this case, post)
    model=Post
    template_name='post_detail.html'
    #context_object_name="..." allows for manual renaming of the context object for use in HTML.