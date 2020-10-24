import requests
from bs4 import BeautifulSoup
import urllib


def foodCrawling(foodname):
    foodname = foodname.split('/')[0]
    print(foodname)
    url = "https://www.10000recipe.com" #만개의 레시피
    requrl = url +"/recipe/list.html?q=" + urllib.parse.quote(foodname) #한글 인코딩
    print(requrl)
    sourcecode = urllib.request.urlopen(requrl).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    link = soup.find_all(class_='common_sp_link')[2]['href'] #최 앞에 있는 레시피
    print(link)

    requrl = url + link #해당 식단의 레시피 페이지를 크롤링한다.
    req = urllib.request.Request(requrl)
    sourcecode = urllib.request.urlopen(requrl).read()
    soup = BeautifulSoup(sourcecode, "html.parser")
    
    source = []
    step = []

    res = soup.find('div', 'view2_summary st3')
    res = res.find('h3')
    title= res.get_text()
    res = soup.find('div','view2_summary_info')
    level = res.get_text().replace('\n','')
    res = soup.find('div', 'ready_ingre3')
    try:
        for n in res.find_all('ul'):
            for jae in n.find_all('li'):
                source.append(jae.get_text().replace('\n','').replace(' ',''))
    except (AttributeError):
        return

    res = soup.find('div', 'view_step')
    i =0
    for n in res.find_all('div', 'view_step_cont'):
        i += 1
        step.append(str(i) +'. ' + n.get_text().replace('\n',' '))
    
    return {"result": "success", "title" :title, "level" :level, "source": source, "step": step}


