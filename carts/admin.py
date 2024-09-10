from django.contrib import admin

from carts.models import Cart
from goods.models import Products, Yarn, Adaptations


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = "products", "quantity", "time_created"
    search_fields = "product", "quantity", "time_created"
    readonly_fields = ("time_created",)
    extra = 1


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display','product_display' ,"quantity", "time_created",]
    list_filter = ["time_created", "user", ]

    def user_display(self, obj):
        if obj.user:
            return str(obj.user)
        return "Анонимный пользователь"

    def product_display(self, obj):
        return str(obj.products.name)


    user_display.short_description = "Пользователь"
    product_display.short_description = "Товар"


