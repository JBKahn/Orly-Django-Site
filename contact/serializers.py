from rest_framework import serializers


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=80)
    email = serializers.EmailField()
    phone_number = serializers.CharField(max_length=40, required=False)
    date = serializers.DateField(required=False)
    head_count = serializers.IntegerField(min_value=0, max_value=500, required=False)
    location = serializers.CharField(max_length=100, required=False)
    additional_info = serializers.CharField(max_length=500, required=False)
