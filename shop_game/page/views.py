from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import get_object_or_404
from . import models
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import Personal_area

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

class Buy_item(LoginRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'buy_item.html'
    success_url = reverse_lazy('home')
    login_url = 'login'
    def index1(request):
        model = models.Product
        users = model.objects.filter(user=request.user.id).all()
        return render(request, "personal_area.html", {"users": users})

