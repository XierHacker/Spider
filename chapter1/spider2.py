import urllib.request
import urllib.parse
import urllib.error
import urllib.response
req=urllib.request.Request(url="https://www.baidu.com/")
response=urllib.request.urlopen(req)
print("type of response:",response)
content=response.read()
print(content)
