import requests 
from bs4 import BeautifulSoup 
import csv 
from itertools import zip_longest

job_title = []
society = []
place = []
describe = []
date = []
links = []


nb = 0
ok = True

while True and ok:
    try:
        path = requests.get(f"https://wuzzuf.net/search/jobs/?a=hpb&q=python&start={nb}")
        src = path.content
        soup = BeautifulSoup(src, "lxml")
        nbofjobs = int(soup.find("strong").text)
        
        if nb > nbofjobs // 15:
            print("page terminated ")
            print(nb)
            ok = False

        job_titles = soup.find_all("h2", {"class", "css-m604qf"})
        societys = soup.find_all("a", {"class", "css-17s97q8"})
        places = soup.find_all("span", {"class", "css-5wys0k"})
        describes = soup.find_all("div", {"class", "css-y4udm8"})
        datesnew = soup.find_all("div", {"class", "css-4c4ojb"})
        datesold = soup.find_all("div", {"class", "css-do6t5g"})

        posted = [*datesnew, *datesold]

        for i in range(len(job_titles)):
            job_title.append(job_titles[i].text)
            society.append(societys[i].text)
            place.append(places[i].text)
            describe.append(describes[i].text)
            date.append(posted[i].text)
            links.append(job_titles[i].find("a").attrs["href"])

        nb += 1
        print("page switched")

    except Exception as e:
        print(f"An error occurred while scraping job list: {e}")

listfile = [job_title, date, society, place, describe, links]

exp = zip_longest(*listfile, fillvalue='')

with open("/Users/KHALIL/desktop/projects/wuzzuf.csv", "w", encoding='utf-8', newline='') as myfile:

    wr = csv.writer(myfile)
    wr.writerow(["jobtitle", "date", "society", "place", "describe", "links"])
    wr.writerows(exp)
    print("file created")
