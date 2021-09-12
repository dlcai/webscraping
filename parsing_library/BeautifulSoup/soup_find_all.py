from bs4 import BeautifulSoup
import re

html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
# find_all(name, attrs, recursive, text, **kwargs)
soup = BeautifulSoup(html, 'lxml')
# 根据节点名name来查询
tag_list = soup.find_all(name='ul') # 返回bs4.element.Tag列表
print(tag_list)
print(type(tag_list[0]))
# Tag对象也可以进行find_all查询
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)
# 根据属性查询attrs={}
print('soup.find_all(attrs={})')
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
# 常用属性id、class等也可以直接传参查询
print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))
# text参数：用来匹配节点的文本，传入str或Pattern,返回节点文本列表
html2 = '''
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
</div>
</div>
'''
soup2 = BeautifulSoup(html2, 'lxml')
for ns in soup2.find_all(text=re.compile(r'link')):
    print(repr(ns), type(ns))
# find(name, attrs, recursive, text, **kwargs) 返回第一个匹配的元素
tag = soup.find(name='ul')
print(tag, type(tag))
print(soup.find(class_='list'))
# 还有 find_parents() find_next_siblings() find_all_next() 等
