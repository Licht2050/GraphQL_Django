from operator import mod
from pyexpat import model
from turtle import title
from django.db import models




class Author(models.Model):
    name = models.CharField(max_length=100)
    vorname = models.CharField(max_length=100)
    


class Book(models.Model):

    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True)


    def __str__(self):
        return self.title