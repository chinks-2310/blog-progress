from decimal import Decimal
import graphene

from core.models import Blog, BlogStatus, Resource, ResourceStatus
from . import inputs
import logging
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)


class UpdateResouceProgress(graphene.Mutation):
    ok = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        user_id = graphene.ID(required=True)
        blog_id = graphene.ID(required=True)
        resource_id = graphene.ID(required=True)
        progress_percentage = graphene.Decimal(required=True)

    def mutate(self, info, **kwargs):
        try:
            blog_id = kwargs.get("blog_id")
            user_id = kwargs.get("user_id")
            resource_id = kwargs.get("resource_id")
            progress_percentage = kwargs.get("progress_percentage")
            resource_status = ResourceStatus.objects.get(
                blog__id=blog_id, resource__id=resource_id, user__id=user_id
            )
            blog_status = BlogStatus.objects.get(blog__id=blog_id, user__id=user_id)
            resource_status.progress_percentage = progress_percentage
            resource_status.is_completed = True
            resource_status.save()
            resources = ResourceStatus.objects.filter(blog__id=blog_id)
            completed_resources = ResourceStatus.objects.filter(
                blog__id=blog_id, is_completed=True
            )
            blog_progress_percentage = Decimal(
                (len(completed_resources) * 100) / len(resources)
            )
            blog_status.progress_percentage = blog_progress_percentage
            blog_status.save()
            logger.info("Resource Progress updated successfully")
            return {
                "ok": True,
                "message": "Resource Progress updated successfully",
            }

        except Exception as e:
            logger.exception(e)
            return {
                "ok": False,
                "message": "Something went wrong while updating the resource progress",
            }


class UpdateBlogProgress(graphene.Mutation):
    ok = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        user_id = graphene.ID(required=True)
        blog_id = graphene.ID(required=True)
        progress_percentage = graphene.Decimal(required=True)

    def mutate(self, info, **kwargs):
        try:
            blog_id = kwargs.get("blog_id")
            user_id = kwargs.get("user_id")
            progress_percentage = kwargs.get("progress_percentage")
            blog_status = BlogStatus.objects.get(blog__id=blog_id, user__id=user_id)
            blog_status.progress_percentage = progress_percentage
            if progress_percentage == Decimal(100):
                blog_status.is_completed = True
            blog_status.save()
            logger.info("Blog Progress updated successfully")
            return {
                "ok": True,
                "message": "Blog Progress updated successfully",
            }

        except Exception as e:
            logger.exception(e)
            return {
                "ok": False,
                "message": "Something went wrong while updating the blog progress",
            }


class EnrollInBlog(graphene.Mutation):
    ok = graphene.Boolean()
    message = graphene.String()

    class Arguments:
        user_id = graphene.ID(required=True)
        blog_id = graphene.ID(required=True)

    def mutate(self, info, **kwargs):
        try:
            blog_id = kwargs.get("blog_id")
            blog = Blog.objects.get(id=blog_id)
            user_id = kwargs.get("user_id")
            user = User.objects.get(id=user_id)
            blog_status = BlogStatus(
                is_completed=False, progress_percentage=Decimal(0), blog=blog, user=user
            )
            blog_status.save()
            logger.info("Blog status created successfully")
            resources = Resource.objects.filter(blog__id=blog_id)
            resource_object_to_create = []
            for resource in resources:
                reso = ResourceStatus(blog=blog, user=user, resource=resource)
                resource_object_to_create.append(reso)
            ResourceStatus.objects.bulk_create(resource_object_to_create)
            logger.info("Resource status created successfully")
            logger.info("Enrolled in a blog successfully")
            return {
                "ok": True,
                "message": "Enrolled in a blog successfully",
            }

        except Exception as e:
            logger.exception(e)
            return {
                "ok": False,
                "message": "Something went wrong while enrolling in the blog",
            }


class Mutation(graphene.ObjectType):
    update_resource_progress = UpdateResouceProgress.Field()
    enroll_in_blog = EnrollInBlog.Field()
    update_blog_progress = UpdateBlogProgress.Field()
