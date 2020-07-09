from rest_framework.response import Response
from rest_framework import status, generics, permissions
from .models import Allergen, MainCourse, Category
from django.shortcuts import render, get_object_or_404
from .serializers import MainCourseSerializer, MainCourseDetailSerializer, AddCategorySerializer, AddAllergenSerializer
from cart.forms import CartAddProductForm


class AllergenAdd(generics.ListAPIView):
    queryset = Allergen.objects.filter()
    serializer_class = AddAllergenSerializer

    def post(self, request):
        serializer = AddAllergenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryAdd(generics.ListAPIView):
    queryset = Category.objects.filter()
    serializer_class = AddCategorySerializer

    def post(self, request):
        serializer = AddCategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MainCourseListView(generics.ListAPIView):
    """Вывод списка блюд"""
    serializer_class = MainCourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        main_courses = MainCourse.objects.all()
        return main_courses

    def post(self, request):
        serializer = MainCourseSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MainCourseDetailView(generics.RetrieveAPIView):
    """Вывод блюда"""
    queryset = MainCourse.objects.filter()
    serializer_class = MainCourseDetailSerializer


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
