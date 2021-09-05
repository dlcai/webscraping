import re
import json
import requests
import time

#提取猫眼top100电影的排名、图片链接、标题、演员、上映时间、评分

pattern = re.compile(r'<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)"' +\
r'.*?name.*?<a.*?>(.*?)</a>.*?star.*?>(.*?)</p>' +\
r'.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>', re.S)

# return a movie item at a time in one page
def parse_one_page(html):     
    items = pattern.findall(html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:] if len(item[3]) > 3 else '',
            'time': item[4].strip()[5:] if len(item[4]) > 5 else '',
            'score': item[5] + item[6]
        }

def write_to_file(item): # write a movie item to txt
    with open('maoyan_top100.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False, indent=4) + '\n') 
        # json.dumps: dict to str

def get_one_page(url): # return html of a page
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +\
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36', 
            'Cookie': '__mta=42866330.1629845905562.1630850195552.1630850200664.35; uuid_n_v=v1; uuid=C9722BE0052E11EC80E9936EB26072D37D3F5CE726D14F8993B1BA4C0A09802D; _csrf=6c7e2a64c65a30407edb555e22190e2f51b958fb0722887610b644c38e953c18; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1629845905; _lxsdk_cuid=17b7a62e03fc8-082664b8c8342f-35667c03-1fa400-17b7a62e03fc8; _lxsdk=C9722BE0052E11EC80E9936EB26072D37D3F5CE726D14F8993B1BA4C0A09802D; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1630850201; _lxsdk_s=17bb62c2f9b-378-7fa-efc||15'
    }
    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.text
        else:
            print(f'{r.status_code} {r.reason}')
            return None 
    except requests.RequestException as e:
        print(repr(e))
        return None

def main(offset):
    url = 'https://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    #print(html)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
        
if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)  #每写入10部电影停2秒
