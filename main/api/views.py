from ..models import contest
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class ContestListView(generics.ListAPIView):
    queryset = contest.Contest.all()
    print(queryset)
    serializer_class = serializers.ContestSerializer
