from django.urls import URLPattern, path
from .views.fish import FishingView, FishView

urlpatterns = [
    path('fish/', FishingView.as_view(), name='Fish'),
    path('fish/<int:pk>', FishView.as_view(), name='Fish')
]