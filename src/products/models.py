from django.db import models
import random, os
from django.db.models.signals import pre_save
from .util import unique_slug_generator
from django.urls import reverse
from django.db.models import Q
# Create your models here.
def get_filename_ext(filename):
    base_name = os.path.basename(filename)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 399239998)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename= new_filename, ext=ext)
    return 'products/{new_filename}/{final_filename}'.format(new_filename= new_filename, final_filename=final_filename)

class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True,  active=True)

    # def search(self, query):
    #     lookups = (Q(title__icontains=query) | 
    #               Q(description__icontains=query) |
    #               Q(price__icontains=query) |
    #               Q(tag__title__icontains=query)
    #               )
        # tshirt, t-shirt, t shirt, red, green, blue,
        # return self.filter(lookups).distinct()

class ProductManager(models.Manager):

    def featured(self): #Product.objects.featured() 
        return self.get_queryset().featured()

    def all(self):
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id= id)
        if qs.count() == 1:
            return qs.first()
        return None

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    # def search(self, query):
    #     return self.get_queryset().active().search(query)


GENDER_CHOICES = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)

RELATION_CHOICES = {
    ('brother', 'BROTHER'),
    ('sister', 'SISTER'),
    ('mom', 'MOM'),
    ('dad', 'DAD'),
    ('mom', 'MOM'),
    ('friend', 'FRIEND'),
    ('girl friend', 'GIRL FRIEND'),
    ('boy friend', 'BOY FRIEND'),
    ('other', 'OTHER'),
}

RELATION_CHOICES = {
    ('brother', 'BROTHER'),
    ('sister', 'SISTER'),
    ('mom', 'MOM'),
    ('dad', 'DAD'),
    ('mom', 'MOM'),
    ('friend', 'FRIEND'),
    ('girl friend', 'GIRL FRIEND'),
    ('boy friend', 'BOY FRIEND'),
    ('other', 'OTHER'),
}

INTRESTS_CHOICES = {
    ('tech', 'TECH'),
    ('traveling', 'TRAVELLING'),
    ('reading', 'READING'),
    ('art', 'ART'),
    ('music', 'MUSIC'),
    ('sports', 'SPORTS'),
    ('painting', 'PAINTING'),
    ('other', 'OTHER'),
}

class Product(models.Model):
    title           = models.CharField(max_length= 100)
    slug            = models.SlugField(blank=True, unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places = 2, max_digits= 10, default = 10) #null = True
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default= False)
    active          = models.BooleanField(default=True)
    timestamp       = models.DateTimeField(auto_now_add=True)
    minAge          = models.DecimalField(decimal_places=0, max_digits=100, default=5)
    maxAge          = models.DecimalField(decimal_places=0, max_digits=100, default=90)
    gender          = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    relation        = models.CharField(max_length=6, choices=RELATION_CHOICES, default='brother')
    intrests        = models.CharField(max_length=6, choices=INTRESTS_CHOICES, default='tech')
    occupation      = models.CharField(max_length=20, default='ALL')
    category        = models.CharField(max_length=20, default='ALL')
    

    objects = ProductManager()

    def get_absolute_url(self):
        # return "/products/{slug}/".format(slug=self.slug)
        return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)
