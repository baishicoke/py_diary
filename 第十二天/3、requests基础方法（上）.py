import requests
import pprint
# html = requests.get('https://baidu.com')
# print(html.text)
# pprint.pprint(html.text)


# html = requests.post('http://httpbin.org/post', data = {'name':'ajiu',"pwd":"11111"})
# print(html.text)


# payload = {'wd': 'python'}
# html = requests.get("https://www.baidu.com/s", params=payload)
# print(html.url)
#
# html.encoding = "UTF-8"
# print(html.text)
#二进制  图片 音乐 视频
# img = requests.get("https://img2.baidu.com/it/u=1792249350,650626052&fm=253&fmt=auto&app=120&f=JPEG?w=1200&h=675")
# with open("img.jpg","wb")as f:
#     f.write(img.content)

# from PIL import Image
# from io import BytesIO
# img = requests.get("https://img2.baidu.com/it/u=1792249350,650626052&fm=253&fmt=auto&app=120&f=JPEG?w=1200&h=675")
# i = Image.open(BytesIO(img.content))
# print(i)

#json



# url = "https://image.baidu.com/search/index?tn=resulttagjson&logid=7739824637303557590&ie=utf-8&fr=&word=图片壁纸&ipn=r&fm=index&pos=history&queryWord=图片壁纸&cl=2&lm=-1&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=true&pn=0&rn=30&itg=1&gsm=1e&1659013693836="
# headers = {
# "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0"
# }
#
# r = requests.get(url,headers=headers)
#
# print(r.headers)

# if r.status_code == 200:
#
#     # print(r.json()["middlers"])
#     for i in r.json()["middlers"]:
#         print(i[1])


requests.get('http://baidu.com', timeout=1)




