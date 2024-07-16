from rest_framework import serializers
from .models import Course, Rating

class CourseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Course
    fields = {
      'id',
      'title',
      'url',
      'created_at',
      'updated_at',
      'active'
    }

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    extra_kwargs = {
      'email': {'write_only': True}
    }
    model = Rating
    fields = {
      'id',
      'course',
      'name',
      'email',
      'comment',
      'grade',
      'created_at',
      'updated_at',
      'active'
    }