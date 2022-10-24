from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models


class HomePageView(ListView):
    model = models.Product
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'