from typing import Any, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404 # render shortcut is used to add rendered templates
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import post 

# Create your views here.


class PostListView(ListView):
    model = post # setting model to post model from models.py 
    template_name = 'blog/home.html' #setting template to home.html
    context_object_name = 'posts'
    ordering = '-date_posted' # ordering makes the list set in specific order by adding date_posted from post model
                              # which is in models.py
    paginate_by = 3 # this makes the home page to paginate by 2 posts per 
    
class UserPostListView(ListView):
    model = post # setting model to post model from models.py 
    template_name = 'blog/user_posts.html' #setting template to home.html
    context_object_name = 'posts'
    paginate_by = 3 # this makes the home page to paginate by 2 posts per page

    # to filter the post by respective user in UserPostListView
    def get_queryset(self):
        user = get_object_or_404(User, username = self.kwargs.get('username'))
        return post.objects.filter(author= user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = post # setting model to post model from models.py 
    

class PostCreateView(LoginRequiredMixin,CreateView):
    model = post # setting model to post model from models.py 
    fields = ['title','content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
        

#UserPassesTestMixin enables only respective users to edit their posts
#LoginRequiredMixin makes user to create or update a post only if logged in 
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = post # setting model to post model from models.py 
    fields = ['title','content']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post # setting model to post model from models.py 
    success_url ='/' # success url to homepage

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False 

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})