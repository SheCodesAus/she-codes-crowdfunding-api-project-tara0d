from rest_framework import serializers  #rest_framework is installed but not recognied in VS Code outside of virtual env
from .models import Project, Pledge, Images, Categories

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pledge
        fields = ['id', 'amount', 'comment', 'anonymous', 'project', 'supporter']
        read_only_fields = ['id', 'supporter']

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category_name']  #can inlcude 'id' if needed to be seen in insomnia
        read_only_fields = ['id']

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['image_url',]

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'goal', 'is_open', 'date_created', 'owner', 'is_funded', 'funding_deadline',
        'min_players', 'max_players', 'min_age', 'min_minutes', 'max_minutes', 'project_images', 'pledges', 'categories',
        'total_pledged', 'favourited_by',
        ]
        read_only_fields = ['id', 'pledges', 'date_created', 'owner', 'is_funded', 'total_pledged', 'favourited_by',]

    def create(self, validated_data):
        return Project.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    project_images = ImagesSerializer(many=True)
    categories = CategoriesSerializer(many=True)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.is_open = validated_data.get('is_open', instance.is_open)
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
