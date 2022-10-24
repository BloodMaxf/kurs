
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm, UserPersonalArea

class Signup(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class Personal(generic.CreateView):
    form_class = UserPersonalArea
    template_name = 'personal_area.html'