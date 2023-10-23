from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from blog.models import Post
from django.urls import reverse_lazy

class Bloglistview(ListView):
    model = Post
    template_name = 'home.html'

class Blogdetailview(DetailView):
    model = Post
    template_name ='post_detail.html'


class Blogcreateview(CreateView):
    model = Post
    template_name ='post_new.html'
    fields = '__all__'


class Blogupdateview(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class Blogdeleteview(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')