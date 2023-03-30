from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Status
from django.urls import  reverse_lazy

from datetime import datetime

class  PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status =Status.objects.get(name= "published")
        context["list"] = Post.objects.filter(
            status= published_status).order_by("created_on").reverse()
        context["timestamp"] = datetime.now().strftime("%F %H:%M:%S")
        return context

# Create your views here.
class PostDetailView(DetailView):
    template_name ="posts/detail.html"
    model = Post 

class DraftPostListView(ListView, LoginRequiredMixin):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        unpublished_status =Status.objects.get(name= "unpublished")
        context["list"] = Post.objects.filter(
            status= unpublished_status).filter(
            author=self.request.user).order_by("created_on").reverse()
        context["timestamp"] = datetime.now().strftime("%F %H:%M:%S")
        return context

class PostCreateView(CreateView, LoginRequiredMixin):
    template_name = "posts/new.html"
    model=Post
    fields = ["title", "body", "author", "status"]

class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostUpdateView(UpdateView, UserPassesTestMixin, LoginRequiredMixin):
    template_name= 'posts/update.html'
    model = Post
    fields = ["title", "body", "status"]

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
