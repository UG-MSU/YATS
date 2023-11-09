from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from main.models import contest, task, submission, contest_user, contest_task, user

class CreateContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = contest
        fields = ('name', 'password')
        extra_kwargs = {'password': {'write_only' : True}}

class ContestSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='id_contest.name')
    description = serializers.CharField(source='id_contest.description')
    password = serializers.CharField(source='id_contest.password')
    class Meta:
        model = contest_user
        fields = ("name", "description", "password")
        extra_kwargs = {'password': {'write_only': True}}

class TaskSerializer(serializers.ModelSerializer):
    task_name = serializers.CharField(source='id_task.task_name')
    statement = serializers.CharField(source='id_task.statement')
    class Meta:
        model = contest_task
        fields = ("task_name", "statement")


class SubmissionSerializer(serializers.ModelSerializer):
    id_task = serializers.CharField(source='id_task.id_task')
    id_contest = serializers.CharField(source='id_contest.id_contest')
    class Meta:
        model = submission
        fields = ("status", "lang", "id_task", "id_contest")
        
        
class UserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='user.role')
    class Meta:
        model = user
        fields = ("ROLES")