from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class Contact(models.Model):
    user_from = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rel_from_set"
    )
    user_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rel_to_set"
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user_from} follows {self.user_to}"

user_model = get_user_model()
user_model.add_to_class(
    'following',
    models.ManyToManyField(
        'self',
        through=Contact,
        symmetrical=False,
        blank=True
    )
)

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to="images/%Y/%m/%d",blank=True, null=True)

    def __str__(self):
        return self.user.username
