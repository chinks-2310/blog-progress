from graphene import ObjectType
import graphene
from graphene_django import DjangoObjectType
from core import models


class BlogType(ObjectType):
    id = graphene.ID()
    blog_title = graphene.String()


class ResourceUserProgressType(ObjectType):
    resource_id = graphene.ID()
    resource_type = graphene.String()
    resource_link = graphene.String()
    resource_text = graphene.String()
    resource_status = graphene.Boolean()
    resource_progress_percentage = graphene.Decimal()


class BlogProgressOfUserType(ObjectType):
    blog_id = graphene.ID()
    blog_title = graphene.String()
    blog_status = graphene.Boolean()
    blog_progress_percentage = graphene.Decimal()
    resources = graphene.List(ResourceUserProgressType)


class ResourcesType(ObjectType):
    resource_id = graphene.ID()
    resource_type = graphene.String()
    resource_link = graphene.String()
    resource_text = graphene.String()
    resource_progress_percentage = graphene.Decimal()


class BlogDetailsType(ObjectType):
    blog_id = graphene.ID()
    blog_title = graphene.String()
    blog_published_date = graphene.String()
    is_enrolled_in_blog = graphene.Boolean()
    blog_progress_percentage = graphene.Decimal()
    blog_status = graphene.Boolean()
    resources = graphene.List(ResourcesType)
