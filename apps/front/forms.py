from django import forms
from ..forms import FormMixin
from django.core import validators
from .models import User
from utils import dxcache

# 用户登录表单
class SigninForm(forms.Form,FormMixin):
    username = forms.CharField(max_length=20,error_messages={'max_length':'最大长度20','required':'请输入用户名'})
    password = forms.CharField(max_length=20,min_length=6,error_messages={'max_length':'密码不能超过20个字符','min_length':'密码不得少于6个字符','required':'请输入完整信息'})
    imgcaptcha = forms.CharField(max_length=4)

    def clean_imgcaptcha(self):
        imgcaptcha = self.cleaned_data.get('imgcaptcha')
        imgcaptcha_mem = dxcache.get(imgcaptcha.lower())
        if imgcaptcha != imgcaptcha_mem:
            raise forms.ValidationError('验证码错误')
        return imgcaptcha_mem
# 用户注册表单
class SignupForm(forms.Form,FormMixin):
    username = forms.CharField(max_length=20, error_messages={'max_length': '最大长度20', 'required': '请输入用户名'})
    password = forms.CharField(max_length=20, min_length=6,error_messages={'max_length': '密码不能超过20个字符', 'min_length': '密码不得少于6个字符','required': '请输入完整信息'})
    repassword = forms.CharField(max_length=20, min_length=6,error_messages={'max_length': '密码不能超过20个字符', 'min_length': '密码不得少于6个字符'})
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3578]\d{9}')])
    imgcaptcha = forms.CharField(max_length=4)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        exists = User.objects.filter(username=username).exists()
        if exists:
            raise forms.ValidationError('该用户名已被注册')
        return username

    def clean(self):
        # claen()函数返回的就是cleaned_data
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repassword = cleaned_data.get('repassword')
        telephone = cleaned_data.get('telephone')
        if password != repassword:
            raise forms.ValidationError('两次输入的密码不一致')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError('手机号已注册')
        return cleaned_data

    def clean_imgcaptcha(self):
        imgcaptcha = self.cleaned_data.get('imgcaptcha')
        imgcaptcha_mem = dxcache.get(imgcaptcha.lower())
        if imgcaptcha != imgcaptcha_mem:
            raise forms.ValidationError('验证码错误')
        return imgcaptcha_mem