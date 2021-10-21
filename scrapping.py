from bs4 import BeautifulSoup
import requests

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

URL = "https://habr.com"

response = requests.get("https://habr.com/ru/all/")
response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')
articles = soup.find_all("article", class_="tm-articles-list__item" )

for article in articles:
    try:
        article_header = article.find('h2', class_="tm-article-snippet__title tm-article-snippet__title_h2").text
        article_text = article.find("div", class_="article-formatted-body article-formatted-body_version-2").text
        hubs = article.find_all("a", class_="tm-article-snippet__hubs-item-link")
        hub_list = [hub.text.strip().lower() for hub in hubs]
        article_date = article.find("span", class_="tm-article-snippet__datetime-published").text
        article_link = URL + article.find("a",class_="tm-article-snippet__title-link").get("href")

        for word in KEYWORDS:
            if (word.lower() in article_header.lower()) or (word.lower() in article_text.lower()) or (word.lower() in hub_list):
                print(f"{article_date} - {article_header} - {article_link}")

    except AttributeError:
        None



