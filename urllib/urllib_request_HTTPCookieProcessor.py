from urllib.request import HTTPCookieProcessor, build_opener
from http.cookiejar import CookieJar, MozillaCookieJar, LWPCookieJar

def iterate_cookie_jar(cookie_jar):
    if len(cookie_jar) == 0:
        print('empty cookie jar')
    for cookie in cookie_jar:
        print(cookie.name + '=' + cookie.value)

cookie_jar = CookieJar() # Cookie对象的集合
handler = HTTPCookieProcessor(cookie_jar)
opener = build_opener(handler)

print('cookie jar before request:')
iterate_cookie_jar(cookie_jar)

response = opener.open('http://www.baidu.com')
print(response.status)
print('Response Header Set-Cookie:', response.getheader('Set-Cookie'), sep='\n')
print('cookies after request 1:')
iterate_cookie_jar(cookie_jar)

response2 = opener.open('http://www.baidu.com')
print(response2.status)
print('Response2 Header Set-Cookie:', response2.getheader('Set-Cookie'), sep='\n')
print('cookies after request 2:')
iterate_cookie_jar(cookie_jar)

# 用MozillaCookieJar把cookie保存为cookies.txt 
filename = 'cookies.txt'
m_cookie_jar = MozillaCookieJar(filename)
handler = HTTPCookieProcessor(m_cookie_jar)
opener = build_opener(handler)
response = opener.open('http://www.baidu.com')
m_cookie_jar.save(ignore_discard=True, ignore_expires=True) #标记为丢弃和过期的cookie也保存

#保存为LWP格式(Set-Cookie3, 兼容libwww-perl, human-readable)
filename = 'cookies_LWP.txt'
lwp_cookie_jar = LWPCookieJar(filename)
handler = HTTPCookieProcessor(lwp_cookie_jar)
opener = build_opener(handler)
response = opener.open('http://www.baidu.com')
lwp_cookie_jar.save(ignore_discard=True, ignore_expires=True) 



     

