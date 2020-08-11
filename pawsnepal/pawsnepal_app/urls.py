from django.urls import path, include
from .views import *


app_name = 'pawsnepal_app'
urlpatterns = [
    path('', HomeView.as_view(), name='dashboard-home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]