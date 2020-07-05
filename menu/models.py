from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Категории"""
    name = models.CharField("Категория", max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def get_absolute_url(self):
        return reverse('menu:product_list_by_category',
                       args=[self.slug])

    class Meta:
        ordering = ('name',)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Allergen(models.Model):
    """Аллергены"""
    name = models.CharField("Название", max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = "Аллерген"
        verbose_name_plural = "Аллергены"

    def __str__(self):
        return self.name


class MainCourse(models.Model):
    """Блюдо"""
    name = models.CharField("Название", max_length=200, db_index=True)
    nutritionalValue = models.PositiveSmallIntegerField("Пищевая ценность", default=0, help_text="Ккал")
    description = models.TextField("Описание", blank=True)
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2, default=0, help_text="Цена в рублях")
    image = models.ImageField("Фото", upload_to="photo/", blank=True)
    allergen = models.ManyToManyField(Allergen, verbose_name="Аллерген", related_name="allergens")
    available = models.BooleanField("Наличие", default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False)
    slug = models.SlugField(max_length=160, unique=True)

    def get_absolute_url(self):
        return reverse('menu:product_detail',
                       args=[self.id, self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"

    def __str__(self):
        return self.name
