import requests
from bs4 import BeautifulSoup
html = requests.get("https://finance.sina.com.cn/")
html.encoding = "utf8"
soup = BeautifulSoup(html.text,"lxml")
#大标题
bigTitle = soup.select("#blk_hdline_01 h3 a")
for bg in bigTitle:
    print("大标题：",bg.text)
    print("链接：",bg["href"])
print("-"*60)
#小标题
smellTitle = soup.select("#blk_hdline_01 p a")
for st in smellTitle:
    print("小标题：",st.text)
    print("链接：",st["href"])
print("-"*60)
#证券
zq = soup.select(".m-p1-mb2-list.m-list-container ul li a")
for z in zq:
    print("证券标题：",z.text)
    print("链接：",z["href"])
    # 进入链接爬取文本内容
    innerHtml = requests.get(z["href"])
    innerHtml.encoding = "utf8"
    soup2 = BeautifulSoup(innerHtml.text,"lxml")
    articles = soup2.select("div .article p")
    str = ""
    for article in articles:
        str += article.text
    print(str)
    print("-" * 30)





