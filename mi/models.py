from django.db import models

# Create your models here.
class Category1(models.Model):
    name = models.CharField(verbose_name='Кат1_название', max_length=32, blank=False, unique=True)
    def __str__(self):
        return self.name

class Category2(models.Model):
    cat1 = models.ForeignKey(Category1, null=True)
    name = models.CharField(verbose_name='Кат2_название', max_length=32, blank=False)
    click = models.IntegerField()
    def __str__(self):
        return self.name

class Category3(models.Model):
    cat1 = models.ForeignKey(Category1, null=True)
    cat2 = models.ForeignKey(Category2, null=True)
    name = models.CharField(verbose_name='Кат3_название', max_length=32, blank=False)
    click = models.IntegerField()
    def __str__(self):
        return self.name

class IsNew(models.Model):
    isnew = models.BooleanField(verbose_name='Новое?', default=True, blank=False)

class Item(models.Model):
    cat1 = models.ForeignKey(Category1, null=True)
    cat2 = models.ForeignKey(Category2, null=True)
    cat3 = models.ForeignKey(Category3, null=True)
    exchange = models.BooleanField(verbose_name='Возможность обмена', default=False, blank=False)
    name = models.CharField(verbose_name='Назв.товара', max_length=30)
    def shortname(self):
        return self.name[:15]
    descr = models.TextField(verbose_name='Детальное описание', max_length=300)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    price = models.IntegerField(verbose_name='Цена', null=False, blank=False)
    image_main = models.ImageField(verbose_name='Главное изображение', storage='')
    image_second = models.ImageField(verbose_name='Второе изображение', storage='')
    image_third = models.ImageField(verbose_name='Третье изображение', storage='')
    image_fourth = models.ImageField(verbose_name='Четвертое изображение', storage='')
    clicks = models.IntegerField(verbose_name='Количество просмотров', default=0)
    reason = models.CharField(verbose_name='Причина продажи', max_length=30)
