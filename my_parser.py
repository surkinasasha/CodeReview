import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pytz

def today():
    time_zone = pytz.timezone('Asia/Yekaterinburg')
    current_date = datetime.now(time_zone).date()
    return current_date

def parse_n_plus_1():
    articles=[]
    nplus1 = requests.get("https://nplus1.ru/").text
    nplus1_html = BeautifulSoup(nplus1, 'html.parser')
    nplus1_current_date_material = "https://nplus1.ru/material/" + str(today()).replace("-","/")
    nplus1_current_date_news = "https://nplus1.ru/news/" + str(today()).replace("-","/")
    articles = []
    for article in nplus1_html.find_all("a"):
        link = article.get("href")
        if link.startswith(nplus1_current_date_material) or link.startswith(nplus1_current_date_news):
            if article.get_text() != None:
                title =article.get_text() 
                link = article.get("href")
                articles.append((title, link, str(today())))
    return articles

def parse_nkj():
    articles=[]
    nkj = requests.get("https://www.nkj.ru/news/").text
    nkj_html =  BeautifulSoup(nkj, 'html.parser')
    for article in nkj_html.find_all("article"):
        if article.find("time") != None:
            date = article.find("time").get("datetime")[:10]
            if (date == str(today())):
                if article.find("h2")!= None:
                    title = article.find("h2").find("a").get_text() 
                    link ="https://www.nkj.ru" + article.find("h2").find("a").get("href")
                    articles.append((title, link, str(today())))
    return articles

def sum_articles():
    return parse_n_plus_1() + parse_nkj()


