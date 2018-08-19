from django.urls import path
from . import views
app_name ='account'

urlpatterns=[
    path('',views.index,name='index'),
    path('signin/',views.my_login,name='signin'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('shopping_cart/',views.shopping_cart,name='shopping_cart'),
    path('logout/',views.my_logout,name='logout'),
    path('img_captcha/',views.img_captcha,name='img_captcha'),
    path('profile/<user_id>/',views.profile,name='profile'),
    path('order/<user_id>/',views.order,name='order'),
]