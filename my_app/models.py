from django.db import models

class Food(models.Model):
	Name =models.CharField(max_length =100)
	Recipe =models.TextField()
	Price =models.CharField(max_length =100)
	Image =models.ImageField(upload_to ='image/')

	def __str__(self):
		return self.Name

class Messages(models.Model):
	Name =models.CharField(max_length =100)
	Number =models.CharField(max_length =15)
	Email =models.CharField(max_length =20)
	Message =models.TextField()
	Date =models.DateTimeField(auto_now_add =True)

	def __str__(self):
		return self.Name

