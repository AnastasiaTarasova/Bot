import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('Films.csv', 'a', encoding="utf8", newline='') as f:
        writer = csv.writer(f)

        writer.writerow((
                         data['title'],
                         data['url'],
                         data['date'],
                         data['genre'],
                         data['description']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', class_='results').findAll('div', class_='item poster card')


    for ad in ads:

                #title, genres,overview
        try:
            title = ad.find('p', class_='flex').find('a').get('title')
        except:
            title = ''
        try:
            url = 'https://www.themoviedb.org' + ad.find('p', class_ = 'flex').find('a').get('href')
        except:
            url = ''
        try:
            date = ad.find('p', class_ = 'meta flex').find('span', class_ = 'release_date').text
        except:
            date = ''
        try:
            genre = ad.find('p', class_ = 'meta flex').find('span', class_ = 'genres').text.split()#насчет сплита я не уверенна
        except:
            genre = ''
        try:
            description = ad.find('p', class_ = 'overview').text
        except:
            description = ''



        data = {'title': title, 'url': url,'date': date, 'genre': genre, 'description': description}
        write_csv(data)


def main():
    url = 'https://www.themoviedb.org/movie?page=1'
    page = 'https://www.themoviedb.org/movie?'
    page_part = 'page='

    for i in range(1, 980, 1):
        url_gen = page + page_part + str(i)
        print(url_gen)

        html = get_html(url_gen)
        get_page_data(html)


if __name__ == '__main__':
    main()
