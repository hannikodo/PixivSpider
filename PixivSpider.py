from bs4 import BeautifulSoup
import requests
from urllib.request import urlretrieve


class PixivSpider(object):
    def __init__(self, date):
        self.net = 'https://www.pixiv.net/'
        self.dailyRankingUrl = 'https://www.pixiv.net/ranking.php?mode=daily?date={}'.format(date)
        self.urlDict = {}

    @staticmethod
    def parse(self):
        print(self.dailyRankingUrl)
        req = requests.get(self.dailyRankingUrl, )
        print("after req1")
        soup = BeautifulSoup(req.text, 'lxml')
        print(soup)
        print("after soup1")
        top50 = soup.find_all("section", class_="ranking-item")
        print("find succeed")
        for x in range(len(top50)):
            page = self.net + top50[x].find('a')['href']
            open_url = requests.get(page)
            each = BeautifulSoup(open_url.text).find('div', class_='img-container').find('img')['src']
            print(each)
            self.urlDict['#'+str(x)] = self.net + each
        print(self.urlDict)

    @staticmethod
    def download(self, path):
        print("download begin ...")
        for val, key in self.urlDict.items():
            urlretrieve(key, path + '/' + val + '.png')

    def run(self, path):
        self.parse(self)
        self.download(self, path)
