import random,string,re
from django.contrib.auth.hashers import make_password,check_password

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from main.models import TUser
from django.views.decorators.csrf import csrf_exempt
from user.captcha.image import ImageCaptcha


def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0


def login(request):
    flag = request.GET.get("flag")
    return render(request,'login.html',{"flag":flag})

def login_out(request):
    request.session["user"] = None
    return redirect("main:index")


@csrf_exempt
def loginlogic(request):
    if request.method == 'POST':
        flag = request.POST.get('flag')
        username = request.POST.get('txtUsername')
        password = request.POST.get('txtPassword')
        text = TUser.objects.filter(username=username)[0].password
        if check_password(password,text):
            request.session['user']=username
            print(1111)
            if flag == 'index':
                return JsonResponse({'user':0})
            elif flag == 'cart':
                print(11112222)
                return JsonResponse({'user': 1})
        else:
            return JsonResponse({'user':2})
        return JsonResponse({'user':3})

def regist(request):
    flag = request.GET.get("flag")
    return render(request,'register.html',{"flag":flag})



def registlogic(request):
    try:
        with transaction.atomic():
            flag = request.GET.get('flag')
            email = request.POST.get('txt_username')
            pwd = request.POST.get('txt_password')
            password = make_password(pwd, None, 'pbkdf2_sha256')
            request.session['user'] = email
            if flag == 'index':
                TUser.objects.create(email=email, password=password)
                return render(request,'register ok.html',{"email":email})
            elif flag == 'cart':
                TUser.objects.create(email=email, password=password)
                return redirect('order:submit_cart')
    except:
        return HttpResponse('很抱歉，您的输入有误!')



def check_username(request):
    if request.method == 'POST':
        username = request.POST.get('txtUsername')
        result = TUser.objects.filter(email=username)
        if validateEmail(username):
            if result:
                return HttpResponse('1')
            else:
                return HttpResponse('0')
        else:
            return HttpResponse('2')

def check_pwd(request):
    if request.method == 'POST':
        userpwd = request.POST.get('txtPassword')
        request.session['userpwd'] = userpwd
        if len(userpwd) < 6:
            return HttpResponse('1')
        elif len(userpwd)<10:
            return  HttpResponse('2')
        return HttpResponse('0')

def check_surepwd(request):
    if request.method == 'POST':
        surepwd = request.POST.get('txtrepassword')
        if surepwd == request.session.get('userpwd'):
            return HttpResponse('1')
        return HttpResponse('0')

def getcaptcha(request):
    image = ImageCaptcha()
    code = random.sample(string.ascii_lowercase+string.ascii_uppercase+string.digits,4)
    random_code = "".join(code)
    request.session['code']=random_code
    data = image.generate(random_code )
    return HttpResponse(data,"image/png")

def check_cap(request):
    code = request.session.get('code')
    if code.lower() == request.POST.get('txt_vcode').lower():
        return HttpResponse('1')
    return HttpResponse('0')


#
# ##  邮件发送
# import datetime
# import hashlib
#
# from django.core.mail import EmailMultiAlternatives
#
# from main import models
#
#
# def arrive_index(request):
#     print(make_password(123456, None, 'pbkdf2_sha256'))
#     text = 'pbkdf2_sha256$100000$hWyGKrPoi7x4$cNz2Buc+xgmFFkqoY9XjUjVnh3jnYvTUjkbpb2p86Xg='
#     check_password(123456, text)
#     return render(request, 'hello.html')
#
#
# def register_form(request):
#
#     return render(request, 'register.html')
#
#
# def hash_code(name, now='yan'):
#     h = hashlib.sha256()
#     name +=  now
#     h.update(name.encode())
#     return h.hexdigest()
#
# def make_string(user):
#     """
#     为用户生成一个唯一的注册的标识
#     :param user:
#     :return:
#     """
#     now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     code = hash_code(user.name, now)
#     models.ConfirmString.objects.create(code=code, user=user)
#
#     return code
#
#
# def send_email(email, code):
#     """
#     向用户的邮箱发送验证邮件
#     :param email:用户邮箱，
#     :param code:生成的唯一的验证标识
#     :return:
#     """
#     subject, from_email, to = '来自149的测试邮件', '18500230996@sina.cn', 'maoxinyu925@163.com'
#     text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
#     html_content = '<p>感谢注册< a href="http://{}/confirm/user_confirm/?code={}"target = blank > www.baidu.com < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1:8000', code)
#     msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
#
#
# def user_register(request):
#     """
#     处理用户注册视图
#     :param request:用户注册信息
#     :return:处理完成用户的信息，返回到用户登录的
#     """
#     username = request.POST.get('username')
#     password = request.POST.get('password')
#     email = request.POST.get('email')
#     new_user = models.User.objects.create(name=username, password=password, email=email)
#     code = make_string(new_user)
#     send_email(email, code)
#
#     message = '请前往邮箱进行验证'
#
#     return render(request,