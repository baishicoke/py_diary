from urllib.parse import urlparse   #解析url
from datetime import datetime       #计算时间
import time         #延迟/沉睡的
import requests

class Delay:
    def __init__(self,delay=3):
        self.delay = delay
        self.urls = {}
    def wait(self,url):
        netloc = urlparse(url).netloc
        print(netloc)
        lastOne = self.urls.get(netloc,False)
        if lastOne and self.delay > 0:
            sleepTime = self.delay - (datetime.now()-lastOne).seconds
            if sleepTime > 0:
                time.sleep(sleepTime)
        self.urls[netloc]=datetime.now()




if __name__ == '__main__':
    urls = ["https://www.baidu.com/"]*10
    d = Delay()
    # d.wait(urls[0])
    for url in urls:
        print(url)
        html = requests.get(url)
        d.wait(url)
        print(html.status_code)


