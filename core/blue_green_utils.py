from django.db.migrations.recorder import MigrationRecorder


def is_migration_applied():
    return MigrationRecorder.Migration.objects.filter(
        name__contains="remove_chapter_number").exists()
