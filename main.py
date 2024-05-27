import requests
from bs4 import BeautifulSoup

url1 = 'https://landofgames.ru/articles/guides/22117-otvety-na-igru-5-bukv-v-tinkoff-s-6-oktjabrja-po-20-dekabrja.html'
url2 = 'https://between-us-girls.ru/5-bukv-tinkoff-segodnya-otvet/'


def get_date():
    response = requests.get(url=url1)
    soup = BeautifulSoup(response.text, 'html.parser')
    date = soup.find('h3').text
    return date


def get_response1():
    response = requests.get(url=url1)
    soup = BeautifulSoup(response.text, 'html.parser')
    word = soup.find('mark', class_='m3').text
    return word[0].upper() + word[1:].lower()


def get_response2():
    response = requests.get(url=url2)
    soup = BeautifulSoup(response.text, 'html.parser')
    word = soup.find('td').find_next('td').text
    return word


def request():
    if get_response2().lower() == get_response1().lower():
        print(f'На {get_date()}\nЗагаданное слово: {get_response2()}')
    else:
        print(f'На {get_date()}\nЗагаданное слово: {get_response1()}')


if __name__ == '__main__':
    request()
