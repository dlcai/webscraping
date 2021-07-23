from urllib.robotparser import RobotFileParser
from urllib.request import Request, urlopen

url = 'https://www.jianshu.com/robots.txt'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) ' +\
        'AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15',
}

rp = RobotFileParser()
#rp.set_url(url)
#rp.read()
req = Request(url=url, headers=headers)
rp.parse(urlopen(req).read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'https://www.jianshu.com'))
print(rp.can_fetch('Cliqzbot', 'https://www.jianshu.com'))
print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'https://www.jianshu.com/search?q=python&page=l&type=collections'))


