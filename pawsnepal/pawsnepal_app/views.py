from django.shortcuts import render
from django.views import View

from django.views.generic import DetailView, ListView
from .models import Blog, PetItems, Brand
from .models import ITEM_CATEGORIES, BLOG_CATEGORIES
from django.db.models import Q

item_categories = dict(ITEM_CATEGORIES)
blog_categories = dict(BLOG_CATEGORIES)

# Get key from dictionary Blog
get_key_for_blog = lambda value: [key for key in blog_categories.keys() if blog_categories[key] == value]

# Get key from dictionary Item
get_key_for_item = lambda value: [key for key in item_categories.keys() if item_categories[key] == value]

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        context = {'blogs': Blog.objects.all()[:4],
                   'item_categories': item_categories.values(),
                   'blog_categories':blog_categories,
                   'brand_list': Brand.objects.all(),
                   'featured_products': PetItems.objects.filter(Q(featured__in = [1,2,3])).order_by('featured') ,
                   'pet_items': PetItems.objects.all()[:6]}

        return render(request, template_name, context)


class BlogDetailView(DetailView):
    template_name = 'blogdetail.html'
    model = Blog

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['item_categories'] = item_categories.values()
        context['blog_categories'] = blog_categories.values()
        context['brand_list'] = Brand.objects.all()

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
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_searched_result'] = ''
        return context

    def get_queryset(self):

        object_list = Blog.objects.all()

        if self.request.GET.getlist('category'):
            selected_category = get_key_for_blog(self.request.GET.getlist('category')[0])
            object_list = Blog.objects.filter(Q(category=selected_category[0]))

            if object_list :
                pass
            else:
                print('Query returned No Matches')
                self.context['is_searched_result'] = 'None'
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


class Shop(ListView):
    template_name = 'shop.html'
    model = PetItems

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_searched_result'] = ''

        context['item_categories'] = item_categories.values()
        context['blog_categories'] = blog_categories.values()
        context['brand_list'] = Brand.objects.all()

        return context

    def get_queryset(self):
        object_list = PetItems.objects.all()
        if self.request.GET.getlist('category'):
            selected_category = get_key_for_item(self.request.GET.getlist('category')[0])
            print('Here in Category Section')
            object_list = PetItems.objects.filter(Q(category=selected_category[0]))

        elif self.request.GET.getlist('brand'):
            print('Here in Brand section')
            brand = Brand.objects.get(name = self.request.GET.getlist('brand')[0])
            PetItems.objects.filter(brand = brand)
            object_list = PetItems.objects.filter(brand = brand)

        elif self.request.GET.getlist('search_item_keyword'):
            print('Here in Search Section')
            keyword = self.request.GET.getlist('search_item_keyword')[0]
            object_list = PetItems.objects.filter(Q(name__icontains=keyword) | Q(name__icontains=keyword))

        if self.request.GET.getlist('reference'):
            if self.request.GET.getlist('reference')[-1] == 'name-a-to-z':
                print('Here in Reference Section')
                object_list = object_list.order_by('name')

            elif self.request.GET.getlist('reference')[-1] == 'name-z-to-a':
                print('Here in Reference Section')
                object_list = object_list.order_by('-name')

            elif self.request.GET.getlist('reference')[-1] == 'price-low-to-high':
                print('Here in Reference Section')
                object_list = object_list.order_by('price')

            elif self.request.GET.getlist('reference')[-1] == 'price-high-to-low':
                print('Here in Reference Section')
                object_list = object_list.order_by('-price')

        return object_list





