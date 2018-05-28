from django.contrib import admin
from .models import Key
# Register your models here.


class KeyAdmin(admin.ModelAdmin):
    readonly_fields = ['key']


admin.site.register(Key, KeyAdmin)