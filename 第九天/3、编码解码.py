import urllib.request
url = "https://www.baidu.com"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)





