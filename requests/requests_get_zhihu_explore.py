import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('ExploreRoundtableCard-questionTitle.*?>(.*?)</a>', re.S) # .match \n
titles = re.findall(pattern, r.text)  # 以字符串列表的形式返回所有非重叠匹配
print(type(titles))
print(titles)
