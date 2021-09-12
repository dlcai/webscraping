from bs4 import BeautifulSoup

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
soup = BeautifulSoup(html, 'lxml')
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(type(soup.select('ul')[0]))
# bs4.element.Tag对象嵌套选择
for ul in soup.select('ul'):
    print(ul.select('li'))
# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])
# 获取文本 Tag.string或get_text()
for li in soup.select('li'):
    print('string:', li.string)
    print('get_text():', li.get_text())
