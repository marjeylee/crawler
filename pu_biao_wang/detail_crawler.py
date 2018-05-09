"""
爬取每个详情页面的信息
"""
import json
import uuid

import requests
from bs4 import BeautifulSoup


def remove_enter_char(line):
    return line.replace('\n', '')


def get_detail_urls():
    """
    获得详情页面的detail_pages
    :return:
    """
    with open('./detail_urls.txt', mode='r', encoding='utf8')as file:
        lines = file.readlines()
        lines = map(remove_enter_char, lines)  # 这个牛逼闪闪的功能该不会是懒加载吧。
        return lines


def get_detail_page_content(text):
    """
    解析html内容
    :param text:
    :return:
    """
    try:
        soup = BeautifulSoup(text)
        pre = soup.find('pre')
        centers = pre.find_all('center')
        name = centers[0].text
        spell = centers[1].text
        content = pre.find(id='content_text').text
        return {'name': name, 'spell': spell, 'content': content}
    except Exception as e:
        print(e)
        return None


def __parse_content(content):
    """
    content字符串
    :param content:
    :return:
    """
    pass


def get_detail_content(detail_url):
    """
    获得页面详情内容
    :param detail_url:
    :return:
    """
    response = requests.get(detail_url)
    if response.status_code == 200:
        text = response.text
        return get_detail_page_content(text)
    return None


if __name__ == '__main__':
    d_urls = get_detail_urls()
    for u in d_urls:
        try:
            content = get_detail_content(u)
            if content is not None:
                json_str = json.dumps(content)
                random_name = './detail_content/' + str(uuid.uuid4())
                with open(random_name, mode='w', encoding='utf8') as file:
                    file.write(json_str)
        except Exception as e:
            print(e)
