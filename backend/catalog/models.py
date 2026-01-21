from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Piano(models.Model):
    CONDITION_CHOICES = (
        ("new", "New"),
        ("used", "Used"),
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)

    short_description = models.TextField(blank=True)
    description = RichTextField()

    youtube_url = models.URLField(blank=True, null=True)

    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="pianos")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name="pianos"
    )

    price = models.IntegerField()
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class PianoImage(models.Model):
    piano = models.ForeignKey(Piano, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="pianos/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.piano.name} - Image {self.id}"
