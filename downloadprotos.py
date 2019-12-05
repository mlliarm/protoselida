__author__ = "milia"
__email__ = "milia@protonmail.com"
__licence__ = "GPL v.2"

import datetime
import os
from datetime import date
import calendar
import urllib
import time
from urllib.request import Request, urlopen
from PIL import Image
import io

def frmfrontpagesgr(efimerida:str, today:str, year:str) -> None:
	""" Downloads the newspaper images from the webpage """
	try:
		url = 'https://www.frontpages.gr/data/' + year + '/' + today + '/' + efimerida + '.jpg'
		req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
		image = urlopen(req).read()
		image = Image.open(io.BytesIO(image))
		oldname = efimerida + '.jpg'
		newname = today + "_" + "FrontpagesGR" + "_" + oldname
		image.save('./' + newname)
	except urllib.error.HTTPError as e:
		print("ERROR 404: Paper " + efimerida + " not found !")
		print(" ")
	except urllib.error.HTTPError as e:
		print(e.args)

def insertdate() -> None:
	""" Asks the user to insert the date of the newspaper(s) to be downloaded """
	global today, year
	mydate = input("Please insert the date in the format YYYY/MM/DD (from the year 2010 till today): ")
	year = mydate[0:4]
	month = mydate[5:7]
	day = mydate[8:10]
	today = year + month + day
	# Findng out the weekday
	mydate = date(int(year), int(month), int(day))
	weekday = calendar.day_name[mydate.weekday()]
	print("Will download the papers of " + weekday + " " + year + "/" + month + "/" + day + " !")
	print(" ")

def autodate() -> None:
	""" Calculating today's date, year and day of the week automatically (default) """
	global today, year
	mydate = time.strftime("%Y:%m:%d")
	year = mydate[0:4]
	month = mydate[5:7]
	day = mydate[8:10]
	today = year + month + day
	weekday = time.strftime("%a") + "day"
	print("Will download today's (" + weekday + ") papers !")
	print(" ")

def main() -> None:
	""" Main function that has the names of the newspapers and calls the previous functions """
	# Main papers
	efimerides_vdomadas = ('HKathimeriniI', 'TaNeaI','EthnosI', 'EfSynI', 'EstiaI','AugiI','EleutherosTyposI','RizospastisI','EspressoI',\
					'AgoraI', 'AggelioforosI','MakedoniaI', 'TiposThessalonikisI','KontraNewsI', 'ToParonI','FreeSundayI','ToXwniI','PressTimeI', 'KarfiI',\
					'LogosI','StarPressI', 'EloraI','ParaskinioI','ArthroI','GPrinI','KarfitsaI','DimokratiaI','ApopsiI','HNautemporikiI','HmerhsiaI','GEpoxiI',\
					'XrhmatisthrioI','MetoxosI','DimoprasionI','DealNewsI','IhodimoprasionI','OikonomikiBEI','DimoprasiakiAI')


	# Local papers of the week
	topikes_efimerides = ('HAgonI','HNeoiAgonesI','HProinosLogosI','HAnexartitosI','TTaxydromosI','TEleutheriaI','TMagnisiaI','TProinosTyposI', \
					'TThessaliaI','NADimokratikiRodouI','NAKoiniGnomiI','NAKykladikiI','BAPolitisI','MTAgonasI','MTXronosI','MTNeaEgnatiaI',\
					'MTProinosTyposI','MTEleutheroVimaI','MTNeaKastoriaI','MTSimeriniSerI','MTHmerhsiaVI','PanelliniaBEI','KMParatiritsI',\
					'KMPoliteiaI','KPatrisI','KRethemniotikaI','KNeaKritiI','KAnatolhI','IEnimerosiI','IHmeraI','IHmerhsiosI','PPeloponnisosI' \
					,'PPatrisI','PGnomiI','PProtiI','DESyneidisiI','PAllagiI','PGegonotaI','PEleutheriaI','PProiniI','SLamiakosI','ASyneidhshI','AAttikoBhmaI',\
					'AXtyposI','EthnikosKirikasI')

	# Clear screen
	os.system('clear')

	# Welcome Message
	print("WELCOME TO THE PROTOSELIDA (FRONT PAGES) DOWNLOADER !")
	print("-----------------------------------------------------")
	print(" ")

	# Decision making follows
	answer = input("1. Would you like to enter an older date? (YES/[NO]): ")
	if answer == "YES" or answer == "yes":
		insertdate()
	else:
		autodate()

	# Choose if you want the local papers as well (43)
	topikes = input("2. Do you want the local newspapers of the day as well? (YES/[NO]): ")

	#	Call the downloading function
	for efimerida in efimerides_vdomadas:
		frmfrontpagesgr(efimerida,today,year)
	if topikes == "YES" or topikes == "yes":
		for efimerida in topikes_efimerides:
			frmfrontpagesgr(efimerida,today,year)
	print(" ")

if __name__ == "__main__":
	main()
