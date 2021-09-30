import requests
from pyquery import PyQuery as pq


# 保存知乎“发现”页面的“热门收藏夹”部分，把收藏夹名称、创建者、展示的收藏夹回答保存到文本
url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +\
                'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
}

html = ''
try:
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        html = r.text
    else:
        print(f'{r.status_code} {r.reason}')
        exit(1)
except requests.RequestException as e:
    print(repr(e))
    exit(1)

doc = pq(html)
cards = doc('div#collection .ExploreCollectionCard').items()
#print(repr(cards))

with open('zhihu_explore_hot_collections.txt', 'w', encoding='utf-8') as f:
    for card in cards:
        f.write(card('a.ExploreCollectionCard-title').text() + '\n')
        f.write('创建者: ' + card('a.ExploreCollectionCard-creatorName').text() + '\n')
        answers = card('.ExploreCollectionCard-contentItem').items()
        for ans in answers:
            f.write('问题: ' + ans('a.ExploreCollectionCard-contentTitle').text() + '\n')
            excerpt = ans('.ExploreCollectionCard-contentExcerpt').text()
            #print(excerpt)
            author = excerpt.split('：')[0]
            content = excerpt[len(author)+1:]
            f.write('答主: ' + author + '\n')
            f.write('回答: ' + content + '\n')
        f.write('\n')
