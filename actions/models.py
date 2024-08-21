from django.conf import settings
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Action(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="actions"
    )
    verb = models.CharField(max_length=155)
    created = models.DateTimeField(auto_now_add=True)
    target_ct = models.ForeignKey(
        ContentType,
        blank=True,
        null=True,
        related_name="target_obj",
        on_delete=models.CASCADE
    )
    target_id = models.PositiveSmallIntegerField(blank=True, null=True)
    target = GenericForeignKey("target_ct", "target_id")
    
    def __str__(self):
        return 
