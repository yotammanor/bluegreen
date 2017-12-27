from django.db import models
from core.blue_green_utils import is_migration_applied


class ChapterManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
