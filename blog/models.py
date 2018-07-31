from django.db import models

# Create your models here.


class Post(models.Model):

	title = models.CharField(max_length=20)
	 # = models.CharField()
	description = models.CharField(max_length=200)
	pub_date = models.DateField( blank=False, null=False, auto_now_add=True)


	def __str__(self):
		return "{} {}".format(self.title, self.pub_date)

