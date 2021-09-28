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
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

# 添加/修改属性 attr()
print('Add/Modify attr() :')
li.attr('name', 'link')
print(li)
li.text('changed item')
print(li)
li.html('<span>changed item</span>')
print(li)

# remove()
html2 = '''
<div class="wrap">
    Hello, World
<p>This is a paragraph.</p>
</div>
'''

doc = pq(html2)
wrap = doc('.wrap')
print(wrap.text())

p = wrap.find('p')
print(type(p))
print(p)

p.remove()
print(wrap.text())

# 伪类选择器
doc = pq(html)
li = doc('li:first-child')
print('li:first-child')
print(li)
li = doc('li:last-child')
print('li:last-child')
print(li)
li = doc('li:nth-child(2)')
print('li:nth-child(2)')
print(li)
li = doc('li:gt(2)') # jQuery的:gt(index)选择器，选择index大于指定值的元素(index从0开始）
print('li:gt(2)')  # index为3，4...的元素，即第4个元素及后面的元素 
print(li)
li = doc('li:nth-child(2n)') # 公式:2的倍数
print('li:nth-child(2n)')
print(li)
li = doc('li:nth-child(even)') # 偶数
print('li:nth-child(even)')
print(li)
li = doc('li:contains(second)') # jQuery contains()选择器 选取包含特定字符串的元素
print('li:contains(second)')
print(li)
