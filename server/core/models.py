from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
RESOURCE_CHOICES = (
    ("Text", "Text"),
    ("Image", "Image"),
    ("Video", "Video"),
    ("PDF", "PDF"),
)


class Blog(models.Model):
    blog_title = models.TextField()
    published_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return self.blog_title


class Resource(models.Model):
    resource_type = models.CharField(max_length=256, choices=RESOURCE_CHOICES)
    resource_link = models.CharField(max_length=256, blank=True)
    resource_text = models.TextField(blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="resources")

    class Meta:
        verbose_name_plural = "Resources"

    def __str__(self):
        return f"{self.id}"


PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]


class BlogStatus(models.Model):
    is_completed = models.BooleanField(default=False)
    progress_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00, validators=PERCENTAGE_VALIDATOR
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Blog Status"
        unique_together = [["blog", "user"]]

    def __str__(self):
        return self.blog.blog_title


class ResourceStatus(models.Model):
    is_completed = models.BooleanField(default=False)
    progress_percentage = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00, validators=PERCENTAGE_VALIDATOR
    )
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Resource Status"
        unique_together = [["resource", "blog", "user"]]
