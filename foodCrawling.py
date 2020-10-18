import requests
from bs4 import BeautifulSoup
import urllib


def foodCrawling(foodname):
    url = "https://www.10000recipe.com" #만개의 레시피
    requrl = url +"/recipe/list.html?q=" + urllib.parse.quote(foodname) #한글 인코딩
    print(requrl)
    req = urllib.request.Request(requrl)
    sourcecode = urllib.request.urlopen(requrl).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    link = soup.find_all(class_='common_sp_link')[0]['href'] #최 앞에 있는 레시피
    print(link)

    requrl


foodCrawling("샌드위치")