from django.shortcuts import get_object_or_404
from rest_framework import generics
from .models import Course, Rating
from .serializers import CourseSerializer, RatingSerializer
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

# API V1
class CoursesAPIView(generics.ListCreateAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

class RatingsAPIView(generics.ListCreateAPIView):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer

  def get_queryset(self):
    if self.kwargs.get('course_pk'):
      return super().get_queryset().filter(course_id = self.kwargs.get('course_pk'))
    return self.queryset.all()

class RatingAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer

  def get_object(self):
    if self.kwargs.get('course_pk'):
      return get_object_or_404(
        self.get_queryset(), course_id = self.kwargs.get('course_pk'), pk = self.kwargs.get('rating_pk'))
    return super().get_object()

# API V2
class CourseViewSet(viewsets.ModelViewSet):
  queryset = Course.objects.all()
  serializer_class = CourseSerializer

  @action(detail=True, methods=['get'])
  def ratings(self, request, pj=None):
    course = self.get_object()
    serializer = RatingSerializer(course.ratings.all(), many=True)
    return Response(serializer.data)
  
# VIEWSET PADRÃO
# class RatingViewSet(viewsets.ModelViewSet):
#   queryset = Rating.objects.all()
#   serializer_class = RatingSerializer

# VIEWSET CUSTOMIZADO
class RatingViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
  queryset = Rating.objects.all()
  serializer_class = RatingSerializer