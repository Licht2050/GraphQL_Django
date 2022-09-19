from dataclasses import fields
from unicodedata import name
from bib_graphql.models import Author
import graphene
from graphene_django import DjangoObjectType

from bib_graphql.models import Book


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"
class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"

#Queries
class Query(graphene.ObjectType):
    all_books =  graphene.List(BookType)
    all_authors = graphene.List(AuthorType)
    book_by_id = graphene.Field(BookType, book_id=graphene.Int())
    # book_by_name = graphene.Field(BookType, name=graphene.)
    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()
    def resolve_all_authors(self, info, **kwargs):
        return Author.objects.all()
    def resolve_book_by_id(self, info, book_id):
        return Book.objects.get(pk=book_id)


#Mutations
class CreateAuthor(graphene.Mutation):
    author = graphene.Field(AuthorType)
    class Arguments:
        name = graphene.String()
        vorname = graphene.String()
    def mutate(self, info, name, vorname):
        at = Author(name=name, vorname=vorname)
        at.save()
        return CreateAuthor(author=at)

class UpdateAuthor(graphene.Mutation):
    author = graphene.Field(AuthorType)
    class Arguments:
        author_id = graphene.Int()
        name = graphene.String()
        vorname = graphene.String()
    def mutate(self, info, author_id, name, vorname):
        at = Author.objects.get(id=author_id)
        at.name = name
        at.vorname = vorname
        return UpdateAuthor(author=at)

class CreateBook(graphene.Mutation):
    book = graphene.Field(BookType)
    author = graphene.List(AuthorType)
    class Arguments:
        titel = graphene.String()
        author_id = graphene.Int()
    def mutate(self, info, titel, author_id):
        at = Author.objects.get(id=author_id)
        bk = Book(titel=titel)
        bk.save()
        bk.authors.add(at)
        return CreateBook(book=bk)

class UpdateBook(graphene.Mutation):
    book = graphene.Field(BookType)
    author = graphene.List(AuthorType)
    class Arguments:
        book_id =  graphene.Int()
        titel = graphene.String()
    def mutate(self, info, book_id, titel):
        bk = Book.objects.get(id=book_id)
        bk.titel = titel
        bk.save()
        return UpdateBook(book=bk)   

class InputAuthorToBook(graphene.Mutation):
    book = graphene.Field(BookType)
    author = graphene.List(AuthorType)
    class Arguments:
        book_id =  graphene.Int()
        author_id = graphene.Int()
    def mutate(self, info, book_id, author_id):
        at = Author.objects.get(id=author_id)
        bk = Book.objects.get(id=book_id)
        bk.authors.add(at)
        return InputAuthorToBook(book=bk)

class RemoveAuthorFromBook(graphene.Mutation):
    book = graphene.Field(BookType)
    author = graphene.List(AuthorType)
    class Arguments:
        book_id =  graphene.Int()
        author_id = graphene.Int()
    def mutate(self, info, book_id, author_id):
        bk = Book.objects.get(id=book_id)
        for at in bk.authors.all():
            if at.id == author_id:
                bk.authors.remove(at)
        return RemoveAuthorFromBook(book=bk)

class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    create_author = CreateAuthor.Field()
    input_author_to_book = InputAuthorToBook.Field()
    remove_author_from_book = RemoveAuthorFromBook.Field()
    update_book = UpdateBook.Field()
    update_author = UpdateAuthor.Field()