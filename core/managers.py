from django.db import models
from core.blue_green_utils import is_migration_applied


class ChapterManager(models.Manager):
    def get_queryset(self):
        if is_migration_applied():
            return super().get_queryset().defer("number")
        return super().get_queryset()
