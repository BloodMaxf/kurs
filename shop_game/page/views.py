from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView,TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import Purchased

class HomePageView(ListView):
    model = models.Product
    template_name = 'home.html'
    paginate_by = 8

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'


class SearchResultsView(ListView):
    model = models.Product

    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = models.Product.objects.filter(
            Q(title__icontains=query) | Q(group__icontains=query)
        )
        return object_list

class Buy_item(LoginRequiredMixin, DetailView):
    model = models.Product
    template_name = 'buy_item.html'
    login_url = 'login'
    def post(self, request, pk):
        models.Purchased_products.objects.create(title=models.Product.objects.get(title=request.POST.get('title')), key=models.Product.objects.get(key=request.POST.get('key')), user_id=request.user)
        instance = models.Product.objects.get(pk=pk)
        instance.delete()
        return HttpResponseRedirect(request.META.get('HTTP_ORIGIN') + f'/users/personal_area/{request.user.pk}')

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