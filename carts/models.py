from django.db import models
from goods.models import Yarn, Adaptations, Products
from users.models import User

class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
           return sum(cart.quantity for cart in self)
        return 0




class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Пользователь')
    products = models.ForeignKey(to=Products, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Аксессуары')
    yarn = models.ForeignKey(to=Yarn, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Пряжа')
    adaptations = models.ForeignKey(to=Adaptations, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Приспособления для вязания')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    session_key = models.CharField(max_length=50, null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзину'
        verbose_name_plural = 'Корзина'
    
    objects = CartQueryset().as_manager()

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
            return f'Корзина {self.user.username} | Товар {self.products.name} | Количество {self.quantity}'
        
        elif self.yarn:
            return f'Корзина {self.user.username} | Пряжа {self.yarn.name} | Количество {self.quantity}'
        
        elif self.adaptations:
            return f'Корзина {self.user.username} | Товар {self.adaptations.name} | Количество {self.quantity}'
        
   