from rest_framework import serializers
from .models import MainCourse, Category, Allergen


class MainCourseDetailSerializer(serializers.ModelSerializer):
    """Описание блюда"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    allergen = serializers.SlugRelatedField(slug_field="name", read_only=True, many=True)

    class Meta:
        model = MainCourse
        fields = '__all__'


class MainCourseSerializer(serializers.ModelSerializer):
    """Список блюд"""
    category = serializers.SlugRelatedField(queryset=Category.objects.all(),
                                            allow_null=False, required=True,
                                            slug_field='name')
    allergen = serializers.SlugRelatedField(many=True,
                                            queryset=Allergen.objects.all(),
                                            allow_null=False, required=True,
                                            slug_field='name')

    class Meta:
        model = MainCourse
        fields = '__all__'
