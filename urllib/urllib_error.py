from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import socket

try:
    response = urlopen('https://cuiqingcai.com/index.htm')
except HTTPError as e:
    #print(e.reason, e.code, e.headers, sep='\n')
    print(repr(e))
except URLError as e:
    #print(e.reason)
    print('URLERROR......') 
    print(repr(e))
else:
    print('Request sucessfully')

try:
    response = urlopen('https://www.baidu.com', timeout=0.01)
except URLError as e:
    print(type(e.reason))
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
