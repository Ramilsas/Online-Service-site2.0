from django.shortcuts import render, redirect
from rest_framework import viewsets, mixins, generics, permissions 

from .models import Product, Cart, CartItem, Category

from .serializers import ProductSerializer, CategorySerializer
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)

    # Проверяем, есть ли корзина в сессии пользователя
    if 'cart_id' in request.session:
        cart = Cart.objects.get(id=request.session['cart_id'])
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    # Проверяем, есть ли товар в корзине
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cart=cart, product=product, quantity=1)

    return redirect('cart')
