from ..models import contest
from rest_framework import serializers

class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = contest
        fields = (['name', 'password']) # if not declared, all fields of the model will be shown