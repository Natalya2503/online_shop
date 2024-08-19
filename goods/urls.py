from django.urls import path
from . import views


app_name = 'goods'

urlpatterns = [
     path('first_product/', views.first_product, name='first_product'),
     path('category/<int:category_id>/', views.first_category, name='first_category'),
     path('product/<int:product_id>/', views.product_details, name='product_details'),
     
     path('catalog_adapt/', views.catalog_adapt, name='catalog_adapt'),
     path('category_adapt/<int:cat_id>/', views.category_adapt, name='category_adapt'),
     path('adapt_detail/<int:adapt_id>/', views.adapt_detail, name='adapt_detail'),

     path('products_catalog/', views.products_catalog, name='products_catalog'),
     path('product_sample/<slug:product_slug>/', views.product_sample, name='product_sample' )

]
