from rest_framework import serializers

from db.models import JsonReceivedModel


class JsonReceivedSerializer(serializers.ModelSerializer):
    class Meta:
        model = JsonReceivedModel
        fields = ("userId", "id", "title", "completed")
