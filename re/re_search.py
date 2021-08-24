import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'
#result = re.match(r'Hello.*?(\d+).*?Demo', content) # return None
result = re.search(r'Hello.*?(\d+).*?Demo', content)
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

pattern = r'<li.*?active.*?singer="(.*?)">(.*?)</a>'
result = re.search(pattern, html, re.S)
print(f'singer: {result.group(1)} song: {result.group(2)}')

# without active
pattern = r'<li.*?singer="(.*?)">(.*?)</a>'
result = re.search(pattern, html, re.S)
print(f'singer: {result.group(1)} song: {result.group(2)}')

# without re.S: failed to match \n
pattern = r'<li.*?singer="(.*?)">(.*?)</a>'
result = re.search(pattern, html)
print(f'singer: {result.group(1)} song: {result.group(2)}')


