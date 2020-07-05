from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Allergen, MainCourse, Category
from django.shortcuts import render, get_object_or_404
from .serializers import MainCourseSerializer, MainCourseDetailSerializer
from cart.forms import CartAddProductForm


class MainCourseListView(APIView):
    """Вывод списка блюд"""

    def create(self, validated_data):
        return MainCourse.objects.create(**validated_data)

    def get(self, request):
        main_courses = MainCourse.objects.all()
        serializer = MainCourseSerializer(main_courses, many=True)
        return Response({'Меню': serializer.data})

    def post(self, request):
        serializer = MainCourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('Название', instance.name)
        instance.nutritionalValue = validated_data.get('Пищенвая ценность', instance.nutritionalValue)
        instance.description = validated_data.get('Описание', instance.description)
        instance.price = validated_data.get('Цена', instance.price)
        instance.image = validated_data.get('Фото', instance.image)
        instance.allergen = validated_data.get('Аллерген', instance.allergen)
        instance.available = validated_data.get('Наличие', instance.available)
        instance.category = validated_data.get('Категория', instance.category)
        instance.slug = validated_data.get('slug', instance.slug)
        instance.save()
        return instance


class MainCourseDetailView(APIView):
    """Вывод блюда"""
    def get(self, request, pk):
        dish = MainCourse.objects.get(id=pk)
        serializer = MainCourseDetailSerializer(dish)
        return Response(serializer.data)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = MainCourse.objects.filter(available=True)
    allergens = Allergen.objects.all()
    cart_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'menu/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'allergen': allergens,
                   'cart_product_form': cart_product_form,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(MainCourse,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'menu/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
