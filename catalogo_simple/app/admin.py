# -*- encoding: utf-8 -*-

from django.contrib import admin
from app.models import Producto, Comentario

admin.site.register(Producto)
admin.site.register(Comentario)