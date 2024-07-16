from django.contrib import admin
from .models import Course, Rating

# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
  list_display = ['title', 'url', 'created_at', 'updated_at', 'active']

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
  list_display = ['course', 'name', 'email', 'grade', 'created_at', 'updated_at', 'active']