import requests
from bs4 import BeautifulSoup

url = 'https://landofgames.ru/articles/guides/22117-otvety-na-igru-5-bukv-v-tinkoff-s-6-oktjabrja-po-20-dekabrja.html'


def get_otvet():
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('h3').text
    otvet = soup.find('mark', class_='m3').text
    print(f'На {data}\nЗагаданное слово: {otvet}')


if __name__ == '__main__':
    get_otvet()
