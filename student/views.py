'''
Author: Lone
Date: 2020-11-28 16:24:50
LastEditTime: 2020-11-28 18:17:14
FilePath: /many2many/student/views.py
'''
from rest_framework.response import Response
from student.serializers import CourseSerializer, StudentSerializer
from student.models import Course, Student
from django.shortcuts import render
from django.forms.models import model_to_dict

# Create your views here.
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        print(serializer.data)
        res = []
        for data in serializer.data:
            courses = Course.objects.filter(id__in=data['courses'])
            print(f"courses: {courses}")
            tmp = []
            for course in courses:
                tmp.append(model_to_dict(course))
            data['courses'] = tmp
            res.append(data)
            
        return Response(res)
    
    

class CourseViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer