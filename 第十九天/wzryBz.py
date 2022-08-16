import requests
from bs4 import BeautifulSoup
import os

for i in range(1,11):
    print("正在爬取第{}页".format(str(i)))

    if i == 1:
        html = requests.get("http://www.netbian.com/s/wangzherongyaoyingxiong/index.htm")
    else:
        html = requests.get("http://www.netbian.com/s/wangzherongyaoyingxiong/index_{}.htm".format(str(i)))

    html.encoding = "gbk"
    # print(html.text)
    soup = BeautifulSoup(html.text,"lxml")
    imgUrls = soup.select(".list ul li a")
    for imgUrl in imgUrls:
        print(imgUrl["title"],"http://www.netbian.com/"+imgUrl["href"])
        imgData = requests.get("http://www.netbian.com/"+imgUrl["href"])
        imgData.encoding = "gbk"
        imgSoup = BeautifulSoup(imgData.text, "lxml")
        img = imgSoup.select_one(".pic p a img")
        title = img["title"]
        print(title,img["src"])
        if not os.path.exists("wzryBz"):  # 判断这个文件夹存不存在
            os.mkdir("wzryBz")  # 在当前目录下创建目录
        with open(r"wzryBz\{}.jpg".format(title), "wb")as f:
            f.write(requests.get(img["src"]).content)
            print(title, "下载完毕……")






