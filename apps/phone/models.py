from django.db import models

# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=20)
    thumbnail = models.URLField(null=True)
    price = models.FloatField()
    desc = models.TextField()
    rom = models.IntegerField()
    ram = models.IntegerField()

class PhoneOrder():
    pass

# 用户的购物车，和用户是一对一的关系
# 里面是用户选择的所有手机
