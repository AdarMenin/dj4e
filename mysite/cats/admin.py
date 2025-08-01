from django.contrib import admin
from cats.models import Breed, Cat

# Register your models here.
admin.site.register([Cat, Breed])
