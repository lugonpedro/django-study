from rest_framework import serializers
from .models import Course, Rating

class CourseSerializer(serializers.ModelSerializer):
  # Nested Relationship
  # ratings = RatingSerializer(many=True, read_only=True)

  # HyperLinked Related Field
  # ratings = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='rating-detail')

  # Primary Key Related Field
  ratings = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

  class Meta:
    model = Course
    fields = (
      'id',
      'title',
      'url',
      'created_at',
      'updated_at',
      'active',
      'ratings'
    )

class RatingSerializer(serializers.ModelSerializer):
  class Meta:
    extra_kwargs = {
      'email': {'write_only': True}
    }
    model = Rating
    fields = (
      'id',
      'course',
      'name',
      'email',
      'comment',
      'grade',
      'created_at',
      'updated_at',
      'active'
    )