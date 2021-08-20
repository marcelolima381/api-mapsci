from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def fields(request):
    return Response(
        [
            ['Machine Learning', 0.54389],
            ['Recommendation Systems', 0.14389],
            ['Network Systems', 0.24389],
            ['Robotics', 0.34389],
            ['Discrete Mathematics', 0.44389],
            ['Computational Geometry', 0.64389],
            ['Graphs Theory', 0.74389],
        ]
    )