import hashlib as cip
import requests as req
import time
from bs4 import BeautifulSoup
import os

url_recursos	= '#'
url_destino		= '#'

def getFromTag(respuesta):
	listTAG = BeautifulSoup(respuesta.text, 'html')
	for TAG in listTAG.find_all(["h3"]):
		return TAG.text



os.system('clear')
intentos = 2
for a in range(intentos):
	respuesta = req.get(url_recursos)
	respuesta = getFromTag(respuesta)
	hashRES = respuesta	
	
	#dat = {'hash':cip.md5((respuesta.text).encode()).hexdigest()}
	dat = {'hash':hash}
	
	respuesta = req.post(url_destino, data=dat)
	print (respuesta.text)