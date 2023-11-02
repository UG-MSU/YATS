from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from main.models import contest

class CreateContestSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #         required=True,
    #         validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    #         )
    # username = serializers.CharField(
    #     max_length=32,
    #     validators=[UniqueValidator(queryset=get_user_model().objects.all())]
    # )
    # password = serializers.CharField(min_length=8, write_only=True)
    # def create(self, validated_data):
    #     user = get_user_model().objects.create_user(validated_data['username'], validated_data['email'],
    #          validated_data['password'])
    #     return user
    class Meta:
        model = contest
        fields = ('name', 'password')
        extra_kwargs = {'password': {'write_only' : True}}