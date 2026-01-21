from django.apps import AppConfig
from django.contrib.auth import get_user_model


def create_admin():
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="admin", email="admin@gmail.com", password="admin"
        )


class CatalogConfig(AppConfig):
    name = "catalog"

    def ready(self):
        create_admin()
