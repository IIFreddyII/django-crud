from rest_framework import serializers
from users.serializers import UserSerializer

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model
    """

    class Meta:
        model = Task
        read_only_fields = ["random_slug", "author", "created_at"]
        fields = read_only_fields + [
            "title",
            "description",
            "email",
            "due_date",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["author"] = UserSerializer(instance.author).data
        return data
