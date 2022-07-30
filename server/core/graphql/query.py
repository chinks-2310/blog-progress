import graphene
from . import types
from . import inputs
from . import resolvers


class Query(graphene.ObjectType):
    blog_progress = graphene.List(
        types.BlogProgressOfUserType,
        filtering=inputs.BlogProgressForUserInput(),
        resolver=resolvers.BlogProgressForUserResolver(),
    )
    blog_details = graphene.List(
        types.BlogDetailsType,
        filtering=inputs.BlogsForUserInput(),
        resolver=resolvers.BlogDetailsResolver(),
    )
