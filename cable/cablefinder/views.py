from django.shortcuts import render_to_response
from cablefinder.models import *
from django.template import RequestContext
from django.http import HttpResponse
import urllib
from django.utils import simplejson


#############################################
# Main Page Call Functions ##################
#############################################

#Step 1 landing page
def index(request):
	return render_to_response('index.html',context_instance=RequestContext(request))
#Step 2 Choose preferences 
def preferences(request):
	elements = {}
	if request.method == 'GET' and len(request.GET) > 0:
		if 'zipcode' in request.GET:
			#Find by zipcode
			zipcode = request.GET['zipcode']
			elements["zipcode"] = zipcode
		#Find by latitude and longitude
		if 'latitude' in request.GET and 'longitude' in request.GET :
			elements["latitude"] = request.GET['latitude']
			elements["longitude"] = request.GET['longitude']
	return render_to_response('preferences.html',elements,context_instance=RequestContext(request))
	
	
	
#Step 3 find package page, passing in zipcode + lat and long
def findpackage(request):
	return render_to_response('findpackage.html',context_instance=RequestContext(request))
#Step 4 purchase package
def buypackage(request):
	return render_to_response('buypackage.html',context_instance=RequestContext(request))




#############################################
# Zip Code to Provider Functions ############
#############################################

# Yahoo Search Parameters on my Yahoo Account (mad11handles)
# Can make up to 50,000 requests per day
APP_ID = "V7xEqm32"
SEARCH_BASE = "http://where.yahooapis.com/geocode?"

#Returns a list of length two, with [latitude,longitude]
def LatitudeAndLongitude(zipcode):
	params = urllib.urlencode({'postal':zipcode,'country':'USA','flags':"J","appid":APP_ID})
	combine = SEARCH_BASE+params
	try:
		result = simplejson.load(urllib.urlopen(SEARCH_BASE + params))
		line2 = result['ResultSet']['Results'][0]
		return [line2['latitude'],line2['longitude']]
	except:
		return None

#Convert latitude/longitude to broadband providers
#Input is a list of length two
def LatLongToWirelineProviders(latandlong):
	if latandlong:
		try:
			#National Broadband API Call for wireline
			string = "http://www.broadbandmap.gov/broadbandmap/broadband/jun2011/wireline?"
			params = urllib.urlencode({"latitude":latandlong[0],"longitude":latandlong[1],"format":"json"})
			print params
			result = simplejson.load(urllib.urlopen(string+params))
			result = result['Results']['wirelineServices']
			print result
			companies = []
			for i in result:
				if i != None:
					companies.append([i["holdingCompanyNumber"],i["holdingCompanyName"],i['technologies'][0]['maximumAdvertisedDownloadSpeed']])
			return companies
		except:
			return None
	return None
	





#############################################
# Unused / Obsolete Functions ###############
#############################################
	
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
	print "question"
	return HttpResponse(json, mimetype='application/javascript')