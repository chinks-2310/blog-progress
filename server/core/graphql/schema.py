import graphene

from core.graphql.mutations import Mutation as coreMutation
from core.graphql.query import Query as coreQuery


class Query(coreQuery, graphene.ObjectType):
    pass


class Mutation(coreMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
