from django.urls import path
from .views import CoursesAPIView, CourseAPIView, RatingsAPIView, RatingAPIView

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    path('ratings/<int:pk>', RatingAPIView.as_view(), name='rating')
]
