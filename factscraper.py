import requests
from bs4 import BeautifulSoup

def factgenerator():
        r=requests.get("http://facts.randomhistory.com/")
        soup=BeautifulSoup(r.content)
        data=soup.find_all("div",{"class":"home-text"})
        fact=""
        for item in data:
                fact=fact+item.text
        return fact.lstrip()

print factgenerator()
            
