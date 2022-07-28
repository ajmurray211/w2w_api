from django.urls import URLPattern, path
from .views.fish import FishingView

urlpatterns = [
    path('fish/', FishingView.as_view(), name='Fish')
]