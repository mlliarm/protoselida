__author__ = "milia"
__email__ = "milia@protonmail.com"
__licence__ = "GPL v.2"

import datetime
import wget
import os
from datetime import date
import calendar
import urllib2
import time

# Papers from frontpagesgr website
def frmfrontpagesgr(efimerida, today, year):
	try:
		url = 'http://www.frontpages.gr/data/' + year + '/' + today + '/' + efimerida + '.jpg'
		urllib2.urlopen(url)
		wget.download(url)
		oldname = efimerida + '.jpg'
		newname = today + "_" + "FrontpagesGR" + "_" + oldname
		os.rename(oldname, newname)
	except urllib2.HTTPError, e:
		#print(e.code)
		print "ERROR 404: Paper not found !"
		print " "
	except urllib2.HTTPError, e:
		print(e.args)

# Insert the date from the keyboard
def insertdate():
	global today, year
	mydate = raw_input("Please insert the date in the format YYYY/MM/DD (from the year 2010 till today): ")
	year = mydate[0:4]
	month = mydate[5:7]
	day = mydate[8:10]
	today = year + month + day		
	# Findng out the weekday
	mydate = date(int(year), int(month), int(day))
	weekday = calendar.day_name[mydate.weekday()]
	print "Will download the papers of " + weekday + " " + year + "/" + month + "/" + day + " !"
	print " "

# Calculating today's date, year and day of week, automatically (default)
def autodate():
	global today, year
	mydate = time.strftime("%Y:%m:%d")
	year = mydate[0:4]
	month = mydate[5:7]
	day = mydate[8:10]
	today = year + month + day
	weekday = time.strftime("%a") + "day"
	print "Will download today's (" + weekday + ") papers !"
	print " "

# Main function
def main():
	# Main papers
	efimerides_vdomadas = ['HKathimeriniI', 'TaNeaI','EthnosI', 'EfSynI', 'EstiaI','AugiI','EleutherosTyposI','RizospastisI','EspressoI',\
					'AgoraI', 'AggelioforosI','MakedoniaI', 'TiposThessalonikisI','KontraNewsI', 'ToParonI','FreeSundayI','ToXwniI','PressTimeI', 'KarfiI',\
					'LogosI','StarPressI', 'EloraI','ParaskinioI','ArthroI','GPrinI','KarfitsaI','DimokratiaI','ApopsiI','HNautemporikiI','HmerhsiaI','GEpoxiI',\
					'XrhmatisthrioI','MetoxosI','DimoprasionI','DealNewsI','IhodimoprasionI','OikonomikiBEI','DimoprasiakiAI']

	# Local papers of the week
	topikes_efimerides = ['HAgonI','HNeoiAgonesI','HProinosLogosI','HAnexartitosI','TTaxydromosI','TEleutheriaI','TMagnisiaI','TProinosTyposI', \
					'TThessaliaI','NADimokratikiRodouI','NAKoiniGnomiI','NAKykladikiI','BAPolitisI','MTAgonasI','MTXronosI','MTNeaEgnatiaI',\
					'MTProinosTyposI','MTEleutheroVimaI','MTNeaKastoriaI','MTSimeriniSerI','MTHmerhsiaVI','PanelliniaBEI','KMParatiritsI',\
					'KMPoliteiaI','KPatrisI','KRethemniotikaI','KNeaKritiI','KAnatolhI','IEnimerosiI','IHmeraI','IHmerhsiosI','PPeloponnisosI' \
					,'PPatrisI','PGnomiI','PProtiI','DESyneidisiI','PAllagiI','PGegonotaI','PEleutheriaI','PProiniI','SLamiakosI','ASyneidhshI','AAttikoBhmaI',\
					'AXtyposI','EthnikosKirikasI']

	# Clear screen
	os.system('clear')

	# Welcome Message
	print "WELCOME TO THE PROTOSELIDA (FIRST PAGES) DOWNLOADER !"
	print "-----------------------------------------------------"
	print " "

	# Decision making follows
	answer = raw_input("1. Would you like to enter an older date? (YES/NO): ")
	if answer == "YES" or answer == "yes":
		insertdate()
	else:
		autodate()

	# Choose if you want the local papers as well (43)
	topikes = raw_input("2. Do you want the local newspapers of the day as well? (YES/NO): ")
	
	#	Call the downloading function
	for efimerida in efimerides_vdomadas:
		frmfrontpagesgr(efimerida,today,year)
	if topikes == "YES" or topikes == "yes":
		for efimerida in topikes_efimerides:
			frmfrontpagesgr(efimerida,today,year)
	print " "

if __name__ == "__main__":
	main()
