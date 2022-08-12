from urllib.parse import urljoin
import requests
class Robots:
    def __init__(self,url,Agent):
        self.url = url
        self.headers = {"User-agent":Agent}
        self.ends = "robots.txt"
        self.baseUrl = url
        # 执行url更新函数
        self.doUrl()

    def doUrl(self):
        url = self.url.split("/")
        url = "/".join(url[:3])
        url = urljoin(url, self.ends)
        self.url = url
    def getRobots(self):
        html = requests.get(self.url)
        #存储
        with open("robots.txt", "w", encoding="utf-8")as f:
            f.write(html.text)
        # 读取
        with open("robots.txt", "r", encoding="utf-8")as f:
            lines = f.readlines()
            flag = False
            domain = []
            for line in lines:
                line = line.strip().replace("\n", "")
                if self.headers["User-agent"] in line:
                    flag = True
                    continue
                elif line.startswith("Disallow"):
                    if flag is True:
                        domain.append(line.replace("Disallow:", ""))
                    elif line is None or line == "":
                        if flag is True:
                            break
            for d in domain:
                if d in self.baseUrl:
                    print("网站禁止你爬取")
                    return False
            return True

if __name__ == '__main__':
    url = "https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xb946899900018ad9&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=12&rsv_sug1=7&rsv_sug7=101&rsv_sug2=0&rsv_btype=i&prefixsug=python&rsp=4&inputT=2824&rsv_sug4=3421"
    agent = "Googlebot"
    r = Robots(url,agent)
    print(r.getRobots())


