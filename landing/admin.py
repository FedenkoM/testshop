from django.contrib import admin
from .models import *
# Register your models here.

class SubscribeAdmin (admin.ModelAdmin):
    #list_display = ['name', 'email']
    list_display = [field.name for field in Subscriber._meta.fields]
    list_filter = ['name',]
    search_fields = ['name', 'email']
    fields = ['email']
    #exclude = []
    #inlines = []
    class Meta:
        model = Subscriber


admin.site.register(Subscriber, SubscribeAdmin)