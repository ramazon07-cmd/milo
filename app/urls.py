from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('post/<int:id>', post_detail, name='post_detail'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', CreateContactView.as_view(), name='contact'),
    path('posts/', posts, name='posts'),
    path('search/', search, name='search'),
]
