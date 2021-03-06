#!/usr/bin/env python

import cmd
import re
import sys
import string
import urllib2

from config.configure import Configure
from lib.parser import Parser
from config.settings import *

class CLI(cmd.Cmd):
  
	def __init__(self):
		cmd.Cmd.__init__(self)
		self.prompt = CLI_PROMPT
		self.intro = "\n" + VERSION_STRING
		self.intro += "\n" + DESCRIPTION
		self.intro += "\n\t" + AUTHOR + " (" + ML + ")"
		self.intro += "\n\t" + SITE + "\n"
		self.ruler = '-'
		self.uws = Configure()
	
	def do_info(self, line):
		print "All variable"
	
	def do_show(self, line):
		if line and line in SHOW_OPTIONS:
			greeting = 'hi, %s!' % line
		elif line:
			greeting = self.uws.getUrl()
		else:
			greeting = 'URL\t=>\t' + self.uws.getUrl()

		p = Parser()
		p.checkParameter(self.lastcmd.split())
		print greeting
	
	def complete_show(self, text, line, begix, endidx):
		if not text:
			completions = SHOW_OPTIONS[:]
		else:
			completions = [ f
							for f in SHOW_OPTIONS
							if f.startswith(text)
							]
		return completions
	
	def do_run(self, line):
		self.mailExp = re.compile(MAIL_REGEX)
		self.mailList = self.mailExp.findall(self.uws.getWeb())
		self.mailListDebug = list(set(self.mailList))
		print self.mailListDebug

	def help_run(self):
		print '\n'.join([ '\nUsage:', 
						   '\trun ',
						   '\nDescription:',
                           '\tExecute User Web Scan for value set.\n',
                           ])

	def do_quit(self, line):
		return True

	def do_exit(self, line):
		return True
	
	def do_set(self, person):
		if person and person in SET_OPTIONS:
			greeting = 'hi, %s!' % person
		elif person:
			greeting = "hello, " + person
		else:
			greeting = 'hello'

		p = Parser()
		print p.checkParameter(self.lastcmd.split())
		if (p.checkParameter(self.lastcmd.split()) == True):
			self.uws.setUrl(p.returnParameter(2))
		print p.countParameter(self.lastcmd.split())
		print greeting
	
	def complete_set(self, text, line, begix, endidx):
		if not text:
			completions = SET_OPTIONS[:]
		else:
			completions = [ f
							for f in SET_OPTIONS
							if f.startswith(text)
							]
		return completions

	def help_set(self):
		print '\n'.join(['\nUsage:', 
						'\tset url <URL site>', 
						'\tset search <email | google | twitter | facebook>',
						'\tset verbose <True | False>', 
						'\nDescription:',
						'\tConfigure url scan and mode verbose.\n'])
	
	def do_get(self, person):
		if person and person in SET_OPTIONS:
			greeting = 'hi, %s!' % person
		elif person:
			greeting = "hello, " + person
		else:
			greeting = 'hello'

		p = Parser()
		print p.checkParameter(self.lastcmd.split())
		print greeting
	
	def complete_get(self, text, line, begix, endidx):
		if not text:
			completions = SET_OPTIONS[:]
		else:
			completions = [ f
							for f in SET_OPTIONS
							if f.startswith(text)
							]
		return completions

	def help_get(self):
		print '\n'.join(['\nUsage:', 
						'\tget url', 
						'\tget verbose', 
						'\nDescription:',
						'\tConfigure url and mode verbose.\n'])

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
