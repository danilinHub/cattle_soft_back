from django.contrib import admin
from .models import Alimentacion, Ganado, Usuario

admin.site.register(Alimentacion)
admin.site.register(Ganado)
admin.site.register(Usuario)

admin.site.site_title = "Cattle"
admin.site.index_title = "Cattle"
admin.site.site_header = "Bienvenidos a Cattle"


