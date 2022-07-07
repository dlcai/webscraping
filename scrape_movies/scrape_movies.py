import requests
import logging
import re
from urllib.parse import urljoin
import os
import json
from html import unescape
import timeit
import multiprocessing

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s -%(message)s')
BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PAGE = 10
RESULTS_DIR = 'results'
os.path.exists(RESULTS_DIR) or os.makedirs(RESULTS_DIR)
count = 0

# 爬取一个页面源码的通用函数
def scrape_page(url): 
    logging.info('scraping %s...', url)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        logging.error('get invalid status code %s ' +\
                'while scraping %s', r.status_code, url)
    except requests.RequestException:
        logging.error('error occurred while scraping %s', url,
                      exc_info=True)
        # 将异常信息添加到日志消息中, 如果没有异常则添加None
# 爬取电影排行榜一个列表页的源码
def scrape_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)
# 解析列表页, 得到每部电影详情页url
def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name">', re.S)
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url

# 爬取详情页源码
def scrape_detail(url):
    return scrape_page(url)

def parse_detail(html):
    cover_pattern = re.compile('class="item.*?<img.*?src="(.*?)".*?' +\
                               'class="cover">', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?' +\
                            '<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映', re.S)
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>' +\
                               '(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    
    cover = re.search(cover_pattern, html).group(1).strip() \
            if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() \
            if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) \
            if re.findall(categories_pattern, html) else []
    published_at = re.search(published_at_pattern, html).group(1) \
            if re.search(published_at_pattern, html) else None 
    drama = re.search(drama_pattern, html).group(1).strip() \
            if re.search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1)) \
            if re.search(score_pattern, html) else None
    
    return {
        'cover': cover,
        'name': unescape(name),
        'categories': categories,
        'published_at': published_at,
        'drama': drama,
        'score': score
    }
     
def save_data(data):
    name = data.get('name')
    global count
    count += 1
    count_str = '0' + str(count) if count < 10  else str(count)
    data_path = f'{RESULTS_DIR}/{count_str}-{name}.json'
    # json.dump()把python数据结构保存为json文件
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=True) 

#def main():
#    for page in range(1, TOTAL_PAGE+1):
#        index_html = scrape_index(page)
#        detail_urls_g = parse_index(index_html)
#        #logging.info('detail urls: %s', list(detail_urls_g))
#        for detail_url in detail_urls_g:
#            detail_html = scrape_detail(detail_url)
#            data = parse_detail(detail_html)
#            logging.info('get detail data %s', data) 
#            logging.info('saving data to json file...')
#            save_data(data)
#            logging.info('data saved successfully.')
# 修改main函数为只爬取一个列表页，以便利用python多进程
# 一个进程爬取一个列表页的数据
def main(page):
    index_html = scrape_index(page)
    detail_urls_g = parse_index(index_html)
    #logging.info('detail urls: %s', list(detail_urls_g))
    for detail_url in detail_urls_g:
        detail_html = scrape_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('get detail data %s', data) 
        logging.info('saving data to json file...')
        save_data(data)
        logging.info('data saved successfully.')
    


if __name__ == '__main__':
    start_t = timeit.default_timer()

    pool = multiprocessing.Pool() # 无参数时默认使用所有cpu核 
    #pool = multiprocessing.Pool(processes=4) 
    page_indexes = range(1, TOTAL_PAGE+1)
    pool.map(main, page_indexes)
    pool.close()
    pool.join()
    
    end_t = timeit.default_timer()
    print(f'爬虫程序运行时间：{end_t - start_t}秒.')
    print(f'本机cpu核数：{multiprocessing.cpu_count()}')
