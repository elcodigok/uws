#!/usr/bin/env python

# version y sitio
VERSION = "0.1"
VERSION_STRING = "Users Web Scan v%s" % (VERSION)
DESCRIPTION = "Search tool users information."
AUTHOR = "Daniel M. Maldonado"
SITE = "http://caceriadespammers.com.ar"
ML = "uws@elcodigok.com.ar"

CLI_PROMPT = 'uws> '

# Expresiones Regulares
MAIL_REGEX  = r'[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}'

GENERAL_IP_ADDRESS_REGEX = r'\A\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\Z'

SET_OPTIONS = [ 'url', 'verbose' ]

SHOW_ORDER = [ 'set', 'get' ]

SHOW_OPTIONS = [ 'url', 'verbose', 'options' ]
