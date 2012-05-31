from django.shortcuts import render_to_response
from cablefinder.models import *
from django.template import RequestContext
import urllib
import simplejson



def index(request):
	print search("02215","99 Bay State Road")
	return render_to_response('index.html',context_instance=RequestContext(request))
	
class YahooSearchError(Exception):
    pass

#Yahoo Search Parameters
APP_ID = "V7xEqm32"
SEARCH_BASE = "http://where.yahooapis.com/geocode?"
	
def search(zipcode,address):
	#Yahoo geocoder
	try:
		params = urllib.urlencode({'postal':zipcode,'line1':address,'flags':"J","appid":APP_ID})
		string = SEARCH_BASE + params
		result = simplejson.load(urllib.urlopen(string))
		if 'Error' in result:
			raise YahooSearchError, result['Error']
		print result['ResultSet']['Results'][0]
		latitude = result['ResultSet']['Results'][0]['latitude']
		longitude = result['ResultSet']['Results'][0]['longitude']
		print latitude
		print longitude
	except:
		return "Error"
	
	try:
		string = "http://www.broadbandmap.gov/broadbandmap/broadband/jun2011/wireless?"
		params = urllib.urlencode({"latitude":latitude,"longitude":longitude,"format":"json"})
		result = simplejson.load(urllib.urlopen(string+params))
		result = result['Results']['wirelessServices']
		for i in result:
			print i["doingBusinessAs"]
	except:
		return "Error"
#National Broadband API Call
    