from django.db import models
from django.contrib.auth.models import User


#class Post(models.Model):
#	titulo = models.CharField(max_length=100)
#	conteudo = models.TextField()
#	autor = models.ForeignKey(User, on_delete=models.CASCADE)



#	def __str__(self):
#		return self.titulo

class Vendor_List(models.Model):
	complete = models.BooleanField(default=False) #quando for True vc nao pode comprar mais
	item = models.CharField(max_length=100)
	
	def __str__(self):
		return self.item #nao esta alterando com o nome do produto
