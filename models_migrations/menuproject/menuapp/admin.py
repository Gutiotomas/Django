from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Drinks)
admin.site.register(Menus)
admin.site.register(MenuCategory)
admin.site.register(Customer)