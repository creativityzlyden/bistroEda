from django.contrib import admin
from django import forms
from .models import Category, MainCourse, Allergen
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class MainCourseAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = MainCourse
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class MainCourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'nutritionalValue']
    list_filter = ['available', 'allergen']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(MainCourse, MainCourseAdmin)

admin.site.register(Allergen)
