from django.contrib import admin
from .models import *

admin.site.register(Table)
admin.site.register(Dish)
admin.site.register(Meal)
admin.site.register(Order)

