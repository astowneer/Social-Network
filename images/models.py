from django.urls import reverse
from django.db import models
from django.conf import settings

class Image(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="images"
    )
    title = models.CharField(max_length=155)
    description = models.TextField(blank=True)
    url = models.URLField(max_length=1000)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    created = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        blank=True,
        related_name="image_likes"
    )

    def get_absolute_url(self):
        return reverse("images:detail", args=[self.id])

    def __str__(self):
        return self.title