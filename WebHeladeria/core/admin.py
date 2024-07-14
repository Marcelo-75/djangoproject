from django.contrib import admin
from .models import Helado

class HeladoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", )

# Register your models here.
admin.site.register(Helado, HeladoAdmin)