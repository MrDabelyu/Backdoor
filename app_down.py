import requests
import os
import bs4
import json

listdir = os.listdir("/mnt/sda3/Project/apps/")
listapp = json.loads(str(open("linkapp.txt", "r").read()))

def checkUp(apk,ls):
  for apps in apk:
     title = str(bs4.BeautifulSoup(requests.get(apk[apps]).content, "html.parser").find('title'))  
     ver = title[title.find("latest")+7:title.find("Android")-1]
     if str(ls).find(ver) == -1:
        print("Updating " + str(apps) +"...")
        getLink(apk,apps)
     else:
        print(str(apps)+" Already Lastest!")

def getLink(apk,apps):
  linkapp = str(bs4.BeautifulSoup(requests.get(apk[apps]).content, "html.parser").find(class_="ga"))
  linkapp = linkapp[linkapp.find("href=")+5:linkapp.find("id=")-1]
  download(linkapp)

def download(link):
  os.system("cd /mnt/sda3/Project/apps/ && wget --no-check-certificate --content-disposition " + link )

checkUp(listapp,listdir)