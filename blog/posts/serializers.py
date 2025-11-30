from rest_framework import serializers
from .models import Category, Topic, Post
from django.contrib.auth.models import User
from django.utils import timezone

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'category', 'created']

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=150, required=True)
    text = serializers.CharField()
    slug = serializers.SlugField()
    created_at = serializers.DateTimeField(required=False)
    updated_at = serializers.DateTimeField(read_only=True)
    topic = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    def validate_title(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Tytuł może zawierać tylko litery!")
        return value

    def validate_created_at(self, value):
        if value and value > timezone.now():
            raise serializers.ValidationError("Data dodania nie może być z przyszłości!")
        return value

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.topic = validated_data.get('topic', instance.topic)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        if 'created_at' in validated_data:
            instance.created_at = validated_data['created_at']
        instance.save()
        return instance