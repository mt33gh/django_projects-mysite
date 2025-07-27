from django.contrib import admin

# Register your models here.
from .models import Cat, Vehicle

admin.site.register(Cat)
admin.site.register(Vehicle)


