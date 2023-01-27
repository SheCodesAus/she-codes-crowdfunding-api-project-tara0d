from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    phone_number = serializers.RegexField("[0-9]{10}", required=True)
    # phone_number = serializers.RegexField(regex=r"^\+61\d{9}$", required=True) Not quite working...
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'phone_number', 'bio',]
        read_only_fields = ['id', 'email',]
    # id = serializers.ReadOnlyField()
    # username = serializers.CharField(max_length=200)
    # email = serializers.EmailField()
    # password = serializers.CharField(write_only = True)
    # first_name = serializers.CharField(max_length=100)
    # last_name = serializers.CharField(max_length=100)
    # phone_number = serializers.CharField()  #How can I validate this? Is this an appropriate field without installing anything else?
    # bio = serializers.CharField(max_length=300)
    # developer = serializers.BooleanField(default=False)    #Need to add way for admin to make created accounts developers ones


    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)



    # class PledgeSerializer(serializers.ModelSerializer):
    # class Meta:
    #     model = Pledge
    #     fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
    #     read_only_fields = ['id', 'supporter']

    # def create(self, validated_data):
    #     return Pledge.objects.create(**validated_data)
