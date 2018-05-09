"""
获得所有药房详情页面
"""

import requests
from bs4 import BeautifulSoup

base_url = 'http://db.ouryao.com/yd2015/index.php?k=&cid=1&cid2=3&page='


def get_catalog_page_list():
    """
    获得所有目录页面的url
    :return:
    """
    catalog_list = []
    for i in range(1, 75):
        url = base_url + str(i)
        catalog_list.append(url)
    return catalog_list


def get_detail_urls_from_text(text):
    soup = BeautifulSoup(text)
    table = soup.find('table')
    trs = table.find_all('tr')
    urls = []
    for tr in trs:
        a = tr.find('a')
        if a is not None:
            href = a.get('href')
            if href is not None:
                complete_url = 'http://db.ouryao.com/yd2015/' + href
                urls.append(complete_url)
    return urls


def get_detail_page_url_from_one_catalog_url(catalog_url):
    """
    获得一个目录页面的所有详情页面
    :param catalog_url:
    :return:
    """
    response = requests.get(catalog_url)
    if response.status_code == 200:
        text = response.text
        detail_urls = get_detail_urls_from_text(text)
        if len(detail_urls) > 0:
            return detail_urls
    return None


def save_detail_page_url(detail_urls):
    """
    保存图片
    :param detail_urls:
    :return:
    """
    with open('./detail_urls.txt', mode='w', encoding='utf8')as file:
        for u in detail_urls:
            file.write(u + '\n')


if __name__ == '__main__':
    catalog_page_list = get_catalog_page_list()
    detail_page_urls = []
    for catalog_page in catalog_page_list:
        d_urls = get_detail_page_url_from_one_catalog_url(catalog_page)
        if d_urls is not  None:
            detail_page_urls.extend(d_urls)
    save_detail_page_url(detail_page_urls)
