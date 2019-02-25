from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    path('loginlogic/', views.loginlogic, name='loginlogic'),
    path('login_out/',views.login_out,name='login_out'),
    path('registlogic/', views.registlogic, name='registlogic'),
    path('check_username/', views.check_username, name='check_username'),
    path('check_pwd/', views.check_pwd, name='check_pwd'),
    path('check_surepwd/', views.check_surepwd, name='check_surepwd'),
    path('check_cap/', views.check_cap, name='check_cap'),
    path('getcaptcha',views.getcaptcha, name='getcaptcha'),

]