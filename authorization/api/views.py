from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from main.models import contest, user
from django.contrib.auth import authenticate, login

def show(request):
    return HttpResponse(request.user.username)

class UserAPIView(APIView):
    def get(self, request):
        user = request.user
        return Response({'current_user': model_to_dict(user)})
    def post(self, request):
        User = authenticate(request=request, username=request.data["username"], password=request.data["password"])
        if User is not None:
            login(request, User)
            return show(request=request)
        return Response({'error': "wrong username or password"})