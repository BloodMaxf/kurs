from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from . import models
from users.models import Personal_area
from django.contrib.auth.models import User

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

class Buy_item(DeleteView):
    model = models.Product
    model1 = Personal_area
    model2 = User

    template_name = 'buy_item.html'
    success_url = reverse_lazy('home')

    def buy(self):
        model = models.Product
        model1 = Personal_area
        model2 = User
        model1.title = model.title
        model1.key = model.key
        model1.user_id = model2.username
