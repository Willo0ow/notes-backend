from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
    SAFE_METHODS, 
    IsAuthenticated, 
    IsAuthenticatedOrReadOnly, 
    BasePermission, 
    IsAdminUser, 
    DjangoModelPermissions, 
    AllowAny
)

class GetAllNotes(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = Note.objects.all()
        serializer = NotesSerializer(queryset, many = True)
        return Response(serializer.data)