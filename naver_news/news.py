# -*- coding: utf-8 -*-
import requests
# from readability import Document
from bs4 import BeautifulSoup
url = "http://news.naver.com"
import pprint


def remove_duplicates(k):
    link_title_dict = dict()
    link_title = list(map(lambda item: link_title_dict.update(
        {item['link']: item['title']}), k))
    links = list(map(lambda item: item['link'], k))
    links = list(set(links))

    def myfilter(item):
        if len(item) == 0:
            return
        else:
            return {"link": item, "title": link_title_dict[item]}

    finals = list(map(lambda item: myfilter(item), links))

    return finals


class NaverNews:

    @staticmethod
    def get_newslist():
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        alist = soup.find_all(name="a")
        news_list = list()
        for a in alist:
            try:
                news_list.append({"title": a['title'], "link": a['href']})
            except:
                pass

        news_list = remove_duplicates(news_list)
        return news_list

    @staticmethod
    def get_article(link):
        res = requests.get(link)
        soup = BeautifulSoup(res.text, "html.parser")
        article = soup.find_all("div", attrs={"id": "articleBodyContents"})[0]
        return article.text
