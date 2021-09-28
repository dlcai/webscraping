from pyquery import PyQuery
import requests

html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''

doc = PyQuery(html)
print(type(doc))
print(doc)
print("typeof doc('li') :", type(doc('li')))  # 仍返回PyQuery对象，方便继续嵌套css选择
print('repr(pq) :')
print(repr(doc('li'))) # PyQuery类继承了list
print('str(pq) :')
print(doc('li')) # print输出str(args)相当于print(str(doc('li')))
print('repr(str(pq)) :')
print(repr(str(doc('li'))))
print('PyQuery(list) :')
for el in doc('li'):
    print(el, type(el))  # PyQuery的css选择器内部实现依赖lxml.etree的xpath

#import pyquery
#print(pyquery.__file__)
from pyquery import PyQuery as pq
# URL初始化
doc = pq(url='https://cuiqingcai.com') # 等价于以requests.get得到响应体文本字符串初始化
print(doc('title'))
doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))
# 文件初始化
doc = pq(filename='demo.html')
print(doc('li'))
