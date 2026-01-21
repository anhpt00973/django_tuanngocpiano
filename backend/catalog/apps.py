from django.apps import AppConfig


class CatalogConfig(AppConfig):
    name = "catalog"

    def ready(self):
        # Import ở đây để tránh circular import
        # Chỉ chạy khi Django đã sẵn sàng
        try:
            from django.contrib.auth import get_user_model

            User = get_user_model()
            # Tự động tạo admin user nếu chưa tồn tại
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                    username="admin", email="admin@gmail.com", password="admin"
                )
                print("✅ Admin user created successfully!")
        except Exception as e:
            # Bỏ qua lỗi nếu database chưa sẵn sàng hoặc đã có user
            print(f"⚠️ Could not create admin user: {e}")
