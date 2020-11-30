import hashlib as cip
import requests as req
from bs4 import BeautifulSoup as col
import os
import time as t
os.system('cls')

#172 + 20
url = 'http://167.71.139.198:30626'
for a in range(10):
    t01 = t.time()
    tmp01 = req.get(url)
    print (tmp01.text)
    print ('----------------------------')
    key = tmp01.text[167:187]
    md5 = cip.md5(key.encode()).hexdigest()
    #t02 = t.time()
    #print (key, md5, abs(t01-t02))
    
    cook = {'PHPSESSID':'1gpeks0798qe6vorm9k38e73c0'}
    dat = {'hash':md5}
    var04 = req.post(url, data=dat, cookies=cook)
    t02 = t.time()
    print ('get/post', abs(t01-t02))
    print (var04.text)
    print (key, md5)
    print ('****************************')
