from urllib.parse import urljoin
import requests

class Robots:
    def __init__(self,url,Agent):
        self.baseUrl=url
        self.url=url
        self.headers={'user-agent':Agent}
        self.ends='robots.txt'
        #执行URL更新函数
        self.doUrl()

    def doUrl(self):
        url = self.url.split('/')
        url = '/'.join(url[:3])
        url = urljoin(url, self.ends)
        self.url=url

    def getRobots(self):
        html = requests.get(self.url)
        #存储robots
        with open('robots.txt', 'w', encoding='utf8')as f:
            f.write(html.text)
        #读取robots
        with open('robots.txt', 'r', encoding='utf8')as f:
            lines = f.readlines()
            flag = False
            domain = []
            for line in lines:
                line = line.strip().replace('\n', '')
                if self.headers['user-agent'] in line:
                    flag = True
                    continue
                elif line.startswith('Disallow'):
                    if flag is True:
                        domain.append(line.replace('Disallow: ',''))
                elif line is None or line == '':
                    if flag is True:
                        break
        for d in domain:
            if d in self.baseUrl:
                print('网站禁止你爬取')
                return False
        return True

if __name__ == '__main__':
    url='https://www.baidu.com'
    agent='Googlebot'
    r=Robots(url,agent)
    print(r.getRobots())