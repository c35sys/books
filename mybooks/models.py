from django.contrib import admin
from django.db import models

# Create your models here.


class Author(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)

    def __unicode__(self):
        return self.lastname
admin.site.register(Author)


class Book(models.Model):
    author = models.ForeignKey(Author)
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
admin.site.register(Book)
