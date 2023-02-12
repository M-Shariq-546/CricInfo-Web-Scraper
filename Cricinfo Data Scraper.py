#Web Scrapping of ESPNCricInfo
import pandas as pd
from requests import get
from bs4 import BeautifulSoup

url = 'http://www.espncricinfo.com/rankings/content/page/211271.html'

response= get(url)

html_soup = BeautifulSoup(response.text , 'html.parser')

ranking = html_soup.find_all('table' , class_='StoryengineTable')

format = html_soup.find_all('div' , class_="ciPhotoContainer")[0].find_all('h3')

#image_tags = html_soup.find_all('img')
#urls = [img['src'] for img in image_tags]

for i , r in enumerate(ranking):
    res1 =print(format[i].text)
    res2 =print(ranking[0].caption.text)
    tr = r.find_all('tr')
    i=0
    for t in tr:
        if(i==0):
            search="th"
        else:
            search="td"
        
        for c in t.findChildren(search):
            res3 = print('{:40}'.format(c.text), end=" ")
        print()
        i+=1
    print("\n\n")


