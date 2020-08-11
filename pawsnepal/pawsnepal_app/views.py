from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Blog
from .models import ITEM_CATEGORIES, BLOG_CATEGORIES

item_categories = dict(ITEM_CATEGORIES)
blog_categories = dict(BLOG_CATEGORIES)


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        context = {'blogs': Blog.objects.all()[:4],  'blog_categories':blog_categories }
        print(item_categories)
        print('*'*20)
        return render(request, template_name, context)


class BlogDetailView(DetailView):
    template_name = 'blogdetail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_categories'] = item_categories.values()
        context['blog_categories'] = blog_categories.values()
        return context

