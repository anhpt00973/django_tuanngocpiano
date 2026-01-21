from django.urls import path
from .views import PianoListAPIView, PianoDetailAPIView

urlpatterns = [
    path("pianos/", PianoListAPIView.as_view()),
    path("pianos/<slug:slug>/", PianoDetailAPIView.as_view()),
]
