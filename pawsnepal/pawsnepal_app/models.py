from django.db import models

# Create your models here.
ITEM_CATEGORIES = (
    (1,'Dog Breed'),
    (2,'Pet Essentials'),
    (3,'Pet Accessories')
)

BLOG_CATEGORIES = (
    (1,'Dog'),
    (2,'Dog Food'),
    (3,'Vetenirarian'),
    (4,'Events')
)

FEATURED_PRODUCTS = (
    (1,'One'),
    (2,'Two'),
    (3,'Three'),
    (4,'Four'),
    (5,'Five'),
    (6,'Six')
)


class Category(models.Model):
    items = models.CharField(max_length=100)
    blogs = models.CharField(max_length=100)


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    banner_image = models.ImageField()  # Mandatory
    logo = models.ImageField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# class Pets(models.Model):
#     name = models.CharField(max_length=100)
#     type = models.CharField(null=True,blank = True,max_length=100)
#     size = models.CharField(null=True, blank = True, max_length=50)
#     price = models.FloatField(null=True, blank=True)
#     description = models.TextField(null=True, blank=True)
#     added_date = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     image = models.ImageField(null=True, blank=True)
#     featured = models.IntegerField(choices=FEATURED_PRODUCTS, null = True, blank=True, unique=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = "Pets"


class PetItems(models.Model):
    name = models.CharField(max_length=100)
    category = models.IntegerField(choices=ITEM_CATEGORIES)
    label = models.CharField(max_length=50, null= True, blank = True)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    price_range = models.CharField(max_length=20, null=True, blank = True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()         # Mandatory
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name = 'brand_name', blank = True, null = True)
    featured = models.IntegerField(choices=FEATURED_PRODUCTS, null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pet Items"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    introduction = models.CharField(max_length=150, null=True)  # Mandatory
    post = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()            # Mandatory
    created_by = models.CharField(max_length=100, null=True, blank=True)
    category = models.IntegerField(choices=BLOG_CATEGORIES)
    tags = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blogs Posts"
        ordering = ['-added_date']


class ContactUs(models.Model):
    firstname = models.CharField(max_length=100)    # Mandatory
    lastname = models.CharField(max_length=100)     # Mandatory
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=100)
    message = models.TextField()                # Mandatory
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name_plural = "Blogs Posts"


class Gallery(models.Model):
    image = models.ImageField()    # Mandatory
    caption = models.CharField(max_length=150, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)