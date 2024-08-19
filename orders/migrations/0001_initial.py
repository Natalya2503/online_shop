# Generated by Django 4.2 on 2024-08-15 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('requires_delivery', models.BooleanField(default=False, verbose_name='Требуется доставка')),
                ('delivery_address', models.TextField(blank=True, null=True, verbose_name='Адрес доставки')),
                ('payment_on_get', models.BooleanField(default=False, verbose_name='Оплата при получении ')),
                ('payment_card', models.BooleanField(default=False, verbose_name='Оплата картой')),
                ('status', models.CharField(default='В обработке', max_length=50, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Цена')),
                ('quantity', models.PositiveBigIntegerField(default=0, verbose_name='Количество')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name=' Дата продажи')),
                ('adaptations', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.adaptations', verbose_name='Приспособления для вязания')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='Заказ')),
                ('products', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.products', verbose_name='Аксессуары')),
                ('yarn', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='goods.yarn', verbose_name='Пряжа')),
            ],
            options={
                'verbose_name': 'Проданный товар',
                'verbose_name_plural': 'Проданные товары',
                'db_table': 'order_item',
            },
        ),
    ]