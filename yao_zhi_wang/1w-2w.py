"""
获取所有页面
"""
import requests

from spider.get_one_page import spider

if __name__ == '__main__':
    for i in range(10017996, 10020000):
        url = 'https://db.yaozh.com/fangji/' + str(i) + '.html'
        print('开始爬取：' + url)
        try:
            spider(url)
        except Exception as e:
            print(e)
