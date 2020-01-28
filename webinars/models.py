from django.db import models
from aurthor.models import Authur

WEBINAR_TYPE = [
    ('free', 'Free'),
    ('paid', 'Paid'),
   ]
# Create your models here.
class Webinar(models.Model):
	title = models.CharField(max_length=150)
	webinar_profile_picture = models.ImageField(upload_to='webinar_icon/', default='/images/test1.jpg')
	date = models.DateField()
	overview = models.TextField()
	youtube_url = models.CharField(max_length=250, null=True)
	aurthor = models.ForeignKey(Authur, on_delete=models.CASCADE)
	webinar_type = models.CharField(max_length=6, choices=WEBINAR_TYPE, default='free', null= True)

	def get_absolute_url(self):
		return "/%i/webinar" % self.id
