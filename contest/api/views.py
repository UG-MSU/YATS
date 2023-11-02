from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
from main.models import contest, user
from django.contrib.auth import authenticate, login
from rest_framework import generics

class CreateContestAPIView(generics.ListAPIView):
    queryset = contest.Contest.all()
    model = contest 
    # def get(self, request):
    #     user = request.user
    #     return Response({'current_user': model_to_dict(user)})
    def post(self, request):
        if 7 < len(request.data ['password']) < 32:
            return Response({'error' : 'invalid size of password'})
        created_contest = contest(name = request.data['name'], password = request.data['password'])
        created_contest.save()
        return Response({'error' : 'success'})
        
