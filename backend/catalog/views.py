from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Piano
from .serializers import PianoSerializer


class PianoListAPIView(generics.ListAPIView):
    queryset = Piano.objects.filter(is_published=True)
    serializer_class = PianoSerializer


class PianoDetailAPIView(generics.RetrieveAPIView):
    queryset = Piano.objects.filter(is_published=True)
    serializer_class = PianoSerializer
    lookup_field = "slug"
