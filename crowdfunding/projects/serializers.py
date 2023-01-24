from rest_framework import serializers  #rest_framework is installed but not recognied in VS Code outside of virtual env
from .models import Project, Pledge

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'goal', 'image', 'is_open', 'date_created', 'owner', 'is_funded', 'funding_deadline',
        'min_players', 'max_players', 'min_age', 'min_minutes', 'max_minutes', 'pledges'    
        ]
        read_only_fields = ['id', 'date_created', 'owner']

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        # instance.date_created = validated_data.get('date_created', instance.date_created)
        # instance.owner = validated_data.get('owner', instance.owner)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.is_funded = validated_data.get('is_funded', instance.is_funded)
        instance.funding_deadline = validated_data.get('funding_deadline', instance.funding_deadline)
        instance.min_players = validated_data.get('min_players', instance.min_players)
        instance.max_players = validated_data.get('max_players', instance.max_players)
        instance.min_age = validated_data.get('min_age', instance.min_age)
        instance.min_minutes = validated_data.get('min_minutes', instance.min_minutes)
        instance.max_minutes = validated_data.get('max_minutes', instance.max_minutes)
        instance.save()
        return instance



#This is what was replaced by the 'model serializer'
# class ProjectSerializer(serializers.Serializer):
#     id = serializers.ReadOnlyField()
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField(max_length=None)
#     goal = serializers.IntegerField()
#     image = serializers.URLField()
#     is_open = serializers.BooleanField()
#     date_created = serializers.DateTimeField(read_only=True)
#     owner = serializers.ReadOnlyField(source='owner.id')

#     def create(self, validated_data):
#         return Project.objects.create(**validated_data)
