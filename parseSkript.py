#!/usr/bin/env python
# coding: utf-8 

# intended for python 2.7 only

import mechanize
from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):

	def __init__(self,var):
		HTMLParser.__init__(self)
		self.read = var
		self.data = []
		self.depth = 0

	def handle_starttag(self, tag, attrs):
		if(len(attrs) != 0):
			if(tag == "div" and attrs[0] == ("class","search-results") ):
				self.depth += 1

		if(tag == "td" and self.depth == 1):
			#print("Encountered a start tag:", tag)	
			self.read = True

	def handle_endtag(self, tag):
		if(tag == "td"):
			self.read = False

			#print("Encountered an end tag :", tag)
	def handle_data(self, data):
		if(self.read):
			#if(handle_data):
			self.data.append(data)

def getParsedOutput(var):
	f = open('test.html','r')
	parser = MyHTMLParser(False)
	parser.feed(f.read().decode('utf-8'))

	myList = filter(filterInput, parser.data)

	for x in myList:
		print(x)

	print(myList)
	f.close()

def filterInput(myInput):
	if(myInput.split() != []):
		return True
	else:
		return False

def getOnlineBussinessData(firstName, lastName):
	br = mechanize.Browser() #initiating a browser
	br.set_handle_robots(False) #ignore robots.txt
	br.addheaders = [("User-agent","Mozilla/5.0")] #our identity

	bot = br.open("https://or.justice.cz/ias/ui/rejstrik-$osoba") #requesting the base url
	br.form = list(br.forms())[0]   
	br["jmeno"] = firstName #prijmeni
	br["prijmeni"] = lastName #jmeno
	#br["id1"] = password #datum narozeni
	response = br.submit()
	parser = MyHTMLParser(False)
	parser.feed(response.read().decode('utf-8'))
	myList = filter(filterInput, parser.data)
	for x in myList:
		print(x)

#getParsedOutput("wtf")
getOnlineBussinessData("Ivo","Valenta")