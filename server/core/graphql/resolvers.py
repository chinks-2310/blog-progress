from decimal import Decimal
from core.models import Blog, BlogStatus, Resource, ResourceStatus
from django.contrib.auth.models import User


class BlogProgressForUserResolver:
    def __call__(self, source, info, filtering={}):
        user_id = filtering.get("user_id")
        blog_id = filtering.get("blog_id")
        blogs = []
        if not blog_id:
            blog_status = BlogStatus.objects.filter(user__id=user_id)
        else:
            blog_status = BlogStatus.objects.filter(blog__id=blog_id, user__id=user_id)
        for status in blog_status:
            blogs.append(status.blog)
        result = []

        for i in range(0, len(blogs)):
            resources = Resource.objects.filter(blog=blogs[i])
            resource_array = []
            for j in range(0, len(resources)):
                resource_status = ResourceStatus.objects.get(
                    blog__id=blogs[i].id, resource__id=resources[j].id, user__id=user_id
                )
                resource = {
                    "resource_id": resources[j].id,
                    "resource_type": resources[j].resource_type,
                    "resource_link": resources[j].resource_link,
                    "resource_text": resources[j].resource_text,
                    "resource_status": resource_status.is_completed,
                    "resource_progress_percentage": resource_status.progress_percentage,
                }
                resource_array.append(resource)
            blog = {
                "blog_id": blogs[i].id,
                "blog_title": blogs[i].blog_title,
                "blog_status": blog_status[i].is_completed,
                "blog_progress_percentage": blog_status[i].progress_percentage,
                "resources": resource_array,
            }
            result.append(blog)
        return result


class BlogDetailsResolver:
    def __call__(self, source, info, filtering={}):
        user_id = filtering.get("user_id")
        blog_id = filtering.get("blog_id")
        if not blog_id:
            blogs = Blog.objects.all()
        else:
            blogs = Blog.objects.filter(id=blog_id)
        result = []

        for i in range(0, len(blogs)):
            resources = Resource.objects.filter(blog=blogs[i])
            blog_status = BlogStatus.objects.filter(
                blog__id=blogs[i].id, user__id=user_id
            )
            if len(blog_status) == 0:
                is_enrolled_in_blog = False
                blog_progress_percentage = Decimal(0)

            else:
                is_enrolled_in_blog = True
                blog_progress_percentage = blog_status[0].progress_percentage

            resource_array = []
            for j in range(0, len(resources)):
                if len(blog_status) != 0:
                    resource_status = ResourceStatus.objects.get(
                        blog=blogs[i], resource=resources[j], user__id=user_id
                    )
                    if not resource_status:
                        resource_progress_percentage = Decimal(0)

                    else:
                        resource_progress_percentage = (
                            resource_status.progress_percentage
                        )
                else:
                    resource_progress_percentage = Decimal(0)
                resource = {
                    "resource_id": resources[j].id,
                    "resource_type": resources[j].resource_type,
                    "resource_link": resources[j].resource_link,
                    "resource_text": resources[j].resource_text,
                    "resource_progress_percentage": resource_progress_percentage,
                }
                resource_array.append(resource)
            blog = {
                "blog_id": blogs[i].id,
                "blog_title": blogs[i].blog_title,
                "blog_published_date": blogs[i].published_date,
                "is_enrolled_in_blog": is_enrolled_in_blog,
                "blog_progress_percentage": blog_progress_percentage,
                "resources": resource_array,
            }
            result.append(blog)
        return result
