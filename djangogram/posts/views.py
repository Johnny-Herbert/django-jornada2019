from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from posts.models import Post
from posts.forms import PostCreateForm

# Create your views here.

class PostListView(LoginRequiredMixin,generic.ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'post/list_post.html'
    ordering =['-created_at']

class PostCreateView(LoginRequiredMixin,generic.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/create_post.html'
    success_url = reverse_lazy('posts:list_post') # app_name:NomeUrl, redireciona quando tiver sucesso
    
    def get_initial(self):
        return {
            'user': self.request.user,
        }
    def form_valid(self,form):
        messages.success(
            self.request,
            'Você compartilhou um novo post! Confira abaixo'
        )
        return super().form_valid(form)
