import requests
from lxml import etree

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
# html = requests.get("https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4",headers=headers)
# soup = etree.HTML(html.text)
# 获取标签下直系的标签内容
# result = soup.xpath('//li/div/a/img/text()')
# 提取标签里的属性 比如src
# result = soup.xpath('//li/div/a/img/@src')
# print(result)
# for i in result:
#     print(i.replace("\n", ""))


# text = '''
# <div>
# 	<ul>
# 		<li class="item-0"><a href="link1.html">first item</a></li>
# 		<li class="item-1"><a href="link2.html">second item</a></li>
# 		<li class="item-inactive"><a href="link3.html">third item</a></li>
# 		<li class="item-1"><a href="link4.html">fourth item</a></li>
# 		<li class="item-0"><a href="link5.html">fifth item</a></li>
# 	</ul>
# </div>
# '''
#
# html = etree.HTML(text)
# 取第一个  相当于列表的 下标/索引
# result = html.xpath("//li[1]/a/text()")
# print(result)
# last()最后一个
# result = html.xpath("//li[last()]/a/text()")
# print(result)
# 根据运算符结果返回  position()<3  小于3的返回 所以只返回前两个
# result = html.xpath("//li[position()<3]/a/text()")
# print(result)
# 根据运算符结果返回  last()-2  共5个在本来的基础上减去2的返回 所以返回了第三个
# result = html.xpath("//li[last()-2]/a/text()")
# print(result)

# text = '''
# <li class="li li-first"><a href="link.html">fifth item</a></li>
# <li class="li li-fifth"><a href="link.html">fifth item</a></li>
# '''
# html = etree.HTML(text)
# result1 = html.xpath('//li[@class="li li-first"]/a/text()')
# print(result1)
# # 把匹配到的属性 含有指定字符的标签给返回来
# result2 = html.xpath('//li[contains(@class,"it")]/a/text()')
# print(result2)





