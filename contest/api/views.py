from django.shortcuts import render
from rest_framework import generics
from main.models import contest, user
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict


class ContestAPIView(APIView):
    def get(self, request):
        contests = contest.Contest.all().values()
        return Response({'contests': list(contests)})
    def post(self, request):
        new_contest = contest(
            name=request.data["name"],
            description=request.data["description"],
            password=request.data["password"],
            creator=user.User.get(username="1"),
        )
        new_contest.save()
        return Response({'created_contest': model_to_dict(new_contest)})

# class ContestAPIView(generics.ListAPIView):
#     queryset = contest.Contest.all()
#     serializer_class = ContestSerializer
