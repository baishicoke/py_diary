from urllib.parse import urlparse   #解析url
from datetime import datetime       #计算时间
import time         #延迟/沉睡的
import requests

#403 访问频率会封IP
#ip代理池
class Delay:
    def __init__(self,delay=3):   #沉睡时间
        self.delay = delay
        self.urls = {}

    def wait(self,url):
        netloc = urlparse(url).netloc #获取域名
        print(netloc)
        lastOne = self.urls.get(netloc,False) #记录访问时间的
        if lastOne and self.delay > 0:
            # datetime.now() 本次访问的时间
            #lastOne 上次的访问时间   来减去他的时间差
            # .seconds 我们把它秒数取出来
            sleepTime = self.delay-(datetime.now()-lastOne).seconds
            if sleepTime > 0:
                time.sleep(sleepTime)

        self.urls[netloc]=datetime.now()
if __name__ == '__main__':
    urls = ["https://github.com/"]*10
    d = Delay()
    # d.wait(urls)
    for url in urls:
        html = requests.get(url)
        d.wait(url)
        print(html.status_code)
