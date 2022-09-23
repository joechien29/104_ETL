import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint


def existed_url_list():
    existed_url = []
    try:
        with open('downloads/jobs/urls_list', 'r', encoding='utf-8') as f:
            for line in f:
                existed_url.append(line.strip())
            print('Existed_URL: ', len(existed_url))
    except FileNotFoundError:
        print('---- no existed url ----')
    return existed_url


def download_url(root_url, existed_url):
    with open('downloads/jobs/urls_list', 'a+', encoding='utf-8') as f:
        url_need_download = []
        for i in range(1, 10):
            print(f'----- Downloading Page {i}')
            root_url_format = root_url.format(i)
            r = requests.get(root_url_format)
            soup = BeautifulSoup(r.text, 'html.parser')
            articles = soup.find_all('article', class_='js-job-item')
            for article in articles:
                a = article.find('a', class_='js-job-link')
                url = a.get('href')[2:]
                id_url = url.split('?')[0]
                if id_url in existed_url:
                    print(' ---- existed url ----')
                    continue
                # job_title = article.get('data-job-name').strip('\n')
                # job_company = article.get('data-cust-name').strip('\n')
                else:
                    job_address = article.find('ul', class_='b-list-inline b-clearfix job-list-intro b-content').text[:7]
                    if '台北市' in job_address:
                        url_need_download.append(id_url)
                        f.write(id_url + '\n')
                        # print('職稱: {}   公司名: {}    地址: {}'.format(job_title, job_company, job_address.strip()))
                        print(id_url)
                        sleep(randint(1, 4))
    return url_need_download
