import datetime,random

from cart.cart import Cart,CartItem

from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render,redirect
from main.models import TUser,TOrder,TAddress,TOrderitem,Bookinfo



def submit_cart(request):
    username = request.session.get('user')
    flag = request.GET.get('flag')
    cart = request.session.get('cart')
    if username is None:
        return render(request,'login.html',{"flag":flag})
    else:
        username_id = TUser.objects.filter(username=username)[0].id
        user_address = TAddress.objects.filter(user_id=username_id)
        return render(request,'indent.html',{"address":user_address,'cart':cart,'username':username})

def check_address(request):
    return render(request,'indent ok.html')

def creat_order(request):

    # try:
    #     with transaction.atomic():
            def order_numbers():
                nowTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                randomNum = random.randint(0, 100)
                if randomNum <= 10:
                    randomNum = str(0) + str(randomNum)
                uniqueNum = str(nowTime) + str(randomNum)
                return uniqueNum

            username = request.session.get('user')
            order_number = order_numbers()
            address_name = request.POST.get('ship_man')
            address = request.POST.get('ship_address')
            zipcode = request.POST.get('ship_code')
            tel = request.POST.get('ship_tel')
            iphone = request.POST.get('ship_iphone')
            cart = request.session.get('cart')
            user = request.session.get('user')
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(now)
            users = TUser.objects.get(username=user)
            address_flag = TAddress.objects.filter(address=address, user_id=users.id)
            print()
            if address_flag is None:
                TAddress.objects.create(address_name=address_name, address=address, zipcode=zipcode, telphone=tel,iphone=iphone,user_id=users.id)
            addresses = TAddress.objects.get(address=address, user_id=users.id)
            TOrder.objects.create(order_id=order_number, sum_price=cart.total_price, datetime=now, status=1,address_id=addresses.id, user_id=users.id)
            book_count = 0
            for i in cart.cartitem:
                book_count += i.amount
                book_info = Bookinfo.objects.get(id=i.book.id)
                order_info = TOrder.objects.get(order_id=order_number)
                TOrderitem.objects.create(book_count=i.amount, total=i.cartitem_price, book_id=book_info.id,order_id=order_info.id)
            request.session["cart"] = None
            return render(request, 'indent ok.html',{'username': username, 'order_number': order_number, 'pay_money': cart.total_price, 'book_count': book_count,'address_name': address_name})

    # except:
    #     return HttpResponse('很抱歉，您的输入有误!')



# def check_username(request):
#     if request.method == 'POST':
#         username = request.POST.get('txtUsername')
#         result = TUser.objects.filter(email=username)
#         if validateEmail(username):
#             if result:
#                 return HttpResponse('1')
#             else:
#                 return HttpResponse('0')
#         else:
#             return HttpResponse('2')
#
# def check_pwd(request):
#     if request.method == 'POST':
#         userpwd = request.POST.get('txtPassword')
#         request.session['userpwd'] = userpwd
#         if len(userpwd) < 6:
#             return HttpResponse('1')
#         elif len(userpwd)<10:
#             return  HttpResponse('2')
#         return HttpResponse('0')
#
# def check_surepwd(request):
#     if request.method == 'POST':
#         surepwd = request.POST.get('txtrepassword')
#         if surepwd == request.session.get('userpwd'):
#             return HttpResponse('1')
#         return HttpResponse('0')