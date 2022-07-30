import graphene


class BlogProgressForUserInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    blog_id = graphene.ID()


class BlogsForUserInput(graphene.InputObjectType):
    user_id = graphene.ID(required=True)
    blog_id = graphene.ID()
