from django.contrib import admin
from .models import Albert,Nikola,Raman

# Register your models here.
admin.site.register(Albert)
admin.site.register(Nikola)
admin.site.register(Raman)

class AlbertAdmin(admin.ModelAdmin):
    list_display=('id','name')