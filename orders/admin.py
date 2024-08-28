from django.contrib import admin

from .models import Order, OrderItem

# admin.site.register(Order)
# admin.site.register(OrderItem)

class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ["products", "yarn", 'adaptation', "price", "quantity"]
    search_fields = (
        "products",
        'yarn',
         'adaptations'
       
    )
    extra = 0


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display =["products", "yarn", 'adaptations', "price", "quantity"] 
    search_fields = (
        "order",
        "products",
     
    )
class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = (
        
        "status",
       
      
        "created_time",
    )

    search_fields = (
       
        "is_paid",
        "created_time",
    )
    readonly_fields = ("created_time",)
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        
        "status",
      
       
        "created_time",
    )

    search_fields = (
        "id",
    )
    readonly_fields = ("created_time",)
    list_filter = (
      
        "status",
       
       
    )
    inlines = (OrderItemTabulareAdmin,)