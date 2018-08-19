from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.
from shortuuidfield import ShortUUIDField

class Usermanager(BaseUserManager):
    def _create_user(self,username,password,telephone,**kwargs):
        if not username:
            raise ValueError('请输入用户名')
        user = self.model(username=username,telephone=telephone)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,telephone,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username=username,password=password,telephone=telephone)

    def create_superuser(self,username,password,telephone,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(username=username,password=password,telephone=telephone)


class User(AbstractBaseUser,PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    username = models.CharField(max_length=20,unique=True)
    telephone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True,null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS = ['telephone']

    objects = Usermanager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username