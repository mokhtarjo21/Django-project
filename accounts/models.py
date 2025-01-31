from django.db import models
from .libs import when_published
from .fields import GenderFields
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    phone_number = models.CharField(max_length=254)
    gender = models.CharField(max_length=254, choices=GenderFields)
    img_base64 = models.TextField(null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=3, help_text="رصيدك الحالي", verbose_name="الرصيد", default=0)

    is_dealer = models.BooleanField(default=False, verbose_name="هل هو معرض؟")

    @property
    def get_full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

class NotificationsModel(models.Model):
    sender = models.ForeignKey(User, related_name='noti_sender', on_delete=models.CASCADE)
    receiver = models.ManyToManyField(User, related_name='noti_receiver')
    reaed_users = models.ManyToManyField(User, related_name='reaed_users')
    msg = models.TextField()

    creation_date = models.DateTimeField(null=True, verbose_name="تاريخ الانشاء")

    def whenpublished(self):
        return when_published(self.creation_date)

class DealerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    dealer_name = models.CharField(max_length=255, verbose_name="اسم المعرض/الشركة")
    description = models.TextField(verbose_name="وصف المعرض", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="العنوان", blank=True, null=True)
    img_base64 = models.TextField(null=True)
    
    website = models.URLField(verbose_name="الموقع الإلكتروني", blank=True, null=True)
    opening_hours = models.CharField(max_length=50, verbose_name="ساعات العمل", blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name="المدينة", null=True)
    location = models.CharField(max_length=255, verbose_name="الموقع الجغرافي", blank=True, null=True)
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ التسجيل", null=True)
    is_active = models.BooleanField(default=True, verbose_name="نشط")

    def __str__(self):
        return self.dealer_name
    
    @property
    def get_splited_desc(self):
        return self.description.split('\n')