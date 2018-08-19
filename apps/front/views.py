from django.shortcuts import render,redirect,reverse
# Create your views here.
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import SigninForm,SignupForm
from utils import restful,dxcache
from utils.captcha import Captcha
from io import BytesIO
from apps.phone.models import Phone

def index(request):
    return render(request,'front/index.html')

@login_required(login_url='/signin/')
def shopping_cart(request):
    return render(request,'front/gouwuche.html')

def my_login(request):
    if request.method == 'GET':
        return render(request,'front/login.html')
    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            imgcaptcha = form.cleaned_data.get('imgcaptcha')
            user = authenticate(request,username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    request.session.set_expiry(0)
                    next_url = request.GET.get('next')
                    if next_url:
                        return redirect(next_url)
                    return restful.ok()
                else:
                    return restful.noauth(message='该用户已被加入黑名单')
            else:
                return restful.paramserror(message='用户名或密码错误！')
        else:
            errors = form.get_error()
            print(errors)
            return restful.paramserror(message=errors)

# 视图函数，要返回的是一张图片，因此要使用流的形式
def img_captcha(request):
    text,image = Captcha.gene_graph_captcha()
    # 将生成的验证码数字保存到memcache
    dxcache.set(text.lower(),text.lower())
    # BytesIO相当于一个管道，用来存放图片的流数据
    out = BytesIO()
    # 调用image的save方法，将图片保存在ByteIO中，
    image.save(out,'png')
    # 指针移动到开头
    out.seek(0)
    # HttpResponse对象
    response = HttpResponse(content_type='image/png')
    # 将ByteIO对象取出，写入到response里面
    response.write(out.read())
    response['Content-length'] = out.tell()
    return response
class SignupView(View):
    def get(self,request):
        return render(request,'front/register.html')
    def post(self,request):
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password =form.cleaned_data.get('password')
            telephone = form.cleaned_data.get('telephone')
            user = User.objects.create_user(username=username,password=password,telephone=telephone)
            login(request,user)
            return restful.ok()
        else:
            errors=form.get_error()
            print(errors)
            return restful.paramserror(message=errors)
def profile(request,user_id):
    # if request.method == "GET":
    #     current_user = User.objects.get(pk=user_id)
    #     context = {
    #         'user': current_user
    #     }
    return render(request, 'front/self_info.html')
def order(request,user_id):
    return render(request,'front/dingdanzhongxin.html')
def my_logout(request):
    logout(request)
    return redirect(reverse('account:index'))
