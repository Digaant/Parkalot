from django.contrib import admin

# Register your models here.
from .models import user, slot
admin.site.register(slot)
admin.site.register(user)