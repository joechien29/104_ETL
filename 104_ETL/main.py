from steps.download_url import download_url
from steps.download_content import download_content
from settings import create_dir


root_url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7\
&keyword=%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%E5%B8%AB\
&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm\
&order=14&asc=0&sctp=M&scmin=30000&scstrict=1&scneg=0\
&s9=1&rostatus=2048&page={}&jobexp=1&mode=s&jobsource=2018indexpoc\
&langFlag=0&langStatus=0&recommendJob=1&hotJob=1'


def main():
    create_dir()
    url_list = download_url(root_url)
    download_content(url_list)


if __name__ == '__main__':
    main()
