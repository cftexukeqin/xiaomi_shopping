from django.urls import path
from . import views
app_name = 'cms'

urlpatterns = [
    path('',views.index,name="index"),
    path('add_phone/',views.AddPhoneView.as_view(),name="add_phone"),
]