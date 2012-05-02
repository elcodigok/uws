#!/usr/bin/env python

import cmd
import re
import sys
import string
import urllib2

from settings import *

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


class CLI(cmd.Cmd):
  
	SET_OPTIONS = [ 'url', 'verbose' ]
	SHOW_OPTIONS = [ 'url', 'verbose', 'options' ]

	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = 'uws> '
		self.intro = "\n" + VERSION_STRING
		self.intro += "\n" + DESCRIPTION
		self.intro += "\n\t" + AUTHOR + " (" + ML + ")"
		self.intro += "\n\t" + SITE + "\n"
		self.ruler = '-'
		self.uws = Configure()
	
	def do_info(self, line):
		print "All variable"
	
	def do_show(self, line):
		if line and line in self.SHOW_OPTIONS:
			greeting = 'hi, %s!' % line
		elif line:
			greeting = "hello, " + line
		else:
			greeting = 'hello'
		print greeting
	
	def complete_show(self, text, line, begix, endidx):
		if not text:
			completions = self.SHOW_OPTIONS[:]
		else:
			completions = [ f
							for f in self.SHOW_OPTIONS
							if f.startswith(text)
							]
		return completions
	
	def do_run(self, line):
		print "runnnnnnnnnn"

	def do_quit(self, line):
		return True

	def do_exit(self, line):
		return True
	
	def do_set(self, person):
		if person and person in self.SET_OPTIONS:
			greeting = 'hi, %s!' % person
		elif person:
			greeting = "hello, " + person
		else:
			greeting = 'hello'
		print greeting
	
	def complete_set(self, text, line, begix, endidx):
		if not text:
			completions = self.SET_OPTIONS[:]
		else:
			completions = [ f
							for f in self.SET_OPTIONS
							if f.startswith(text)
							]
		return completions


#web = urllib2.urlopen("http://code.google.com/p/python-twitter/")
#html = web.read()
#web.close()
#mailExp = re.compile(r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}')
#mailList = mailExp.findall(html)
#print "Mail scaneados %s" % (mailList)
#print "En total son: %s" % (len(mailList))

if __name__ == '__main__':
	CliUscanWeb = CLI()
	CliUscanWeb.cmdloop()
