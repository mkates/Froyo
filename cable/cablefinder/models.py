from django.db import models


#Company like DirecTV, Dish, etc.
class Company(models.Model):
	name = models.CharField(max_length=200)

# A package offered by a company
class Package(models.Model):
	SERVICE_TYPES = (('i','internet'),('t','tv'),('p','phone'))
	
	company = models.ForeignKey(Company)
	name = models.CharField(max_length=200)
	service = models.CharField(choices=SERVICE_TYPES,max_length = 1)
	
#A combination of several packages
class Bundle(models.Model):
	name = models.CharField(max_length=200)





