from rest_framework import serializers
from main.models import contest

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = contest
        fields = ("name", "description", "password")