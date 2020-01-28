from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.

class AuthurAdmin(admin.ModelAdmin):

	list_display = ('user_id','name')

admin.site.register(Authur, AuthurAdmin)