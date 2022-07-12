import graphene
from graphene_django import DjangoObjectType

from bib.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book

class Query(graphene.ObjectType):
    all_books =  graphene.List(BookType)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

class InsertBook(graphene.Mutation):
    book = graphene.Field(BookType)

    class Arguments:
        id = graphene.ID()
        title = graphene.String()
        author = graphene.String()

    def mutate(self, info, title, author):
        bk = Book(title=title, author=author)
        bk.save()
        return InsertBook(book=bk)

class Mutation(graphene.ObjectType):
    insert_book = InsertBook.Field()
