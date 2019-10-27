from rest_framework import serializers

class HelloSerializer (serializers.Serializer):
    """Serializers an name field for test our APIView"""
    name = serializers.CharField(max_length=10)
