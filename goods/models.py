from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию товара'
        verbose_name_plural = 'Категории товара'
    

class Products(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.PROTECT, verbose_name='Категория' )
   

    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class YarnCategories(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'yarncategory'
        verbose_name = 'Категорию пряжи'
        verbose_name_plural = 'Категории пряжи'

class YarnSubCategories(models.Model):
    name = models.CharField(max_length=200, verbose_name='Подкатегория пряжи')
    category = models.ForeignKey(to=YarnCategories, on_delete=models.PROTECT, related_name='subcategories', verbose_name='Категория')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'yarnsubcategory'
        verbose_name = 'Подкатегорию пряжи'
        verbose_name_plural = 'Подкатегории пряжи'
    

    

class Yarn(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    color = models.CharField(max_length=250, blank=True, verbose_name='Цвет')
    length = models.CharField(max_length=250, blank=True, null=True, verbose_name='Длина нити в мотке(метров)')
    weight = models.IntegerField(blank=True, null=True, verbose_name='Вес мотка')
    compound = models.CharField(max_length=300,blank=True, verbose_name='Состав')
    country = models.CharField(blank=True, max_length=255, verbose_name='Страна')
    subcategory = models.ForeignKey(to=YarnSubCategories, on_delete=models.PROTECT,  related_name='products', verbose_name='Подкатегория')

    
    def __str__(self):
        return f'{self.name} - {self.color}'
    
    class Meta:
        db_table = 'yarn'
        verbose_name = 'Пряжа'
        verbose_name_plural = 'Пряжа'




class Adaptations(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField(max_length=200, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=5, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    compound = models.CharField(max_length=250, blank=True, null=True, verbose_name='Состав')
    equipment = models.TextField(blank=True, null=True, verbose_name='Комплектация')
    length = models.CharField(max_length=300, blank=True, null=True, verbose_name='Длина лески(для спиц)')
    length1 = models.CharField(max_length=300, blank=True, null=True, verbose_name='Длина спицы\крючка')
    size = models.CharField(max_length=300, blank=True, null=True, verbose_name='Диаметр спицы\крючка')
    manufacturer = models.CharField(max_length=250,blank=True, null=True, verbose_name='Производитель')
    country = models.CharField(max_length=250, blank=True, null=True, verbose_name='Страна')

    def __str__(self):
        return self.name
    

    class Meta:
        db_table = 'adaptations'
        verbose_name = 'Приспособление для вязания'
        verbose_name_plural = 'Приспособление для вязания'





      


    
