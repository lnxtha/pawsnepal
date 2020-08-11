from django.urls import path
from .views import *

app_name = 'pawsnepal_app'
urlpatterns = [
    path('', HomeView.as_view(), name='dashboard-home'),

]