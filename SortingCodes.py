import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.geeksforgeeks.org/fundamentals-of-algorithms/")
soup=BeautifulSoup(r.content)

data=soup.find_all("div",{"class":"entry-content"})
codelinks=[]

for item in data:
    print item.contents[13].text
    print item.contents[15].text
    for links in item.contents[15].find_all("a"):
        codelinks.append(links.get("href"))
for link in codelinks:
    req=requests.get(link)
    csoup=BeautifulSoup(req.content)
    body=csoup.find_all("pre")
    for code in body:
        print code.text
