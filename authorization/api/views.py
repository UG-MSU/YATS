from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from main.models import contest, user
from django.contrib.auth import authenticate, login
from rest_framework import generics
from authorization.api import serializers


def update(request):
    if (
        len(get_user_model().User.filter(username=request.data["username"])) == 0
        and len(request.data["username"]) != 0
    ):
        request.user.username = request.data["username"]
    if len(request.data["first_name"]) != 0:
        request.user.first_name = request.data["first_name"]
    if len(request.data["patronymic"]) != 0:
        request.user.first_name = request.data["patronymic"]
    if len(request.data["last_name"]) != 0:
        request.user.first_name = request.data["last_name"]
    if len(request.data["country"]) != 0:
        request.user.first_name = request.data["country"]
    if len(request.data["city"]) != 0:
        request.user.first_name = request.data["city"]
    if len(request.data["school"]) != 0:
        request.user.first_name = request.data["school"]
    if len(request.data["password"]) > 7 and len(request.data["password"]) < 33:
        request.user.set_password(request.data["password"])
    request.user.save()
    User = authenticate(
        request=request,
        username=request.user.username,
        password=request.data["password"],
    )
    login(request, User)


def show(request):
    return HttpResponse(request.user.username)


class AuthUserAPIView(generics.ListAPIView):
    queryset = []
    serializer_class = serializers.RegAuthUserSerializer

    def post(self, request):
        User = authenticate(
            request=request,
            username=request.data["username"],
            password=request.data["password"],
        )
        if User is not None:
            login(request, User)
            return Response({"error": "success"})
        return Response({"error": "wrong username or password"})


class RegUserAPIView(generics.ListAPIView):
    queryset = []
    serializer_class = serializers.RegAuthUserSerializer

    def post(self, request):
        try:
            get_user_model().User.get(username=request.data["username"])
        except get_user_model().DoesNotExist:
            if len(request.data["password"]) < 8 or len(request.data["password"]) > 32:
                return Response({"error": "invalid size of password"})
            created_user = get_user_model().User.create_user(
                request.data["username"], "none@none.none", request.data["password"]
            )
            created_user.save()
            current_user = authenticate(
                request=request,
                username=request.data["username"],
                password=request.data["password"],
            )
            login(request, current_user)
            return Response({"error": "success"})
        return Response({"error": "this username already exists"})


class UpdateUserAPIView(generics.ListAPIView):
    queryset = []
    serializer_class = serializers.UpdateUserSerializer

    def get(self, request):
        if request.user is None:
            return Response({"error": "user is not authenticated"})
        data = serializers.UpdateUserSerializer(request.user).data
        return Response({"error": "success", "user": data})

    def put(selfself, request):
        if request.user is None:
            return Response({"error": "user is not authenticated"})
        update(request)
        return Response(
            {
                "error": "success",
                "user": serializers.UpdateUserSerializer(request.user).data,
            }
        )


class RoleUserAPIView(generics.ListAPIView):
    queryset = []
    serializer_class = serializers.UserRoleSerializer

    def get(self, request):
        if request.user is None:
            return Response({"error": "user is not authenticated"})
        return Response({"error": "success", "role": request.user.role})
