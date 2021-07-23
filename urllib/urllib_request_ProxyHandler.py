from urllib.request import build_opener, ProxyHandler
from urllib.error import URLError

proxy_handler = ProxyHandler({
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080'
})
opener = build_opener(proxy_handler)

try:
    response = opener.open('http://www.baidu.com')
    print(response.status)
    print(response.getheaders())
except URLError as e:
    print(e.reason)
