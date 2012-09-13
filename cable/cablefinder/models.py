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
	#BASIC INFO
	name = models.CharField(max_length=100)
	Price = models.FloatField()
	originalPrice = models.FloatField()
	
	#CHANNEL INFO
	totalChannels =  models.IntegerField()
	channels = models.ManyToManyField(Channel)
	
	#COSTS
	costInitial = models.FloatField()
	onlineOrderSavings = models.IntegerField()
	promotions = models.ManyToManyField(Promotion)
	cancellationFee = models.FloatField()	 
	
	#BOX FEES
	
	
	
	
#The User
class User(models.Model):
	address = models.CharField(max_length=200, null=True)
	zipcode = models.IntegerField(max_length=5, null=True)
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

#Question Class
#Eventually make this one to many field
class Question(models.Model):
	question = models.CharField(max_length=500)
	answer1 = models.CharField(max_length=200, null=True)
	answer2 = models.CharField(max_length=200, null=True)
	answer3 = models.CharField(max_length=200, null=True)
	answer4 = models.CharField(max_length=200, null=True)
	
	
	
	
	