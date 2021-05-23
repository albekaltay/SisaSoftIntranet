from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Eğer User modeli inherit edilseydi Aşağıdakiler import edilecekti.
# from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db.models import CASCADE



class Checklist(models.Model):
    doc_numb = models.IntegerField(verbose_name='İşlem Numarası')
    islem = models.CharField(max_length=150,verbose_name='İşlem Adı')

    def __str__(self):
        return self.islem

    class Meta:
        verbose_name_plural = "1 - Muhasebe - İnsan Kaynakları Takip Listesi"
        verbose_name = 'İşlem'


class Checklist2(models.Model):
    doc_numb = models.IntegerField(verbose_name='İşlem Numarası')
    islem = models.CharField(max_length=150,verbose_name='İşlem Adı')

    def __str__(self):
        return self.islem

    class Meta:
        verbose_name_plural = "2 - Bilgi İşlem Takip Listesi"
        verbose_name = 'İşlem'


class Checklist3(models.Model):
    doc_numb = models.IntegerField(verbose_name='İşlem Numarası')
    islem = models.CharField(max_length=150,verbose_name='İşlem Adı')

    def __str__(self):
        return self.islem

    class Meta:
        verbose_name_plural = "3 - Oryantasyon Süreci Takip Listesi"
        verbose_name = 'İşlem'







class UserDocuments(models.Model):

    userId = models.ForeignKey('user.CustomUserModel',default=None,on_delete=CASCADE,verbose_name='Email')
    documentNumber = models.ForeignKey(Checklist,on_delete=CASCADE,verbose_name='İşlem',default=None)

    doc_choices = (
        ('Tamamlandı','Tamamlandı'),
        ('Tamamlanmadı', 'Tamamlanmadı',),
        )
    kontrol = models.CharField(max_length=100,default='Tamamlanmadı', choices=doc_choices,verbose_name='Kontrol')



    # description = models.TextField(verbose_name='Çalışan Notu')


    class Meta:
        verbose_name_plural = "A - Kullanıcı Kontrol (Muhasebe - İnsan Kaynakları Takip Listesi)"
        verbose_name = 'Kullanıcı Kontrol'

    def __str__(self):
        return self.userId.username


class UserDocuments2(models.Model):
    userId = models.ForeignKey('user.CustomUserModel', default=None, on_delete=CASCADE, verbose_name='Email')
    documentNumber = models.ForeignKey(Checklist2, on_delete=CASCADE, verbose_name='İşlem',
                                       default=None)

    doc_choices = (
        ('Tamamlandı', 'Tamamlandı'),
        ('Tamamlanmadı', 'Tamamlanmadı',),
    )
    kontrol = models.CharField(max_length=100, default='Tamamlanmadı', choices=doc_choices, verbose_name='Kontrol')

    # description = models.TextField(verbose_name='Çalışan Notu')

    class Meta:
        verbose_name_plural = "B - Kullanıcı Kontrol (Bilgi İşlem Takip Listesi)"
        verbose_name = 'Kullanıcı Kontrol'

    def __str__(self):
        return self.userId.username


class UserDocuments3(models.Model):
    userId = models.ForeignKey('user.CustomUserModel', default=None, on_delete=CASCADE, verbose_name='Email')
    documentNumber = models.ForeignKey(Checklist3, on_delete=CASCADE, verbose_name='İşlem',
                                       default=None)

    doc_choices = (
        ('Tamamlandı', 'Tamamlandı'),
        ('Tamamlanmadı', 'Tamamlanmadı',),
    )
    kontrol = models.CharField(max_length=100, default='Tamamlanmadı', choices=doc_choices, verbose_name='Kontrol')

    # description = models.TextField(verbose_name='Çalışan Notu')

    class Meta:
        verbose_name_plural = "C - Kullanıcı Kontrol (Oryantasyon Süreci Takip Listesi)"
        verbose_name = 'Kullanıcı Kontrol'

    def __str__(self):
        return self.userId.username






@receiver(post_save, sender=('user.CustomUserModel'))
def create_UserDocuments(sender, instance, created, **kwargs):
    for islem in Checklist.objects.all():
        if created:

            UserDocuments.objects.create(userId=instance,documentNumber=islem)


@receiver(post_save, sender=('user.CustomUserModel'))
def create_UserDocuments2(sender, instance, created, **kwargs):
    for islem in Checklist2.objects.all():
        if created:

            UserDocuments2.objects.create(userId=instance,documentNumber=islem)



@receiver(post_save, sender=('user.CustomUserModel'))
def create_UserDocuments3(sender, instance, created, **kwargs):
    for islem in Checklist3.objects.all():
        if created:

            UserDocuments3.objects.create(userId=instance,documentNumber=islem)



# post_save.connect(create_UserDocuments,sender=User)