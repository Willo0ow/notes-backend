from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
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
from django.contrib.auth import authenticate, login

class GetAllNotes(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        queryset = Note.objects.all()
        serializer = NotesSerializer(queryset, many = True)
        return Response(serializer.data)

class SaveNote(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request, format='json'):
        import json
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            note = serializer.save()
            if note:
                returnJson = serializer.data
                return Response(returnJson, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        import json
        tryUsername = request.data['username']
        tryPassword = request.data['password']
        user = authenticate(username=tryUsername, password=tryPassword)
        serializer = UserSerializer(user)
        if user:
            login(request, user)
            returnJson = serializer.data
            return Response(returnJson, status=status.HTTP_200_OK)
        return Response('Not found', status=status.HTTP_400_BAD_REQUEST)


