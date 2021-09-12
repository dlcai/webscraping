from bs4 import BeautifulSoup
from bs4 import element

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dormouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters;and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tille" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html, 'lxml')
print(soup.prettify())
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p) # 获取第一个p节点
# 获取节点名称
print(soup.title.name)
# 获取节点属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
# 获取节点文本内容
print(soup.p.string)
# 嵌套选择，返回的仍是bs4.element.Tag类型
print(type(soup.head.title))

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">
    Once upon a time there were three little sisters;and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
    </a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
    and
    <a href="http://example.com/tille" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.
    </p>
<p class="story">...</p>
"""
# 直接子节点 contents, children
soup = BeautifulSoup(html, 'lxml')
print(soup.p.contents) # 返回直接子节点list
print(soup.p.children) # 返回list_iterator对象
for i, child in enumerate(soup.p.children):
    print(i, repr(child))
# 所有子孙节点 descendants
print(soup.p.descendants) 
for i, child in enumerate(soup.p.descendants):
    print(i, repr(child))
# 父节点 parent
print('第一个a节点的父节点:')
print(soup.a.parent)
# 所有祖先节点 parents
print('a节点的所有祖先节点:')
print(type(soup.a.parents))
#print(list(enumerate(soup.a.parents)))
for i, parent in enumerate(soup.a.parents):
    if isinstance(parent, element.Tag) and not isinstance(parent, BeautifulSoup):
        print(i, parent.name, type(parent))
# 兄弟节点
html = """
<html>
<body>
<p class="story">
    Once upon a time there were three little sisters;and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
    </a>
        Hello
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        and
    <a href="http://example.com/tille" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.
</p>
"""
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling', repr(soup.a.next_sibling))
print('Prev Sibling', repr(soup.a.previous_sibling))
print('Next Siblings')
for i, sibling in enumerate(soup.a.next_siblings):
    if isinstance(sibling, element.Tag):
        print(i, sibling.name, sibling['id'], type(sibling))
    if isinstance(sibling, element.NavigableString):
        print(i, repr(sibling), type(sibling))
# 返回多个节点的生成器，转换成list再提取信息
print(list(soup.a.parents)[0].attrs)
