from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class RegAuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True},
        }


class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "first_name",
            "patronymic",
            "last_name",
            "country",
            "city",
            "school",
            "password",
            "role",
            "email"
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "role": {"read_only": True},
        }


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["role"]
