from django.contrib import admin

# Register your models here.
from .models import  Product, Cart, CartItem, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'image', 'description', )
    list_display_links = ('name',)
    list_editable = ('price',)


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart,CartAdmin)
admin.site.register(CartItem)
admin.site.register(Category)