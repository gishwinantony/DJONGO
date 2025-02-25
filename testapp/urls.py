from django.urls import path
from .views import MapUrlAPIView,FindUrlAPIView,Homepage

urlpatterns = [
    path('map',MapUrlAPIView.as_view ()),
    path('find/<str:key>',FindUrlAPIView.as_view()),
    path('',Homepage.homepage_view)
]
