from bs4 import BeautifulSoup
import requests
from csv import writer

url= "https://myanimelist.net/topanime.php"
page = requests.get(url)
print(page)

soup = BeautifulSoup(page.content, 'lxml')


shows = soup.find_all('tr', class_="ranking-list")

for show in shows:
    linkTag = show.find('td', class_="title al va-t word-break").find('div', class_="detail").find('div', class_="di-ib clearfix").find('h3', class_="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3").a
    link = linkTag['href']
    title = ""
    for c in linkTag:
        title += c
    
    