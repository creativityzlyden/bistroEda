from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('api/dish/', views.MainCourseListView.as_view()),
    path('api/dish/<int:pk>/', views.MainCourseDetailView.as_view()),
    # path('api/add/', views.MainCourseCreateView.as_view()),
]