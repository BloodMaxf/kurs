from django.urls import path
from . import views


urlpatterns =[
    path('signup/', views.Signup.as_view(), name='signup'),
    path('personal_area/<int:pk>/', views.Personal.as_view(), name='personal_area'),
]