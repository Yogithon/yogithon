from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class Pet(models.Model) :
    title = models.CharField(max_length=60)
    school = models.CharField(max_length=15)
    p_name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='Images/%Y/%m/%d')
    insta_url = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(null=True)

    def __str__(self):
        return self.title

class User(AbstractBaseUser) :
    first_name = models.CharField(max_length=5)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(verbose_name='email', max_length=100, unique=True)
    user_id = models.CharField(max_length=30, unique=True)
    user_pw = models.CharField(max_length=12)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_id', 'user_pw']

    def __str__(self):
            return self.user_id

    class Meta :
        db_table = 'users'
