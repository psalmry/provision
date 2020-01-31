from django.db import models
from aurthor.models import Authur
from django.contrib.auth.models import User

COURSE_TYPE = [
    ('tech', 'Technical'),
    ('mangt', 'Managerial'),
   ]

class Course(models.Model):
	title = models.CharField(max_length=100)
	course_full_img = models.ImageField(upload_to='images/', default='/images/test1.jpg')
	category = models.ForeignKey('Categorie', on_delete=models.CASCADE)
	overview = models.TextField()
	course_type = models.CharField(
        max_length=6,
        choices=COURSE_TYPE,
        default='mangt',
    			)
	date = models.DateField(null=True)
	location = models.ManyToManyField('Course_Locality')
	fees = models.DecimalField(decimal_places=2, max_digits=10000)
	outline = models.TextField()
	duration = models.IntegerField(default=5, verbose_name='Durations in Days')
	instructors = models.ManyToManyField(Authur, verbose_name='Instructors for this Course')


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/%i/course" % self.id

class Categorie(models.Model):
	name = models.CharField(max_length=90)
	date = models.DateField()
	instructor_by_category = models.ManyToManyField(Authur, verbose_name='Instructors for this Category')

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/%i/category" % self.id

class Course_Locality(models.Model):
	#course_id = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
	#date = models.DateField()
	location = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
	language = models.ForeignKey('Language', on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name_plural = 'Course Localities'

	def __str__(self):
		return self.location.state + ' | ' + self.language.name


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
	course_id = models.ForeignKey('Course', on_delete=models.CASCADE, null=True)
	localty  = models.ForeignKey('Course_Locality', on_delete=models.CASCADE, null=True)
	date = models.DateField()
	status = models.CharField(max_length=8, choices=COURSE_STATUS, default='pending')

	def __str__(self):
		return self.course_id.title

	class Meta:
		verbose_name_plural = 'My Courses'


    			





