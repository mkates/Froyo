from django.db import models


#Company like DirecTV, Dish, etc.
class Company(models.Model):
	name = models.CharField(max_length=200)

#Channels like HBO, Stars, etc.
class Channel(models.Model):
	name = models.CharField(max_length=100)

#Promotions, in the form of text
class Promotion(models.Model):
	name = models.CharField(max_length=500)

# A package offered by a company
class Package(models.Model):
	SERVICE_TYPES = (('i','internet'),('t','tv'),('p','phone'))
	company = models.ForeignKey(Company)
	name = models.CharField(max_length=200)
	service = models.CharField(choices=SERVICE_TYPES, max_length = 1)

class SatellitePackage(models.Model):
	name = models.CharField(max_length=100)
	basePrice = models.FloatField()
	promotions = models.ManyToManyField(Promotion)
	
	totalChannels =  models.IntegerField()
	channels = models.ManyToManyField(Channel)
	costInitial = models.FloatField()
	onlineOrderSavings = models.IntegerField()
	
#UNUSED CLASSES RIGHT NOW
class User(models.Model):
	address = models.CharField(max_length=200, null=True)
	zipcode = models.IntegerField(length=5, null=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	
	SERVICES_WANTED = (('tpi','tv/phone/internet'),
						('tp','tv/phone'),
						('ti','tv/internet'),
						('pi','phone/internet'),
						('t','tv'),
						('p','phone'),
						('i','internet'))
	services = models.CharField(choices=SERVICES_WANTED, max_length = 3)
	
	
	