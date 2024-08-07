from django.urls import path
from .views import CoursesAPIView, CourseAPIView, RatingsAPIView, RatingAPIView, RatingViewSet, CourseViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('courses/', CoursesAPIView.as_view(), name='courses'),
    path('courses/<int:pk>', CourseAPIView.as_view(), name='course'),
    path('courses/<int:pk>/ratings/', RatingsAPIView.as_view(), name='course_ratings'),
    path('courses/<int:pk>/ratings/<int:rating_id>', RatingsAPIView.as_view(), name='course_rating'),
    path('ratings/', RatingsAPIView.as_view(), name='ratings'),
    path('ratings/<int:rating_id>', RatingAPIView.as_view(), name='rating')
]
