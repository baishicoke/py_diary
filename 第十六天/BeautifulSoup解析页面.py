from bs4 import BeautifulSoup
import requests
headers = {
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
html = requests.get("https://book.douban.com/",headers=headers)
soup = BeautifulSoup(html.text,"lxml")
# tbody = soup.select("div h2")
# # print(tbody)
# for t in tbody:
#     print(t.text)

# tbody = soup.select("title")
# print(tbody)

# tbody = soup.select_one("div h2")
# print(tbody)


tbody = soup.select("li .info .title a")
# print(tbody)
for t in tbody:
    print(t.text)
