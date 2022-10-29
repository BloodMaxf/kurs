from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from . import models


class HomePageView(ListView):
    model = models.Product
    template_name = 'home.html'

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'


class SearchResultsView(ListView):
    model = models.Product
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = models.Product.objects.filter(
            Q(title__icontains=query) | Q(genre__icontains=query)
        )
        return object_list