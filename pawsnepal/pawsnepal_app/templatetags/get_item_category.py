from django import template
from ..models import ITEM_CATEGORIES, BLOG_CATEGORIES, Blog

item_categories = dict(ITEM_CATEGORIES)
blog_categories = dict(BLOG_CATEGORIES)

register = template.Library()


@register.simple_tag(name='get_item_category')
def get_item_category(key):
    return item_categories[int(key)]


@register.simple_tag(name='get_blog_category')
def get_blog_category(key):
    try:
        return blog_categories[int(key)]
    except:
        return 'NULL'




@register.simple_tag(name='get_blog_count')
def get_blog_count(category):
    blog_key_list = list(blog_categories.keys())
    blog_value_list = list(blog_categories.values())
    #print(Blog.objects.filter(category=blog_key_list[blog_value_list.index(category)]).count())
    return Blog.objects.filter(category=blog_key_list[blog_value_list.index(category)]).count()


