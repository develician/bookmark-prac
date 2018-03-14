from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_create'
    success_url = reverse_lazy('bookmark:index')
    def form_valid(self, form):
        if form.is_valid:
            form.instance.save()
            return redirect('/bookmark/')
        else:
            return self.render_to_response({'form': form})

class BookmarkModifyView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDetailView(LoginRequiredMixin, DetailView):
    model = Bookmark

class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')
