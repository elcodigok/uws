#!/usr/bin/env python 

from config.settings import *

class Parser:
	def __init__(self):
		self.parameter = None
		self.valid = False
	
	def checkParameter(self, parameter):
		self.parameter = parameter
		# value 0 => command
		if (self.parameter[0] in SHOW_ORDER):
			# value 1 => order
			if (self.parameter[1] in SET_OPTIONS):
				# value 2..n => value
				print self.parameter[2]
				self.valid = True
			else:
				self.valid = False
		else:
			self.valid = False
		
		return self.valid
	
	def countParameter(self, parameter = []):
		self.parameter = parameter
		return len(self.parameter)