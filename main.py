import requests
from bs4 import BeautifulSoup

url1 = 'https://landofgames.ru/articles/guides/22117-otvety-na-igru-5-bukv-v-tinkoff-s-6-oktjabrja-po-20-dekabrja.html'
url2 = 'https://between-us-girls.ru/5-bukv-tinkoff-segodnya-otvet/'


def get_request1():
    response = requests.get(url=url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('td').text
    request = soup.find('td').find_next('td').text
    print(f'Ресурс 1:\nНа {data}\nЗагаданное слово: {request}\n')


def get_request2():
    response = requests.get(url=url1)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = soup.find('h3').text
    request = soup.find('mark', class_='m3').text
    print(f'Ресурс 2:\nНа {data}\nЗагаданное слово: {request}')


if __name__ == '__main__':
    get_request1()
    get_request2()
