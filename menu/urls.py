from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path("api/auth-token/", obtain_auth_token, name="rest_auth_token"),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('api/dish/', views.MainCourseListView.as_view(), name='add'),
    path('api/dish/<int:pk>/', views.MainCourseDetailView.as_view(), name='api_detail'),
    path('api/category/', views.CategoryAdd.as_view(), name='categoryAdd'),
    path('api/allergen/', views.AllergenAdd.as_view(), name='allergenAdd'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
