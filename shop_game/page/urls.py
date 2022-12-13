from django.urls import path
from . import views

urlpatterns =[
    path('', views.HomePageView.as_view(), name='home'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('product/<int:pk>/buy_item', views.Buy_item.as_view(), name='buy_item'),
    path('add_game/', views.Add_game.as_view(), name='Add_game'),
    path('<int:pk>/GameDelete', views.GameDelete.as_view(), name='DeleteGame'),
    path('<int:pk>/EditGame', views.GameEdit.as_view(), name='GameEdit'),
]