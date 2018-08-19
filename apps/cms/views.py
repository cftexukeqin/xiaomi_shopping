from django.shortcuts import render
from django.views.generic import View
from . forms import AddPhoneForm
from utils import restful
from apps.phone.models import Phone
# Create your views here.

def index(request):
    return render(request,'cms/index.html')

class AddPhoneView(View):
    def get(self,request):
        return render(request,'cms/add_phone.html')

    def post(self,request):
        form = AddPhoneForm(request.POST)
        if form.is_valid():
            phone = form.save()
            phone.save()
            return restful.ok()
        else:
            print(form.get_error())
            return restful.paramserror(message="手机添加出错！")

