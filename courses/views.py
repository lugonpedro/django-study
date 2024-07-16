from rest_framework import generics
from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer

class CoursesAPIView(generics.ListCreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

# class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):

class RatingsAPIView(generics.ListCreateAPIView):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer

# class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):