#Python Script
#Providers Based on Zip Code
import urllib2
import urllib
import ast
import re


def providers():
    try:
        f = open("zipcodes.txt","r")
        n = open("latandlong.txt","w")
        ln = 0
        try:
            f.readline()
            while True:
                string = f.readline()
                newstring = re.sub(' +',' ',string)
                newstring = newstring.split(" ")
                data = newstring[0]+","+newstring[7]+","+newstring[8]+"\n"
                n.write(data)
                if newstring[0] == "99929":
                    break
                ln += 1
                if ln % 100 == 0:
                    print ln
        finally:
            f.close()
            n.close()
    except IOError:
        pass
    print "FINISHED"


def zipcodesToProviders(a,b):
    try:
         n = open("latandlong.txt","r")
         p = open("provider.txt","a")
         e = open("errors.txt","a")
         j = a
         try:
            while j < b:
                values = n.readline().split(",")
                lat = values[1]
                longi = values[2]
                try:
                    string = "http://www.broadbandmap.gov/broadbandmap/broadband/dec2011/wireline?format=json&latitude="+lat+"&longitude="+longi
                    result = urllib2.urlopen(string).readline()
                    result = ast.literal_eval(result)
                    result = result['Results']['wirelineServices']
                    companies = ""
                    for i in result:
                        if i != None:
                            companies += str(i["holdingCompanyNumber"])+"]"+str(i["holdingCompanyName"])+"]"+str(i['technologies'][0]['maximumAdvertisedDownloadSpeed'])+":"
                    write1 = values[0]+";"+companies
                    write1 = write1[:-1] + "\n"
                    p.write(write1)
                except:
                    stri = values[0]+";"
                    e.write(stri)
                j = j + 1
                if j % 10 == 0:
                    print j
         except IOError:
             print "ERROR"
    finally:
         n.close()
         p.close()
         e.close()

    return

zipcodesToProviders(0,33122)
