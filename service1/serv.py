#!/usr/bin/python
# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import time
import cgi
import re
import argparse
import operator

# Управляет разбором аргументов программы
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', '--port', default=8881, type=int) # порт для запуска сервера
    return parser

parser = createParser()
namespace = parser.parse_args()
rrCount = 0
hashCount = 0

def incRRC():
   global rrCount
   rrCount += 1
   return rrCount

def incHC():
   global hashCount
   hashCount += 1
   return hashCount

class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        from urlparse import parse_qs
        sp = self.path
        print('path')
        print(sp)
        processRequest(self, sp, rrCount, hashCount) 

def processRequest(self, sp, rrCount, hashCount):
    startTime = time.time()
    data = None
    errorCode = None
    contentType = None
    if (sp == '/round-robin'):
        rrCount = incRRC()
        errorCode = 200
        contentType = "text; charset=utf-8"
	print("RoundRobinCount: " + str(rrCount))
        data = ''
    elif(sp == '/round-robin/stat'):
	errorCode = 200
        contentType = "text; charset=utf-8"
        data = str(rrCount)
    elif(sp == '/hash'):
	errorCode = 200
	#hashCount += 1
	hashCount = incHC()
	print("HashCount: " + str(hashCount))
        contentType = "text; charset=utf-8"
        data = ''
    elif(sp == '/hash/stat'):
	errorCode = 200
        contentType = "text; charset=utf-8"
        data = str(hashCount)
    elif(sp == '/query'):
	errorCode = 200
	time.sleep(100)
        contentType = "text; charset=utf-8"
        data = ''
    else:
        errorCode = 400
        data = 'Can not find parameter'
        contentType = "Content-type", "text; charset=utf-8"
    self.send_response(errorCode)
    self.send_header("Content-type", contentType)
    self.send_header("Content-Length", str(len(data)))
    self.end_headers()
    print('Returns: ' + data)
    self.wfile.write(data)
    print "processed in " + str(time.time() - startTime) + " seconds."
    

def init(port):
    print 'Starting server'
    serv = HTTPServer(("0.0.0.0", port), HttpProcessor)
    serv.serve_forever()

def main(argv):
    usageStr = 'Usage: serv.py --port <port>'
    port = namespace.port
    print 'port is:', port
    init(port)

if __name__ == "__main__":
    main(sys.argv[1:])
