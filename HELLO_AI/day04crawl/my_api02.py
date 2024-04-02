import os
import sys
import urllib.request
import requests
import json
client_id = "GxkwrxFbYvNOCMsXaGx_"
client_secret = "NN2nxjwaLx"
encText = urllib.parse.quote("장원영")
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

response_body = response.read()
txt = response_body.decode('utf-8')

myjson=json.loads(txt)
list=myjson['items']
for b in list:
    print(b['title'],end="\t")
    print(b['link'])
