from django.shortcuts import render_to_response
from cablefinder.models import *
from django.template import RequestContext
from django.http import HttpResponse
import urllib
from django.utils import simplejson



def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

#Simple form submission
def browse(request):
	if request.method == 'GET':
		zipcode = request.GET['zipcode']
		address = request.GET['address']
		service = ['tv','phone','internet']
		services = []
		for s in service:
			if s in request.GET:
				services.append(s)		
		results = search(zipcode,address)
		#results = []
		return render_to_response('browse.html',{"results":results,"services":services},context_instance=RequestContext(request))
	else:
		return render_to_response('browse.html')

def question(request):
	print "hee"
	return HttpResponse(json, mimetype='application/javascript')








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
		#National Broadband API Call for wireline
		string = "http://www.broadbandmap.gov/broadbandmap/broadband/jun2011/wireline?"
		params = urllib.urlencode({"latitude":latitude,"longitude":longitude,"format":"json"})
		result = simplejson.load(urllib.urlopen(string+params))
		result = result['Results']['wirelineServices']
		print result
		companies = []
		for i in result:
			if i != None:
				companies.append([i["holdingCompanyName"],i['technologies'][0]['maximumAdvertisedDownloadSpeed']])
		return companies
	except:
		return "Error"
    