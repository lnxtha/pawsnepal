from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from .models import Blog
from .models import ITEM_CATEGORIES, BLOG_CATEGORIES
from django.db.models import Q

import operator

item_categories = dict(ITEM_CATEGORIES)
blog_categories = dict(BLOG_CATEGORIES)


# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        context = {'blogs': Blog.objects.all()[:4],  'blog_categories':blog_categories }
        return render(request, template_name, context)


class BlogDetailView(DetailView):
    template_name = 'blogdetail.html'
    model = Blog


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_categories'] = item_categories.values()
        context['blog_categories'] = blog_categories.values()

        # print(self.kwargs['pk'])

        # FOR RELATED POSTS START ########
        related_posts = Blog.objects.raw(
            'select distinct id as id, tags as tags from pawsnepal_app_blog where id = '+str(self.kwargs['pk']))
        tags = related_posts[0].tags.split('#')
        tags = [i.replace(' ','') for i in tags]
        tags.remove('')
        related_blog_posts = []
        for i in tags:
            [related_blog_posts.append(i.title) for i in Blog.objects.filter(tags__contains=i)]

        post_dictionary = {}
        for i in related_blog_posts:
            post_dictionary[i] = related_blog_posts.count(i)

        related_blog_posts = sorted(post_dictionary.keys(), key=lambda kv: kv[1], reverse=True)[:3]

        context['related_posts'] = Blog.objects.filter(Q(title__in = related_blog_posts) & ~Q(id= self.kwargs['pk']))
        return context
        # FOR RELATED POSTS START ########


