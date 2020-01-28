from django.contrib import admin

# Register your models here.
from webinars.models import Webinar

class WebinarAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'aurthor', 'webinar_type')

admin.site.register(Webinar, WebinarAdmin)
