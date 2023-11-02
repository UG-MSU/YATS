from ..models import contest, task, submission
from rest_framework import serializers


class ContestSerializer(serializers.ModelSerializer):
    class Meta:
        model = contest
        fields = [
            "name",
            "password",
        ]  # if not declared, all fields of the model will be shown

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = task
        fields = [
            "task_name",
            "statement",
        ]


class SumbissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = submission
        fields = [
            "status",
            "lang",
            "id_contest_id",
            "id_task_id",
        ]
