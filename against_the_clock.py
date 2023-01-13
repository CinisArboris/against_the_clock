import hashlib as cip
import requests as req
import time
from bs4 import BeautifulSoup
import os

url_resour = '#'
url_destin = '#'

def getFromTag(xResponse):
	listTAG = BeautifulSoup(xResponse.text, 'html')
	for TAG in listTAG.find_all(["h3"]):
		return TAG.text

os.system('clear')
intentos = 2
for a in range(intentos):
	xResponse = req.get(url_resour)
	xResponse = getFromTag(xResponse)
	hashRES = xResponse	
	
	#dat = {'hash':cip.md5((xResponse.text).encode()).hexdigest()}
	dat = {'hash':hash}
	
	xResponse = req.post(url_destin, data=dat)
	print (xResponse.text)
