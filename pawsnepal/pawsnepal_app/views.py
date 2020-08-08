from django.shortcuts import render
from django.views import View

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name  = 'index.html'
        return render(request, template_name, {'':''})
