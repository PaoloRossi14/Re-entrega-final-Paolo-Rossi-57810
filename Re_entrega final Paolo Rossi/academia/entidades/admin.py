from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Compras)
admin.site.register(Visitantes)
admin.site.register(Profesores)