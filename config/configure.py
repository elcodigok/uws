#!/usr/bin/env python

import urllib2

class Configure:

	def __init__(self):
		self.url = None
		self.verbose = False
		self.html = None

	def getUrl(self):
		return self.url

	def setUrl(self, url):
		self.url = url
	
	def getWeb(self):
		web = urllib2.urlopen(self.getUrl())
		self.html = web.read()
		web.close()
		return self.html

	def getVerbose(self):
		return self.verbose

	def setVerbose(self, state):
		self.verbose = state
