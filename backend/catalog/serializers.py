from rest_framework import serializers
from .models import Piano, PianoImage, Brand, Category


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class PianoImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PianoImage
        fields = ["id", "image", "order"]


class PianoSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    images = PianoImageSerializer(many=True, read_only=True)

    class Meta:
        model = Piano
        fields = [
            "id",
            "name",
            "slug",
            "short_description",
            "description",
            "youtube_url",
            "brand",
            "category",
            "price",
            "condition",
            "is_published",
            "created_at",
            "updated_at",
            "images",
        ]
