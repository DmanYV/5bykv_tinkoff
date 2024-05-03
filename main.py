import requests
from bs4 import BeautifulSoup

url = 'https://landofgames.ru/articles/guides/22117-otvety-na-igru-5-bukv-v-tinkoff-s-6-oktjabrja-po-20-dekabrja.html'


def get_request():
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('h3').text
    request = soup.find('mark', class_='m3').text
    print(f'На {data}\nЗагаданное слово: {request}')


if __name__ == '__main__':
    get_request()
