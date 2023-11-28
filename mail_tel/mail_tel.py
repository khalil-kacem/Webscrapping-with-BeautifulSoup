from bs4 import BeautifulSoup 
import requests
import re

site = input("give me a url to search if it contains a mail or phone number : ")

emails=[]
tels=[]

r = requests.get(site)
src=r.content
soup=BeautifulSoup(src,"lxml")
for link in soup.find_all("a",attrs={"href":re.compile("^mailto:")}):
    emails.append(link.get("href"))
for tel in soup.find_all("a",attrs={"href":re.compile("^tel:")}):
    tels.append(tel.get("href"))

if (len(emails)==0):
    print("no email founded")
else:
    print(emails)

if (len(tels)==0):
    print("no tels founded")
else:
    print(tels)







