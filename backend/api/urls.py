from django.urls import path
from .views import PriceFeedView

urlpatterns = [
    path('price-feeds/', PriceFeedView.as_view(), name='price-feeds'),
]