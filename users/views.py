from django.shortcuts import render
from rest_framework import generics
from .serialializer import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
