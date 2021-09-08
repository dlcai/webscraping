from lxml import etree

text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''

html = etree.HTML(text) # <class 'lxml.etree._Element'> XPath解析对象,自动补全缺失的tag
print(type(html))
result = etree.tostring(html) # bytes
print(type(result))
print('自动补全缺失的tag:')
print(result.decode('utf-8'))
# 写入文件
result_text = result.decode('utf-8')
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(result_text)

# etree读取文本文件解析
html = etree.parse('test.html', etree.HTMLParser()) # Element对象
print(html.docinfo.public_id)
print(html.docinfo.system_url)
html.docinfo.public_id = None;
html.docinfo.system_url = None;
print('modified docinfo of Element object:')

result = etree.tostring(html, method='html', pretty_print=True)
print(result.decode('utf-8'))

# 用//开头的XPath规则选取所有满足要求的节点
result = html.xpath('//*') # return a list of Element objects
print(result)
result = html.xpath('//li')
print(result)
# /开头获取直接子节点
result = html.xpath('//li/a')
print(result)
result = html.xpath('//ul/a')
print(result)

# 选取父节点 ..或parent::*
result = html.xpath('//a[@href="link4.html"]/../@class') #href属性link4.html的a节点的父节点
print(result)
result = html.xpath('//*/parent::*') # 所有节点的父节点(多个)
print(result)
result = html.xpath('//a/../@class') # 所有a节点的父节点的class属性
print(result)
# 文本获取 text()
result = html.xpath('//li[@class="item-inactive"]/text()')
print(result)
result = html.xpath('//li[@class="item-inactive"]//text()')
print(result)
# 1个属性有多个值匹配 li[contains(@class, "li")] contains条件语句
li = etree.HTML('<li class="li li-first"><a href="link.html">first item</a></li>')
result = li.xpath('//li[@class="li"]/a/text()') 
print(result)
result = li.xpath('//li[contains(@class, "li")]/a/text()')
print(result)
# 多个属性共同确定一个节点 and、or、mod等XPath运算符
text = '''
<li class="li li-first" name="item"><a href="link.html">mult-attr item</a></li>
'''
li = etree.HTML(text)
result = li.xpath('//li[contains(@class, "li") and @name="item"]/a/text()') 
print(result)
# 不包含某些属性的节点
result = li.xpath('//li[not(@class or @id)]/a/text()')
print(result)
result = li.xpath('//li[not(@id)]/a/text()')
print(result)
# 按序选择 [i] last() position() < 3
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)
# 节点轴选择
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
print('节点轴选择:')
result = html.xpath('//li[1]/ancestor::*') # 所有祖先节点
print(result)
result = html.xpath('//li[1]/ancestor::div') # 名为div的祖先节点
print(result)
result = html.xpath('//li[1]/attribute::*') # 获取所有属性值
print(result)
result = html.xpath('//li[1]/child::a') # 直接子节点
print(result)
result = html.xpath('//li[1]/descendant::span') # 子孙节点
print(result)
result = html.xpath('//li[1]/following::*[2]/text()') # 当前节点之后的所有节点
print(result)
result = html.xpath('//li[1]/following-sibling::*/a/text()') #当前节点之后所有同级节点
print(result)
