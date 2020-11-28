'''
Author: Lone
Date: 2020-11-28 16:44:20
LastEditTime: 2020-11-28 18:37:53
FilePath: /many2many/student/serializers.py
'''
from django.core.validators import validate_integer
from rest_framework import serializers
from .models import Course, Student


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'id')

class StudentSerializer(serializers.ModelSerializer):
    course_ids = serializers.ListField(write_only=True, required=False)
    
    class Meta:
        model = Student
        fields = ('name', 'course_ids', 'courses', 'id')
        extra_kwargs = {'courses': {'read_only': True}}
        
    def create(self, validated_data):
        ids = None
        if validated_data.get('course_ids'):
            ids = validated_data.pop('course_ids')
        student = Student.objects.create(**validated_data)
        if ids:
            courses = Course.objects.filter(id__in=ids)
            student.courses.add(*courses)
        return student
    
    def update(self, instance, validated_data):
        ids = None
        if validated_data.get('course_ids'):
            ids = validated_data.pop('course_ids')
        if ids:
            courses = Course.objects.filter(id__in=ids)
            instance.courses.clear()
            instance.courses.add(*courses)
        instance.name = validated_data.get('name', instance.name)
        return instance