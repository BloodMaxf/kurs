from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView,TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import Purchased

class HomePageView(ListView):
    model = models.Product
    template_name = 'home.html'
    paginate_by = 4

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

class Buy_item(LoginRequiredMixin, DetailView):
    model = models.Product

    template_name = 'buy_item.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    # def post_save(request):
    #     model1 = models.Purchased_products
    #     new_post = models.Purchased_products(request.POST)
    #     model1.title = request.POST["title"]
    #     model1.key = request.POST["key"]
    #     model1.user_id = request.POST["user_id"]
    #     model1.save()

class Add_game(CreateView, LoginRequiredMixin):
    model = models.Product
    form_class = Purchased
    template_name = 'Add_game.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

class GameDelete(DeleteView):
    model = models.Product
    template_name = 'DeleteGame.html'
    success_url = reverse_lazy('home')

class GameEdit(UpdateView):
    model = models.Product
    form_class = Purchased
    template_name = 'EditGame.html'
    success_url = reverse_lazy('home')