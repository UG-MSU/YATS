from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from main.models import contest, user
from django.contrib.auth import authenticate, login
from authorization.api import serializers

def show(request):
    return HttpResponse(request.user.username)

class AuthUserAPIView(generics.ListAPIView):
    queryset = user.User.all()
    serializer_class = serializers.RegAuthUserSerializer
    def post(self, request):
        User = authenticate(request=request, username=request.data["username"], password=request.data["password"])
        if User is not None:
            login(request, User)
            return Response({"error": "success"})
        return Response({"error": "wrong username or password"})

class RegUserAPIView(generics.ListAPIView):
    queryset = user.User.all()
    serializer_class = serializers.RegAuthUserSerializer
    def post(self, request):
        if user.User.get(username=request.data["username"]) is not None:
            return Response({"error": "this username already exists"})
        if len(request.data["password"]) < 8 or len(request.data["password"]) > 32:
            return Response({"error": "invalid size of password"})
        created_user = user(username=request.data["username"], password=request.data["password"])
        created_user.save()
        User = authenticate(request=request, username=request.data["username"], password=request.data["password"])
        if User is not None:
            login(request, User)
            return Response({"error": "success"})
        return Response({"error": "something went wrong"})