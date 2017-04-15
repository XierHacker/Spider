import urllib.request
import urllib.parse
import urllib.error
import urllib.response
from bs4 import BeautifulSoup
import re
import sys
import os
import os.path

def getPic(url):
    user_agent="Chrome/49.0.2623.22"
    referer="https://t66y.com/thread0806.php?fid=16&search=&page=1"
    headers = {"User-Agent":user_agent,"Referer":referer }
    try:
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
    except urllib.error.HTTPError as e:
        print("we got a http error:",e)

    else:
        bs = BeautifulSoup(response.read())
        titlelist = bs.find_all(name="title")
        title=titlelist[0].get_text()
        linklist = bs.find_all(name="input", attrs={"src": re.compile(".+\.jpg")})
        print(title)
        #make directory
        if os.path.exists(path=title):
            pass
        else:
            os.mkdir(path=title)
        #sava pic to disk
        i = 1
        for link in linklist:
            print(link["src"])
            try:
                urllib.request.urlretrieve(url=link["src"], filename=title+"/"+str(i) + ".jpg")
            except urllib.error.HTTPError as e:
                print("we get a problem",e)
                continue
            else:
                i += 1

def getLink(url,pages=2):
    print("---------收集链接中--------")
    headers = {"User-Agent": "Chrome/49.0.2623.22"}
    Linklist=[]
    for i in (1,pages+1):
        temp = url[:-1]
        temp+=str(i)
        try:
            request = urllib.request.Request(url=temp, headers=headers)
            response = urllib.request.urlopen(request)
        except urllib.error.HTTPError as e:
            print("we got a http error:", e)
            continue
        else:
            bs=BeautifulSoup(response.read())
            linklist=bs.find_all(name="h3")
            for link in linklist:
               rlink="https://t66y.com/"+link.contents[0]["href"]
               print("收集：",rlink)
               if rlink in Linklist:
                   pass
               else:
                   Linklist.append(rlink)
    Linklist=Linklist[11:]
    return Linklist

Links=getLink(url="https://t66y.com/thread0806.php?fid=16&search=&page=1")
for urls in Links:
    getPic(url=urls)







