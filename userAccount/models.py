from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.crypto import get_random_string

class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, userID, nickname, password):
        #if not userID:
        #    raise ValueError('must have user ID')
        if not nickname:
            raise ValueError('must have user nickname')
        if not password:
            raise ValueError('must have user password')
        user = self.model(
            userID = userID,
            nickname = nickname
        )
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    # 관리자 유저 생성
    def create_superuser(self, userID, nickname, password):
        user = self.create_user(
            userID = userID,
            password = password,
            nickname = nickname
        )
        user.is_admin = True
        user.save(using=self._db)

        return user

        
class User(AbstractBaseUser):
    id = models.AutoField(primary_key = True, null=False, blank=False)
    userID = models.CharField(default='', max_length=150, null=False, blank=False, unique=False)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)

    # User 모델의 필수 field
    is_active = models.BooleanField(default=True)    
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    USERNAME_FIELD = 'userID'
    REQUIRED_FILEDS = ['nickname']

    def __str__(self):
        return self.userID

class isLogin(models.Model):
    userID = models.CharField(default='', max_length=150, null=False, blank=False, unique=False)
    nickname = models.CharField(default='', max_length=100, null=False, blank=False, unique=True)

