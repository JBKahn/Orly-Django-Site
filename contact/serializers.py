from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=20)
    last_name = serializers.CharField(max_length=20)
    message = serializers.CharField(max_length=500)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=20)
