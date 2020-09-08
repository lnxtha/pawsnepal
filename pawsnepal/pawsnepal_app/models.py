from django.db import models

# Create your models here.
ITEM_CATEGORIES = (
    (1,'Pet Food'),
    (2,'Pet Accessories'),
    (3,'Dog Heal')
)

BLOG_CATEGORIES = (
    (1,'Dog'),
    (2,'Dog Food'),
    (3,'Vetenirarian'),
    (4,'Events')
)

FEATURED_PRODUCTS = (
    (1,'Crown'),
    (2,'Diamond'),
    (3,'Platinum'),
    (4,'Gold'),
    (5,'Silver'),
    (6,'Bronze')
)




class Category(models.Model):
    items = models.CharField(max_length=100)
    blogs = models.CharField(max_length=100)


class Pets(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(null=True,blank = True,max_length=100)
    size = models.CharField(null=True, blank = True, max_length=50)
    price = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    featured = models.IntegerField(choices=FEATURED_PRODUCTS, null = True, blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pets"


class PetItems(models.Model):
    name = models.CharField(max_length=100)
    category = models.IntegerField(choices=ITEM_CATEGORIES)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField()         # Mandatory

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Pet Items"


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    banner_image = models.ImageField()  # Mandatory
    logo = models.ImageField()
    added_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


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