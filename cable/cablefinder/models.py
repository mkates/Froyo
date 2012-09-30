from django.db import models
from django import forms
from django.forms import ModelForm


#################################
####### Contact Form ############
#################################
# Stores an object in the database as well as send as email to 
# the email in settings.py
class ContactForm(models.Model):
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	phone = models.CharField(max_length=20)
	comments = models.CharField(max_length=1000)

#################################
####### Provider Classes ########
#################################

class Company(models.Model):
	name = models.CharField(max_length=200)
	id = models.IntegerField(primary_key=True)

#Channels like HBO, Stars, etc.
class Channel(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=100)

# A package offered by a company
class Package(models.Model):
	id = models.IntegerField(primary_key=True)
	SERVICE_TYPES = (('i','internet'),('t','tv'),('p','phone'))
	service = models.CharField(choices=SERVICE_TYPES, max_length = 1)
	company = models.ForeignKey(Company)
	name = models.CharField(max_length=200)
	
#Cable class, inherits from package
class CablePackage(Package):
	#PRICING
	price = models.FloatField()
	originalPrice = models.FloatField()
	
	#CHANNELS
	channels = models.ManyToManyField(Channel)
	hdchannels = models.IntegerField()
	
	#RATINGS
	hdrating = models.IntegerField()
	sportsrating = models.IntegerField()
	movierating = models.IntegerField()
	kidsrating = models.IntegerField()
	culturalrating = models.IntegerField()
	musicrating = models.IntegerField()
	newsrating = models.IntegerField()
	religionrating = models.IntegerField()
	
	mobilerating = models.IntegerField()
	customerservicerating = models.IntegerField()
	valuerating = models.IntegerField()
	
	promotions = models.CharField(max_length=2000)
	
	
class PhonePackage(Package):
	#PRICING
	price = models.FloatField()
	originalPrice = models.FloatField()
	
	#FEATURES
	callwaiting = models.BooleanField()
	callerid = models.BooleanField()
	callforwarding = models.BooleanField()
	threewaycalling = models.BooleanField()
	
	
	
	
	
	
#################################
####### Unused Classes ########
#################################	
	
#User Class
class User(models.Model):
	address = models.CharField(max_length=200, null=True)
	zipcode = models.IntegerField(max_length=5, null=True)
	
	SERVICES_WANTED = (('tpi','tv/phone/internet'),
						('tp','tv/phone'),
						('ti','tv/internet'),
						('pi','phone/internet'),
						('t','tv'),
						('p','phone'),
						('i','internet'))
	services = models.CharField(choices=SERVICES_WANTED, max_length = 3)

#Promotions, in the form of text
class Promotion(models.Model):
	name = models.CharField(max_length=500)

#Feature
class Feature(models.Model):
	packageid = models.ForeignKey(Package)
	text = models.CharField(max_length=500)
	
	