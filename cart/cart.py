from main.models import Bookinfo

class CartItem():
    def __init__(self,book,amount,cartitem_price):
        self.book = book
        self.amount = amount
        self.cartitem_price = cartitem_price

class Cart():
    def __init__(self):
        self.save_price = 0
        self.total_price = 0
        self.cartitem = []

def sums(self):
    self.total_price = 0
    self.save_price = 0
    for i in self.cartitem:
        self.total_price += i.book.dangdang_price * i.amount
        self.save_price += (i.book.price - i.book.dangdang_price) * i.amount

## 增加书籍
def add_book_toCart(self,bookid):
    print(bookid)
    for i in self.cartitem:
        print(bookid)
        print(i.book.id)
        if i.book.id == int(bookid):
            print(1)
            i.amount += 1
            i.cartitem_price += i.book.dangdang_price
            sums(self)
            return
    book = Bookinfo.objects.get(id=bookid)
    cartitem_price = book.dangdang_price
    self.cartitem.append(CartItem(book,1,cartitem_price))
    sums(self)

## 更改数量
def modify_book_cart(self,bookid,amount):
    for i in self.cartitem:
        if i.book.id == int(bookid):
            i.amount = int(amount)
            i.cartitem_price = i.book.dangdang_price * i.amount
            sums(self)
            return i.cartitem_price

##  删除书籍
def delete_book_cart(self,bookid):
    for i in self.cartitem:
        if i.book.id == int(bookid):
            self.cartitem.remove(i)
            print(111)
            sums(self)
