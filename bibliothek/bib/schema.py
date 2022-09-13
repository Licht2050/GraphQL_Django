import graphene
import bib_graphql.schema


class Query(bib_graphql.schema.Query, graphene.ObjectType):
    pass
class Mutation(bib_graphql.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)