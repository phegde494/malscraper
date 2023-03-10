from bs4 import BeautifulSoup
import requests
import re
from csv import writer

url= "https://myanimelist.net/topanime.php" # Site we wanna scrape
page = requests.get(url) # Making our request

soup = BeautifulSoup(page.content, 'lxml')


shows = soup.find_all('tr', class_="ranking-list") # Get a list of shows (in dirty html format)

with open('shows.csv', 'w', encoding='utf8', newline='') as f: # Open up csv file and write data
    thewriter = writer(f)
    header = ['Title', 'Link', 'Rating', 'Length']
    thewriter.writerow(header)

    for show in shows:
        linkTag = show.find('td', class_="title al va-t word-break").find('div', class_="detail").find('div', class_="di-ib clearfix").find('h3', class_="hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3").a
        # Parse through html classes and find attributes
        link = linkTag['href'] #link to show's page
        title = linkTag.text # show's title

        rating = show.find('td', class_="score ac fs14").div.find('span').text #show's rating

        details = show.find('td', class_="title al va-t word-break").div.find('div', class_="information di-ib mt4").text
        others = details.split('\n')
        lengthString = others[1]
        length = re.findall(r'\d+', lengthString)[0] #show's episode length

        info = [title, link, rating, length]
        thewriter.writerow(info)




    
    