import requests
from time import sleep
from random import randint
import os
from bs4 import BeautifulSoup
import json


def write_to_json(data, url):
    url = url.split('?')[0].split('/')[-1]
    filepath = os.path.join('./downloads/jobs/', url + '.json')
    with open(filepath, 'w+', encoding='utf-8') as f:
        data = json.dumps(data)
        f.write(data)


def download_content(url_list):
    if url_list == []:
        print('---- No new data have to download ----')
        raise Exception
    else:
        data = {}
        for url in url_list:
            http_url = 'http://' + url
            r = requests.get(http_url)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'html.parser')
                name = soup.find('title').text
                title_list = name.split('－')[0].split('｜')
                print(title_list)
                try:
                    data['職稱'] = title_list[0]
                    data['公司名'] = title_list[1]
                    data['上班地點'] = title_list[2]
                except IndexError:
                    pass
                ps = soup.find('p', class_='mb-5 r3 job-description__content text-break')
                data['工作內容'] = [x for x in ps.text.split('\n') if x != '']

                exp = soup.find('div', class_='job-requirement-table row')
                exp = exp.text.split()  # 工作經歷、學歷等
                exp_list = []
                try:
                    for i in range(0, len(exp), 2):
                        after_edit = exp[i] + ':' + exp[i + 1]
                        exp_list.append(after_edit)
                except IndexError:
                    pass
                data['條件要求'] = [x for x in exp_list if x != '']
                # pprint(data)
                sleep(randint(3, 8))
                write_to_json(data, url)

                print('============= Download Complete =============')
            else:
                print('============= Request Denied =============')
    return data
