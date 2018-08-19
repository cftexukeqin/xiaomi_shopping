from django.shortcuts import render
from .models import Phone
from django.contrib.auth.decorators import login_required

# Create your views here.
def mobile_list(request):
    phones = Phone.objects.all()
    context = {
        'phones':phones
    }
    return render(request, 'front/phone_list.html', context=context)

def detail(request,phone_id):
    phone = Phone.objects.get(pk=phone_id)
    context = {
        'phone':phone
    }
    return render(request, 'front/phone_detail.html',context=context)

