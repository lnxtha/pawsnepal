from django.urls import path, include
from .views import *

app_name = 'pawsnepal_app'
urlpatterns = [
    path('', HomeView.as_view(), name='dashboard-home'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),

    path('blog/list/', BlogListView.as_view(), name='blog-list'),
]

# http://127.0.0.1:8000/blog/4/
# http://127.0.0.1:8000/blog/4/