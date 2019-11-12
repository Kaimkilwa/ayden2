from django.db import models

# Create your models here.
GOT_US = {
	('f',	'FRIENDS'),
	('S',	'SEARCH ENGINE'),
	('A',	'ADVERTISEMENT'),
	('O',	'OTHERS'),
	('N', 'NEWS LETTER')

}
class Contactmodel(models.Model):
	name  =  models.CharField(max_length = 200)
	created_on = models.DateTimeField(auto_now_add = True)
	email =  models.CharField(max_length = 200)
	got_us_through = models.CharField(choices = GOT_US, max_length =200 ,default=3)
	
	comment    = models. TextField()

	class Meta:
		ordering = ['-created_on']
		verbose_name_plural = 'Customer contact'
	def __str__(self):
		return self.name


