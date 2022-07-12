import graphene
import bib.schema

class Mutation(bib.schema.Mutation, graphene.ObjectType):
    pass

class Query(bib.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query = Query, mutation=Mutation)