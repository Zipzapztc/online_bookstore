from django.urls import path,include
from .views import log_in,log_out,register,user_info,change_nickname,send_verification_code,change_password,forget_password

#http://localhost:8000/user/
urlpatterns = [
    path('login/', log_in, name='login'),
    path('captcha',include('captcha.urls')),
    path('logout/', log_out, name='logout'),
    path('register/', register, name='register'),
    path('user_info/', user_info, name='user_info'),
    path('change_nickname/', change_nickname, name='change_nickname'),
    path('send_verification_code/', send_verification_code, name='send_verification_code'),
    path('change_password/', change_password, name='change_password'),
    path('forget_password/', forget_password, name='forget_password'),

]