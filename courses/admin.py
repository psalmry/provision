from django.contrib import admin

# Register your models here.
from .models import *

class CourseAdmin(admin.ModelAdmin):
	list_display = ('code','title', 'category', 'duration', 'course_type', 'label')


class MyCourseAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'course_id', 'start_date', 'end_date',  'status')

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')


class LocationAdmin(admin.ModelAdmin):
	list_display = ('state', 'city')

class LanguageAdmin(admin.ModelAdmin):
	list_display = ('name', 'symbol')

class CourseInfoAdmin(admin.ModelAdmin):
	list_display = ('course_id', 'location', 'language', 'fees', 'start_date', 'end_date', 'instructor')
	list_select_related = ('course_id', )
	


admin.site.register(Course, CourseAdmin)
admin.site.register(MyCourse, MyCourseAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CourseInfo, CourseInfoAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Language, LanguageAdmin)


