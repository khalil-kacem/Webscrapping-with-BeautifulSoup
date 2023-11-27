import requests
from bs4 import BeautifulSoup
import pandas as pd

date = input("Give me a date in the following format MM/DD/YY: ")
page = requests.get(f"https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date={date}")

src = page.content
soup = BeautifulSoup(src, 'lxml')
matches_details = []
champion = soup.find_all("div", {"class", "matchCard"})


def get_match_info(champion):
    championship = champion.contents[1].find('h2').text.strip()
    print(championship)

    allmatches = champion.contents[3].find_all("div", {"class", "item"})
    nbofmatches = len(allmatches)
    print(nbofmatches)
    for i in range(nbofmatches):
        team_a = allmatches[i].find("div", {"class": "teamA"}).text.strip()
        print(team_a)
        team_b = allmatches[i].find("div", {"class": "teamB"}).text.strip()
        print(team_b)
        resultat = allmatches[i].find("div", {"class": "MResult"}).find_all('span', {"class", "score"})
        score = f"{resultat[0].text.strip()}:{resultat[1].text.strip()}"
        print(score)
        matchtime = allmatches[i].find("div", {"class": "MResult"}).find_all('span', {"class", "time"})
        time = f"{matchtime[0].text.strip()}"
        print(time)
        matches_details.append(
            {"match ": championship, "team a": team_a, "team b": team_b, "score ": score, "time ": time})


for i in range(len(champion)):
    get_match_info(champion[i])


keys = matches_details[0].keys()
df = pd.DataFrame(matches_details)
df.to_csv('match-details.csv', index=keys)
print("File created")
