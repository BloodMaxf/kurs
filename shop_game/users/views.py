from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from .models import Personal_area
from django.contrib.auth.mixins import LoginRequiredMixin

class Signup(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Personal(LoginRequiredMixin, ListView):
    model = Personal_area
    template_name = 'personal_area.html'
    login_url = 'login'

