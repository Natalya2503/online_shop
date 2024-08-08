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
        "requires_delivery",
        "status",
        "payment_on_get",
      
        "created_time",
    )

    search_fields = (
        "requires_delivery",
        "payment_on_get",
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
        "requires_delivery",
        "status",
        "payment_on_get",
       
        "created_time",
    )

    search_fields = (
        "id",
    )
    readonly_fields = ("created_time",)
    list_filter = (
        "requires_delivery",
        "status",
        "payment_on_get",
       
    )
    inlines = (OrderItemTabulareAdmin,)