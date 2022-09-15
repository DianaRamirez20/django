from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "Seed admin user"

    def handle(self, *args, **options):
        admin_email = "admin@admin.com"

        if User.objects.filter(email=admin_email).exists():
            return

        User.objects.create_superuser(
            username="diana",
            email=admin_email,
            password="diana",
        )
