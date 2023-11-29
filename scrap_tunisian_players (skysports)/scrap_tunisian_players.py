import requests 
from bs4 import BeautifulSoup 
import csv 
from itertools import zip_longest


players_name=[]
players_position=[]

path=requests.get("https://www.skysports.com/football/teams/tunisia/squad")
src=path.content
soup=BeautifulSoup(src,"html.parser")


m=soup.find_all("table",{"class","table -small no-wrap football-squad-table"})

for j in range(len(m)):
    tableofplayers=m[j].find_all("h6")
    for i in range(len(tableofplayers)):
        players_name.append(tableofplayers[i].text)
        players_position.append(m[j].get("title"))


players=[map(lambda x: [x], players_name),players_position]

players_details = zip_longest(*players, fillvalue='')
with open ("/Users/KHALIL/desktop/projects/playersoftunisia.csv","w",encoding='utf-8',newline='') as play:
    wr=csv.writer(play)
    wr.writerow(["name_of_players","position"])
    wr.writerows(players_details)
    print("file is created")


