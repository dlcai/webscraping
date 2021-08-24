import re

content = '12alphabet-34microsoft-56apple'
result = re.sub(r'\d+', '', content)
print(result)

html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

pattern = r'<li.*?>\s*(<a*?>)?(\w+)(</a>)?\s*</li>'
results = re.findall(pattern, html, re.S)
for result in results:
    print(result[1])

# use re.sub
html = re.sub(r'<a.*?>|</a>', '', html)
print(html)
# 返回匹配目标()的元组列表，如果只有1个(),返回()匹配的串
results = re.findall(r'<li.*?>(.*?)</li>', html, re.S)
for s in results:
    print(s.strip())



