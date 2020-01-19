import requests
from bs4 import BeautifulSoup
import re
import pandas

url = "https://www.imdb.com/list/ls068082370/"
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html , 'html.parser')

tags = soup.find_all("div",{"class" : "lister-item mode-detail"})

count = 1
List = []
for data in tags:
    d = {}
    d["Name"]=data.find("h3",{"class":"lister-item-header"}).text.replace(str(count)+".","").replace("\n","")
    try:
        d["Certificate"]=data.find("span",{"class":"certificate"}).text
    except:
        d["Certificate"] ="NONE"
    d["Total Time"]=data.find("span",{"class":"runtime"}).text.replace("\n","")
    d["Genre"]=data.find("span",{"class":"genre"}).text.replace("\n","")
    d["Rating"]=data.find("span",{"class":"ipl-rating-star__rating"}).text.replace("\n","")
    d["Total Votes"]=data.find("span",{"name":"nv"}).text.replace("\n","")
    #d["Total Gross"]=data.find("span",{"name":"nv" , "data-value":"28,341,469"}).text.replace("\n","")
    List.append(d)


df = pandas.DataFrame(List)
df.to_csv("ImDb Top 250 Movies.csv")






