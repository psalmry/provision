from django.contrib import admin

# Register your models here.
from .models import *

class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'category', 'fees', 'duration', 'course_type')

class MyCourseAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'course_id', 'localty', 'date', 'status')

class CategorieAdmin(admin.ModelAdmin):
	list_display = ('name', 'date')


class LocationAdmin(admin.ModelAdmin):
	list_display = ('state', 'city')

class LanguageAdmin(admin.ModelAdmin):
	list_display = ('name', 'symbol')

class Course_LocalityAdmin(admin.ModelAdmin):
	list_display = ('location','language')



admin.site.register(Course, CourseAdmin)
admin.site.register(MyCourse, MyCourseAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Course_Locality, Course_LocalityAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Language, LanguageAdmin)


