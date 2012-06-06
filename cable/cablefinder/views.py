from django.shortcuts import render_to_response
from cablefinder.models import *
from django.template import RequestContext
import urllib
import simplejson



def index(request):
	print search("07722","10 Pacer Court")
	return render_to_response('index.html',context_instance=RequestContext(request))

#Yahoo Search Parameters
APP_ID = "V7xEqm32"
SEARCH_BASE = "http://where.yahooapis.com/geocode?"
	
def search(zipcode,address):
	#Yahoo geocoder
	try:
		#Zip Code to city state
		params = urllib.urlencode({'postal':zipcode,'country':'USA','flags':"J","appid":APP_ID})
		result = simplejson.load(urllib.urlopen(SEARCH_BASE + params))
		line2 = result['ResultSet']['Results'][0]['line2']
		
		#Convert address,zip,city,state to lat and long
		params = urllib.urlencode({'postal':zipcode,'addr':address,'line2':line2,'flags':"J","appid":APP_ID})
		result = simplejson.load(urllib.urlopen(SEARCH_BASE + params))
		latitude = result['ResultSet']['Results'][0]['latitude']
		longitude = result['ResultSet']['Results'][0]['longitude']
	except:
		return "Error"
	try:
		#National Broadband API Call for wireless
		string = "http://www.broadbandmap.gov/broadbandmap/broadband/jun2011/wireless?"
		params = urllib.urlencode({"latitude":latitude,"longitude":longitude,"format":"json"})
		result = simplejson.load(urllib.urlopen(string+params))
		result = result['Results']['wirelessServices']
		companies = []
		for i in result:
			if i != None:
				companies.append(i["doingBusinessAs"])
		return companies
	except:
		return "Error"
    