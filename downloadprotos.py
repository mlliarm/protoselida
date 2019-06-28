# encoding=utf8
__author__ = "milia"
__email__ = "milia@protonmail.com"
__licence__ = "GPL v.2"

import datetime
import wget
import os
from datetime import date
import calendar
import urllib
import time

def frmfrontpagesgr(efimerida, today, year):
	""" Downloads the newspaper images from the webpage """
	try:		
		url = 'https://www.frontpages.gr/d/' + today + '/' + str(efimerida.encode('utf-8')) + '.jpg'
		print(url)
		urllib.request.urlopen(url)
		wget.download(url)
		oldname = efimerida + '.jpg'
		newname = today + "_" + "FrontpagesGR" + "_" + oldname
		os.rename(oldname, newname)
	except urllib.error.HTTPError as e:
		#print(e.code)
		print("ERROR 404: Paper " + efimerida + " not found !")
		print(" ")
	except urllib.error.HTTPError as e:
		print(e.args)

def insertdate():
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

def autodate():
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

def main():
	""" Main function that has the names of the newspapers and calls the previous functions """
	# Main papers
	efimerides_vdomadas =('1/Η-Καθημερινή','2/Τα-Νέα', '5/Έθνος', '72/Η-εφημερίδα-των-συντακτών', '13/Αυγή', '9/Ριζοσπάστης','10/Ελεύθερος-Τύπος','6/Espresso','24/Αγγελιοφόρος',
                              '45/Θεσσαλονίκη','504/Kontra-News','26/Εστία','27/Ελεύθερη-ώρα','34/Δημοκρατία','80/Η-Ναυτεμπορική', '87/Χρηματιστήριο','98/Ηχώ-των-Δημοπρασιών' )


	# Local papers of the week
	topikes_efimerides = ('102/Πρωινός-Λόγος', '105/Ταχυδρόμος', '109/Ελευθερία', '133/Πρωινός-Τύπος', '405/Διάλογος', '406/Θεσσαλία', '148/Κοινή-Γνώμη', '418/Κυκλαδική',
                              '113/Ο-Πολίτης', '439/Νέα-Εγνατία', '419/Τύπος-Χαλκιδικής', '131/Σημερινή-των-Σερρών', '303/Ημερησία', '413/Παρατηρητής', '431/Πολιτεία', '140/Πατρίς',
                              '141/Ρεθεμνιώτικα-Νέα', '146/Νέα-Κρήτη', '409/Ανατολή', '151/Ημέρα-Ζακύνθου', '152/Ημερήσιος', '166/Πελοπόννησος', '165/Πατρίς', '160/Η-Γνώμη',
                              '164/Πρώτη', '162/Ελευθερία', '415/Πρωινή-Ηλείας', '175/Λαμιακός-Τύπος')

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
