from django.contrib import admin
from .models import UserProfile, DealerProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(DealerProfile)