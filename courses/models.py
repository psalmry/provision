from django.db import models
from aurthor.models import Authur
from django.contrib.auth.models import User

COURSE_TYPE = [
    ('tech', 'Technical'),
    ('mangt', 'Managerial'),
   ]


class Course(models.Model):
	title = models.CharField(max_length=100)
	code = models.CharField(max_length=10, default='PRO101')
	course_full_img = models.ImageField(upload_to='images/', default='/images/test1.jpg')
	label = models.CharField(max_length=20, default='Physical Event')
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	base_language = models.CharField(max_length=20, default='English')
	overview = models.TextField()
	course_type = models.CharField(
        max_length=6,
        choices=COURSE_TYPE,
        default='mangt',
    			)
	date = models.DateField(null=True)
	outline = models.TextField()
	duration = models.IntegerField(default=5, verbose_name='Durations in Days')

	
	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/%i/course" % self.id

class Category(models.Model):
	name = models.CharField(max_length=90)
	date = models.DateField()
	
	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/%i/category" % self.id

class CourseInfo(models.Model):
	course_id = models.ForeignKey('Course', related_name='variants', on_delete=models.CASCADE, null=True)
	location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
	language = models.ForeignKey('Language', on_delete=models.CASCADE, null=True)
	fees = models.DecimalField(decimal_places=2, max_digits=10000, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	instructor = models.ForeignKey(Authur, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name_plural = 'Course Infomations'

	def __str__(self):
		return self.course_id.title + ' | ' + str(self.location)


class Location(models.Model):
	state = models.CharField(max_length=150)
	city = models.CharField(max_length=150)
	
	class Meta:
		verbose_name_plural = 'Locations'

	def __str__(self):
		return self.state + ' | ' + self.city

class Language(models.Model):
	name = models.CharField(max_length=150)
	symbol = models.CharField(max_length=3)

	class Meta:
		verbose_name_plural = 'Languages'

	def __str__(self):
		return self.name + ' | ' + self.symbol


class MyCourse(models.Model):
	COURSE_STATUS = [('pending', 'Pending'),
				('register', 'Registered'), 
				('finished', 'Finished')]

	user_id = models.OneToOneField(User, on_delete=models.CASCADE)
	course_id = models.ForeignKey('CourseInfo', on_delete=models.CASCADE, null=True)
	start_date = models.DateField(null=True)
	end_date = models.DateField(null=True)
	status = models.CharField(max_length=8, choices=COURSE_STATUS, default='pending')

	def __str__(self):
		return self.course_id.course_id.title

	class Meta:
		verbose_name_plural = 'My Courses'


    			





