from django.conf.urls import url
from . import views



urlpatterns = [
    url(r' ', views.GetLikeRateAPIView, name='GetLikeRateAPIView'),
    url(r' ', views.GetLikeAboveRateAPIView, name='GetLikeAboveRateAPIView'),
    url(r' ', views.GetLikeBelowRateAPIView, name='GetLikeBelowRateAPIView'),
    url(r' ', views.GetLikesAPIView, name='GetLikesAPIView')
]