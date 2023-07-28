from django.db import models
# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    # categories = [
    #     ("Строительные материалы ", "Строительные материалы"),
    #     ("Аренда спецтехники", "Аренда спецтехники"),
    #     ("Благоустройство территории", "Благоустройство территории"),
    #     ("Асфальтирование", "Асфальтирование"),
    #     ("Ремонт дорог", "Ремонт дорог"),
    #     ("Грунт", "Грунт"),
    #     ("Дорожные работы", "Дорожные работы"),
    #     ("Земляные работы и прочие работы", "Земляные работы и прочие работы"),
    #     (
    #         "Тротуарная бетонная плитка и бордюры",
    #         "Тротуарная бетонная плитка и бордюры",
    #     ),
    #     ("Другое", "Другое"),
    # ]

    name = models.CharField(
        max_length=100, verbose_name="Категория", default="Другое"
    )
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    def __str__(self):
        return self.name


class Product(models.Model):

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField(max_length=255, verbose_name="Название")

    price = models.IntegerField(default=0, verbose_name="Цена")


    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True, verbose_name="Категория")

    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="URL"
    )

    image = models.ImageField(upload_to="img/", verbose_name="Текущее фото")

    def __str__(self):
        return self.name


class Image(models.Model):
    
    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
    
    image = models.ImageField(upload_to="img/")
