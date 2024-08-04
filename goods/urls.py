from django.urls import path
from . import views


app_name = 'goods'

urlpatterns = [
     path('first_product/', views.first_product, name='first_product'),
     path('category/<int:category_id>/', views.first_category, name='first_category'),
     path('product/<int:product_id>/', views.product_details, name='product_details')
]
