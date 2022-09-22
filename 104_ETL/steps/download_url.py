import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


def download_url(root_url):
    url_in_taipei = []
    for i in range(1, 10):
        root_url_format = root_url.format(i)
        r = requests.get(root_url_format)
        soup = BeautifulSoup(r.text, 'html.parser')
        articles = soup.find_all('article', class_='js-job-item')
        for article in articles:
            a = article.find('a', class_='js-job-link')
            url = a.get('href')[2:]
            job_title = article.get('data-job-name').strip('\n')
            job_company = article.get('data-cust-name').strip('\n')
            job_address = article.find('ul', class_='b-list-inline b-clearfix job-list-intro b-content').text[:7]
            if '台北市' in job_address:
                url_in_taipei.append(url)
                # print('職稱: {}   公司名: {}    地址: {}'.format(job_title, job_company, job_address.strip()))
                print(url)
                print('*' * 20)
                # sleep(randint(5, 10))

    return url_in_taipei
