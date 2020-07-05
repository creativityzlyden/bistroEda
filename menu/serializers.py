from rest_framework import serializers
from .models import MainCourse


class MainCourseDetailSerializer(serializers.ModelSerializer):
    """Описание блюда"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    allergen = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = MainCourse
        fields = '__all__'


class MainCourseSerializer(serializers.ModelSerializer):
    """Список блюд"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    allergen = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = MainCourse
        fields = '__all__'
