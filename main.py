import requests
from bs4 import BeautifulSoup as bs

KEYWORDS = {'дизайн', 'фото', 'web', 'Python*', 'DevOps*'}
URL = 'https://habr.com/ru/all/'


def parser(keyword, url):
    response = requests.get(url)
    response.raise_for_status()
    text = response.text
    soup = bs(text, 'html.parser')
    articles = soup.find_all('article')
    for article in articles:
        hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')
        hubs_text = {hub.text for hub in hubs}
        if keyword & hubs_text:
            title = article.find('h2')
            link = title.find('a').attrs.get('href')
            url = 'https://habr.com' + link
            title_text = title.text
            date = article.find('span', class_='tm-article-snippet__datetime-published')
            publish_date = date.find('time').attrs.get('title')
            print(f'{publish_date}, {title_text}, {url}')
            return


if __name__ == '__main__':
    parser(KEYWORDS, URL)
