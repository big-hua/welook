from django.http import JsonResponse,HttpResponse
from django.shortcuts import render

from cart.cart import Cart, add_book_toCart, modify_book_cart, delete_book_cart


def carts(request):
    username = request.session.get("user")
    cart = request.session.get('cart')
    flag = request.GET.get('flag')
    return render(request,'car.html', {"cart": cart,"flag":flag,'username':username})

def add_cart(request):
    bookid = request.GET.get('bookid')
    cart = request.session.get('cart')
    if cart is None:
        cart = Cart()
        add_book_toCart(cart,bookid)
        request.session["cart"] = cart
    else:
        add_book_toCart(cart,bookid)
        request.session["cart"] = cart
    return HttpResponse()

def update_cart(request):
    bookid = request.GET.get('bookid')
    amount = request.GET.get('amount')
    print(bookid)
    print(amount)
    cart = request.session.get('cart')
    cartitem_price = modify_book_cart(cart,bookid,amount)
    request.session["cart"] = cart
    return JsonResponse({'total_price':cart.total_price,'save_price':cart.save_price,'cartitem_price':cartitem_price})

def delete_cart(request):
    bookid = request.GET.get('bookid')
    cart = request.session.get('cart')
    delete_book_cart(cart, bookid)
    request.session["cart"] = cart
    return JsonResponse({'total_price': cart.total_price, 'save_price': cart.save_price})