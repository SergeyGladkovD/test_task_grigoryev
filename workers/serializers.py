from rest_framework import serializers

from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    """Сериалайзер модели работник."""

    class Meta:
        model = Worker
        fields = ["id", "full_name", "brigade_number", "salary", "specialization"]
