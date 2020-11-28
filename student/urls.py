'''
Author: Lone
Date: 2020-11-28 17:00:10
LastEditTime: 2020-11-28 18:15:25
FilePath: /many2many/student/urls.py
'''
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from student import views

router = DefaultRouter()
router.register(r'students', views.StudentViewSet)
router.register(r'courses', views.CourseViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]