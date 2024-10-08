from django.contrib import admin
from goods.models import CategoriesAdaptations, Products, Yarn, YarnCategories, Adaptations, YarnSubCategories

admin.site.site_header = 'Панель администрирования'


@admin.register(CategoriesAdaptations)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    ordering = ['id']
    

@admin.register(YarnCategories)
class YarnCategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    ordering = ['id']
    search_fields = ['name']
    list_per_page = 5

@admin.register(YarnSubCategories)
class YarnSubCategoriesAdmin(admin.ModelAdmin):
    ordering = ['id']
    search_fields = ['name']
    list_per_page = 5

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    ordering = ['id']
    list_display = ['name', 'price', 'quantity']
    search_fields = ['name']
    list_per_page = 5

@admin.register(Yarn)
class YarnAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    ordering = ['id']
    list_display = ['name', 'price', 'color', 'quantity']
    
    search_fields =['name', 'color']
    list_per_page = 5

@admin.register(Adaptations)
class AdaptationsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    ordering = ['id']
    list_display = ['name','price', 'quantity']
    search_fields = ['name']
    list_per_page = 5