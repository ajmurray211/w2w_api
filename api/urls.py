from django.urls import URLPattern, path
from .views.fish import FishingView, FishView
from .views.hunting import HuntingView, HuntView

urlpatterns = [
    path('fish/', FishingView.as_view(), name='Fish'),
    path('fish/<int:pk>', FishView.as_view(), name='Fish'),
    path('hunting/', HuntingView.as_view(), name='Hunting'),
    path('hunting/<int:pk>', HuntView.as_view(), name='Hunting')
]