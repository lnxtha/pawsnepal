from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView
from .models import Blog, Pets
from .models import ITEM_CATEGORIES, BLOG_CATEGORIES
from django.db.models import Q

item_categories = dict(ITEM_CATEGORIES)
blog_categories = dict(BLOG_CATEGORIES)

# Get key from dictionary Blog
get_key_for_blog = lambda value: [key for key in blog_categories.keys() if blog_categories[key] == value]

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        context = {'blogs': Blog.objects.all()[:4],  'blog_categories':blog_categories, 'featured_products': Pets.objects.filter(Q(featured__in = [1,2,3])).order_by('featured') }
        return render(request, template_name, context)


class BlogDetailView(DetailView):
    template_name = 'blogdetail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_categories'] = item_categories.values()
        context['blog_categories'] = blog_categories.values()

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

        related_blog_posts = sorted(post_dictionary.keys(), key=lambda kv: kv[1], reverse=True)

        context['related_posts'] = Blog.objects.filter(Q(title__in = related_blog_posts) & ~Q(id= self.kwargs['pk']))[:3]
        return context
        # FOR RELATED POSTS START ########


class BlogListView(ListView):
    template_name = 'bloglist.html'

    def get_queryset(self):

        object_list = Blog.objects.all()

        if self.request.GET.getlist('category'):

            selected_category = get_key_for_blog(self.request.GET.getlist('category')[0])
            object_list = Blog.objects.filter(Q(category=selected_category[0]))

            if object_list :
                pass
            else:
                print('Query returned No Matches')
                object_list = Blog.objects.all()

        elif self.request.GET.getlist('keyword'):
            print('Here in Keyword Section')
            keyword = self.request.GET.getlist('keyword')[0]

            object_list = Blog.objects.filter( Q(title__icontains=keyword) | Q(tags__icontains=keyword))

            if object_list:
                pass
            else:
                print('Query returned No Matches')
                object_list = Blog.objects.all()

        else:
            object_list = Blog.objects.all()

        return object_list

