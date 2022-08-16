import requests
from bs4 import BeautifulSoup
import os

for i in range(1,11):
    print("正在爬取第{}页".format(str(i)))

    html = requests.get("https://pro.58pic.com/psearch/78672461-%E5%9B%BD%E6%BD%AE-0-0-0-p{}.html".format(str(i)))
    soup = BeautifulSoup(html.text,"lxml")
    imgUrls = soup.select(".qtw-card.qtw-card-pro.qtas-pic-card.qtw-card-pro-normal.item a")
    for imgUrl in imgUrls:
        # print(imgUrl["title"],"https:"+imgUrl["href"])
        imgData = requests.get("https:"+imgUrl["href"])
        imgSoup = BeautifulSoup(imgData.text,"lxml")
        img = imgSoup.select_one(".main img")
        title = img["title"]
        print(title,"https:"+img["src"])
        if not os.path.exists("qt"): #判断这个文件夹存不存在
            os.mkdir("qt") #在当前目录下创建目录
        with open(r"qt\{}.jpg".format(title),"wb")as f:
            f.write(requests.get("https:"+img["src"]).content)
            print(title,"下载完毕……")
