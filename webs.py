#! /usr/bin/env python3
import os
import string
import requests
folder = "/data/feedback"
url="http://external-ip/feedback/"
for filename in os.listdir(folder):
  f=os.path.join(folder, filename)
  file=open(f)
  d={}
  d["title"]=file.readline().strip()
  d["name"]=file.readline().strip()
  d["date"]=file.readline().strip()
  d["feedback"]= file.readline().strip()
  response = requests.post(url,data=d)
  print(response.ok,
  response.status_code)
  file.close()
