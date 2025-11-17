from django.urls import  path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path ('singlepage/<int:pk>/', views.singlepage, name='singlepage'),
    path ('post_like/<int:pk>/', views.post_like, name='like'),
    path ('post/search_results', views.search, name='search')
]
