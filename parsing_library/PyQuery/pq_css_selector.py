#coding=utf-8
from pyquery import PyQuery as pq

html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''

doc = pq(html)
lis = doc('#container .list li')
print(lis)
print(type(lis))
# css查询方法find() 查找范围：所有子孙节点，与jQuery函数用法相同
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
# children()方法 查找范围：直接子节点
print('items.children() 输出直接子节点:')
print(items.children())
print("items.children('.active') 筛选符合条件的直接子节点:")
print(items.children('.active'))

# parent() 父节点
print('items.parent() 父节点')
print(repr(items.parent()))
print('items.parents() 祖先节点')
print(repr(items.parents()))
print("items.parents('.wrap') 祖先节点")
print(repr(items.parents('.wrap')))

# siblings() 兄弟节点
print('siblings() 兄弟节点:')
li = doc('.list .item-0.active')
print(li.siblings())
print("siblings('.active') ")
print(li.siblings('.active'))

# 遍历多个节点 调用items方法
lis = doc('li').items()
print('typeof PyQuery.items():')
print(type(lis))
for li in lis:
    print(li, type(li))

# 获取第一个节点的属性 attr()方法
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))

a4 = doc('a')
print(a4, type(a4))
print(a4.attr.href)

for item in a4.items():
    print(item.attr.href)

# text() 返回节点内部的纯文本内容  html() 返回节点内的所有html文本
print('a.text():')
print(a.text())
li = doc('.item-0.active')
print(li)
print(li.html())
# 多个节点时, text()返回的是所有节点内部纯文本，中间用空格隔开的一个字符串
# html()返回的是第一个节点内部的html文本
html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
doc = pq(html)
lis = doc('li')
print('多节点text() html():')
print(lis.html())
print(type(lis.html()))
print(lis.text())
print(type(lis.text()))

