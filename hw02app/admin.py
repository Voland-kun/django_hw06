from django.contrib import admin
from django.utils.html import format_html

from .models import Customer, Product, Order


@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


@admin.action(description="Отменить заказ")
def cancel_order(modeladmin, request, queryset):
    queryset.update(status='canceled')


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'show_image']
    ordering = ['name']
    search_fields = ['description']
    search_help_text = 'Поиск по полю описания'
    actions = [reset_quantity]

    def show_image(self, obj, res=50):
        if obj.photo:
            return format_html('<img src="{}" width="{}" />', obj.photo.url, res)
        else:
            return 'no image'

    readonly_fields = ['date', 'show_image_300']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            None,
            {
                'fields': ['show_image_300'],
             }
        ),
        (
            'Описание товара',
            {
                'classes': ['collapse'],
                'description': 'Описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Дата добавления',
            {
                'fields': ['date'],
            }
        ),
        (
            'Изображение',
            {
                'classes': ['collapse'],
                'fields': ['photo'],
            }
        ),
    ]

    def show_image_300(self, obj):
        return self.show_image(obj, res=300)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_price', 'order_date', 'status']
    ordering = ['-id']
    list_filter = ['order_date', 'products', 'status']
    actions = [cancel_order]
    # search_fields = ['products']
    # search_help_text = 'Поиск по полю продуктов'

    readonly_fields = ['order_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['customer'],
            },
        ),
        (
            'Статус заказа',
            {
                'fields': ['status'],
            }
        ),
        (
            'Заказанные товары',
            {
                'classes': ['collapse'],
                'description': 'Товары',
                'fields': ['products'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['total_price'],
            }
        ),
        (
            'Дата добавления',
            {
                'fields': ['order_date'],
            }
        ),
    ]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email']
    ordering = ['name']
    search_fields = ['address']
    search_help_text = 'Поиск по полю адреса'

    fields = ['name', 'email', 'phone', 'address', 'date']
    readonly_fields = ['date']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)

#admin admin
