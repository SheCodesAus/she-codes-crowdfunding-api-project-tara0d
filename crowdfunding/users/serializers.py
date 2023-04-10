from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    # phone_number = serializers.RegexField("[0-9]{10}", required=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'password', 'username', 'is_creator',]
        read_only_fields = ['id', 'email',]
        extra_kwargs = {'password': {'write_only': True}}
    

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

