
from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from main.models import Bookinfo

# Create your views here.

# def index(request):
#     return render(request,'index.html')

def arrive_index(request):
    username = request.session.get("user")
    one_category = Bookinfo.objects.filter(classify=None)
    two_category = Bookinfo.objects.filter(classify_id__gte=1,classify_id__lt=100)

    hot_sale = Bookinfo.objects.filter(id__gt=1000).order_by('-sales')[:10]
    new_book = Bookinfo.objects.filter(id__gt=1000).order_by('-sale_time')[:8]
    good_book = Bookinfo.objects.filter(id__gt=1000).order_by('-score')[:10]
    new_book_category_id = []
    for i in new_book:
        new_book_category_id.append(Bookinfo.objects.filter(id=i.classify_id))

    return render(request,'index.html',{'one':one_category,'two':two_category,'three':hot_sale,'four':new_book,'five':good_book,'username':username,'new_book_category_id':new_book_category_id})

def query_category_book(request):
    username = request.session.get("user")
    one_category = Bookinfo.objects.filter(classify=None)
    two_category = Bookinfo.objects.filter(classify_id__gte=1, classify_id__lt=100)
    category_id = request.GET.get('category_id')
    child_id = request.GET.get('child_id')
    page = request.GET.get('page')
    category_name = Bookinfo.objects.filter(id=category_id)[0].bookname

    if child_id:
        child_book = Bookinfo.objects.filter(classify_id=child_id)
        pagtor = Paginator(child_book, per_page=5)
        child_name = Bookinfo.objects.filter(id=child_id)[0].bookname

        if page:
            pass
        else:
            page = 1
        pages = pagtor.page(page)
        return render(request, 'booklist.html', {'username':username,'category_id':category_id,'child_id':child_id,'page': pages,'one':one_category,'two':two_category,'category_name':category_name,'child_name':child_name})

    else:
        parent_book = []
        category_two = Bookinfo.objects.filter(classify_id=category_id)
        for i in category_two:
            parent_book += list(Bookinfo.objects.filter(classify_id = i.id))
        pagtor = Paginator(parent_book, per_page=5)

        if page:
            pass
        else:
            page = 1
        pages = pagtor.page(page)
        return render(request, 'booklist.html', {'username':username,'category_id':category_id,'page': pages,'one':one_category,'two':two_category,'category_name':category_name})


def bookdetail(request):
    username = request.session.get("user")
    bookid = request.GET.get("bookid")
    category_id = request.GET.get('category_id')
    child_id = request.GET.get('child_id')
    category_name = Bookinfo.objects.get(id=category_id).bookname
    child_name = Bookinfo.objects.get(id=child_id).bookname
    book_detail = Bookinfo.objects.get(id=bookid)
    print(book_detail)
    return render(request,'Book details.html',{'username':username,"book_detail":book_detail,"category_id":category_id,"child_id":child_id,"category_name":category_name,"child_name":child_name})




