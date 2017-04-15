import urllib.request
import urllib.parse
import urllib.error
import urllib.response
from bs4 import BeautifulSoup

request=urllib.request.Request(url="http://tech.qq.com/a/20170223/000339.htm")
response=urllib.request.urlopen(request)
bs=BeautifulSoup(response.read())
print(bs)
