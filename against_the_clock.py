import hashlib as cip
import requests as req
import time

url_recursos = '#'
url_destino = '#'



intentos = 10
for a in range(intentos):

	#a = time.time()
	respuesta = req.get(url_recursos)
	#b = time.time()
	#print (respuesta.text, abs(b-a))
	
	#a = time.time()
	dat = {'hash':cip.md5((respuesta.text).encode()).hexdigest()}
	respuesta = req.post(url_destino, data=dat)
	#b = time.time()
	print (respuesta.text)