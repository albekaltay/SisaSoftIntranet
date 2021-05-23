from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



class CustomUserModel(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/',blank=True,null=True)
    position = models.CharField(max_length=150,verbose_name='Pozisyon')
    telephone_number = PhoneNumberField()
    birthday = models.DateTimeField(blank=True,null=True)
    class Meta:
        db_table = 'user'
        verbose_name = 'kullanıcı'
        verbose_name_plural = 'Kullanıcılar'

    def __str__(self):
        return self.username


