from django.contrib import admin

from .models import *
admin.site.register(Ordinazione)
admin.site.register(Pasto)
admin.site.register(Piatto)
admin.site.register(Tavolo)
admin.site.register(Ingredienti)
admin.site.register(Composizione)
