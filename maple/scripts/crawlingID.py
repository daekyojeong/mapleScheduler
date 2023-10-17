import requests
import urllib.request
from bs4 import BeautifulSoup


def userIDCrawling(ID):
    url = f'https://maplestory.nexon.com/N23Ranking/World/Total?c={ID}&w=0'
    soup = crawling(url)
    soup = soup.select_one('#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr.search_com_chk')
    lvl = int(soup.select_one('tr.search_com_chk > td:nth-child(3)').text[3:])
    job = soup.select_one('tr.search_com_chk > td.left > dl > dd').text.split('/')[-1].strip()
    img_src = soup.select_one('tr.search_com_chk > td.left > span > img:nth-child(1)')['src']
    urllib.request.urlretrieve(img_src, 'test.jpg')
    return {'lvl': lvl, 'img_src': img_src, 'job': job}

def crawling(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup
    else:
        print('not found ID')
        return -1