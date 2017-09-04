import os
import time
import PixivSpider

t = time.localtime(time.time() - 24*60*60)
date = '{date[0]}{date[1]:0>2}{day:0>2}'.format(
            date=[x for x in t],
            day=t[2]
        )
path = '/Users/hanniko/Pictures/SpiderPic/Pixiv/'+date

if not os.path.isdir(path):
    os.mkdir(path)
os.chdir(path)

spider = PixivSpider.PixivSpider(date)
spider.run(path)
