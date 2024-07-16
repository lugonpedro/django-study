from django.urls import path
from .views import CoursesAPIView, RatingsAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('ratings/', RatingsAPIView.as_view(), name='ratings')
]
