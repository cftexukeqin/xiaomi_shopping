from django.urls import  path
from . import views

app_name = "phone"

urlpatterns = [
    path('lists/',views.mobile_list,name="lists"),
    path('<int:phone_id>/',views.detail,name="detail"),
]