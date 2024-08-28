from django.db import models
from users.models import User
from goods.models import Products, Yarn, Adaptations

class OrderItemQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
           return sum(cart.quantity for cart in self)
        return 0



class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_DEFAULT, blank=True, null=True, verbose_name='Пользователь', default=None)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    delivery_address = models.TextField(null=True, blank=True, verbose_name="Адрес доставки")
    status = models.CharField(max_length=50, default='В обработке', verbose_name='Статус')

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return f'Заказ № {self.pk} | Покупатель {self.user.username} {self.user.last_name}'

class OrderItem(models.Model):
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Заказ')
    products = models.ForeignKey(to=Products, on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, verbose_name='Аксессуары')
    yarn = models.ForeignKey(to=Yarn, on_delete=models.SET_DEFAULT, default=None,blank=True,  null=True, verbose_name='Пряжа')
    adaptations = models.ForeignKey(to=Adaptations, on_delete=models.SET_DEFAULT, default=None,blank=True, null=True, verbose_name='Приспособления для вязания')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveBigIntegerField(default=0, verbose_name='Количество')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=' Дата продажи')

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Проданный товар'
        verbose_name_plural = 'Проданные товары'
    
    objects = OrderItemQueryset.as_manager()

    def products_price(self):
        if self.products:
             return self.products.price * self.quantity
        elif self.yarn:
             return self.yarn.price * self.quantity
        elif self.adaptations:
             return self.adaptations.price * self.quantity
        return 0

    def __str__(self):
         if self.products:
             product_name = self.products.name
         elif self.yarn:
             product_name = self.yarn.name
         elif self.adaptations:
             product_name = self.adaptations.name
         else:
             product_name = 'Неизвестный товар' 
         return f'Заказ № {self.order.pk} | {product_name}'


