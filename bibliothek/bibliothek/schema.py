import graphene
import bib.schema

class Mutation(bib.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(mutation=Mutation)