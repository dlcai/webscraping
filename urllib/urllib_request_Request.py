import urllib.request
import urllib.parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Host': 'httpbin.org'
}
# urlencode:百分号编码，把中文字符对应的utf-8三字节编码用hex字符串表示,每个字节前加%
data = bytes(urllib.parse.urlencode({'name':'丁'}), encoding='utf-8')
req = urllib.request.Request(url=url, headers=headers, data=data, method='POST')
response = urllib.request.urlopen(req)
#print(response.read().hex())
print(urllib.parse.urlencode({'name':'丁'}))
print(bytes(urllib.parse.urlencode({'name':'丁'}),encoding='utf-8'))
print(bytes(urllib.parse.urlencode({'name':'丁'}),encoding='utf-8').hex())
print(response.read().decode('utf-8'))
#print(response.read().decode('unicode_escape'))
#print('丁'.encode('utf-8'))
#print('丁'.encode('unicode_escape'))
