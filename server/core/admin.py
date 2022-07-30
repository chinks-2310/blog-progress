from django.contrib import admin

from core.models import Blog, BlogStatus, Resource, ResourceStatus

# Register your models here.


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    list_display = ("id", "blog_title", "published_date")
    search_fields = ("blog_title",)


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "resource_type",
        "resource_link",
        "blog",
    )
    search_fields = ("resource_type", "blog__id", "blog__blog_title")
    list_filter = ("resource_type",)


@admin.register(BlogStatus)
class BlogStatusAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "is_completed",
        "progress_percentage",
        "blog",
    )
    search_fields = (
        "blog__id",
        "blog__blog_title",
    )
    list_filter = ("is_completed",)


@admin.register(ResourceStatus)
class ResourceStatusAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "is_completed",
        "progress_percentage",
        "resource",
        "blog",
    )
    search_fields = (
        "resource__resource_type",
        "blog__id",
        "blog__blog_title",
        "resource__id",
    )
    list_filter = ("resource__resource_type", "is_completed")
