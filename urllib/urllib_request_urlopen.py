import urllib.request
import urllib.parse
import urllib.error
import socket

# urlopen默认实现GET请求
response = urllib.request.urlopen('https://www.python.org')
#print(type(response)) # http.client.HTTPResponse Object
#print(response.status)
#print(response.getheaders())
#print(response.getheader('Server'))

# 加入data参数，urlopen的请求变为POST方法
url_str = urllib.parse.urlencode({'word':'hello','单词':'你好'})  # percent-encoded ascii string
#print(type(url_str))
#print(url_str)  # url query part

data = bytes(url_str, encoding='utf-8')
r2 = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(r2.read().decode('utf-8'))

# timeout参数与异常处理
try:
    r3 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:  #运行结果：不会抛出URLError
    if isinstance(e.reason, socket.timeout):
        print('URLError reason: socket.timeout')
except urllib.error.HTTPError as e:
    print(e)
except socket.timeout as e: 
    print('socket.timeout (subclass of OSError): ', e)
    

        

