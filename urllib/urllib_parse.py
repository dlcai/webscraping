from urllib.parse import urlencode, parse_qs, parse_qsl
from urllib.parse import quote, unquote
from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit
from urllib.parse import urljoin

# urlencode(): dict -> % str
base_url = 'https://www.baidu.com?'
query_str =  urlencode({'name':'丁', 'age':'25'})
url = base_url + query_str
print(url)

# parse_qs(): parse query string back to dict
# parse_qsl(): parse query string back to tuple list
print(parse_qs(query_str))
print(parse_qsl(query_str))

# quote(): 中文str -> % str
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
print(unquote(url))

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
# urlunparse(): 参数是长度为6的可迭代对象
data = ['http', 'www.baidu.com', 'index.html', 'user','id=5', 'comment']
url_str = urlunparse(data)
print(url_str)

# urlsplit() 不再解析params部分，返回长度为5的元组,如果有;params会解析成path的一部分
result = urlsplit('http://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
# urlunsplit()：参数是长度为5的可迭代对象
data = ['http', 'www.baidu.com', 'index.html', 'id=5', 'comment']
url_str = urlunsplit(data)
print(url_str)

# urljoin(base_url, url)  base_url仅提供scheme, netloc和path, 如果新url没有则补充
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://www.google.com/FAQ.html'))
print(urljoin('http://www.baidu.com?wd=abc', '?id=5#comment'))
