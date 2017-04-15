import urllib.request
import urllib.parse
import urllib.error
import urllib.response
response=urllib.request.urlopen(url="https://www.baidu.com/")
print("type of response:",response)
content=response.read()
print(content)
