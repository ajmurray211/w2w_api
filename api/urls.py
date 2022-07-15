from django.urls import path
from .views.Fishs import FishsView, FishView

urlpatterns = [
    path('fish/', FishsView.as_view(), name = "Fish"),
    path('fish/<int:pk>', FishView.as_view(), name = 'Fish')
]