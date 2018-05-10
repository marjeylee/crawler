"""
获取一个页面的数据
"""
import requests
from bs4 import BeautifulSoup
import pymysql


def get_cookies(orig_cookies):
    """
    获取格式化后的cookies
    :param orig_cookies: 页面原始cookies字符串
    :return:
    """
    cookies = {}  # 初始化cookies字典变量
    for line in orig_cookies.split(';'):
        name, value = line.strip().split('=', 1)
        cookies[name] = value
    return cookies


def get_text(url, cookies):
    """
    获取页面内容
    :param url: 页面内容
    :param cookies: cookies
    :return:
    """
    res = requests.get(url, cookies=cookies)
    if res.status_code == 200:
        print("请求页面成功！")
        return res.text
    print('请求页面失败！')
    return None


def parse_content(text):
    """
    解析内容
    :param text:html页面内容
    :return:
    """
    soup = BeautifulSoup(text)
    table = soup.find(class_='table')
    trs = table.find_all('tr')
    if trs is not None and len(trs) > 0:
        page_content = {}
        print('解析页面成功')
        for tr in trs:
            key = tr.find('th').text.strip('\n').strip(' ')
            value = tr.find('td').text.strip('\n').strip(' ')
            page_content[key] = value
        return page_content
    print('解析页面失败！！！！！！！！！！！！！！！')
    return None


def save_po(po):
    """
    保存到数据库
    :param po:
    :return:
    """
    # 打开数据库连接
    db = pymysql.connect("192.168.46.128", "root", "MyNewPass4!", "traditional chinese medicine", charset='utf8')

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # SQL 插入语句
    sql = "INSERT INTO t_prescription(name, alias, classical, source, big_class, small_class,prescription, processing, usages,curative_effect,calcitization, taboo, cut, attached, note,literature, application,url) \
           VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
          (po['name'], po['alias'], po['classical'], po['source'], po['big_class'], po['small_class'],
           po['prescription'], po['processing'],
           po['usages'], po['curative_effect'], po['calcitization'], po['taboo'], po['cut'], po['attached'], po['note'],
           po['literature'],
           po['application'], po['url'])
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print('数据插入成功')
    except:
        print('数据插入失败')
        # 发生错误时回滚
        db.rollback()
    # 关闭数据库连接
    db.close()


def save_to_db(content, url):
    """
    将数据保存到数据库
    :param content: 内容
    :return:
    """
    po = {'name': '', 'alias': '', 'classical': '', 'source': '', 'big_class': '', 'small_class': '',
          'prescription': '', 'processing': '', 'usages': '',
          'curative_effect': '', 'calcitization': '', 'taboo': '', 'cut': '', 'attached': '', 'note': '',
          'literature': '', 'application': '', 'url': url}
    keys = content.keys()
    for key in keys:
        if key == '方名':
            print(content[key])
            po['alias'] = content[key]
            continue
        if key == '规范名':
            po['name'] = content[key]
            continue
        if key == '经典':
            po['classical'] = content[key]
            continue
        if key == '出处':
            po['source'] = content[key]
            continue
        if key == '功用大类':
            po['big_class'] = content[key]
            continue
        if key == '功用小类':
            po['small_class'] = content[key]
            continue
        if key == '处方':
            po['prescription'] = content[key]
            continue
        if key == '炮制':
            po['processing'] = content[key]
            continue
        if key == '功用':
            po['usages'] = content[key]
            continue
        if key == '主治':
            po['curative_effect'] = content[key]
            continue
        if key == '方解':
            po['calcitization'] = content[key]
            continue
        if key == '禁忌':
            po['taboo'] = content[key]
            continue
        if key == '化裁':
            po['cut'] = content[key]
            continue
        if key == '附方':
            po['attached'] = content[key]
            continue
        if key == '附注':
            po['note'] = content[key]
            continue
        if key == '文献':
            po['literature'] = content[key]
            continue
        if key == '运用':
            po['application'] = content[key]
            continue
        if key == 'url':
            po['url'] = content[key]
            continue
    save_po(po)


def spider(url):
    orig_cookies = "think_language=zh-CN; _ga=GA1.2.830504101.1524124260; _gat=1; " \
                   "MEIQIA_EXTRA_TRACK_ID=13RqSPm12f7KHh5DfpAFU6TMhSw; _gid=GA1.2.1951402781.1524124295; yaozh_userId=558625; " \
                   "yaozh_uidhas=1; yaozh_mylogin=1524124374; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; " \
                   "MEIQIA_EXTRA_TRACK_ID=13RqSPm12f7KHh5DfpAFU6TMhSw; _ga=GA1.3.830504101.1524124260; bigdata_use_tips=1; " \
                   "UtzD_f52b_saltkey=PSGT3ShA; UtzD_f52b_lastvisit=1524126106; PHPSESSID=nvolivjtqa0l8q1bsb0kpgjdo5; " \
                   "UtzD_f52b_ulastactivity=1524124368%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D525652; " \
                   "UtzD_f52b_creditbase=0D0D0D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; " \
                   "Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1524129361,1524129722,1524131643,1524184952; " \
                   "yaozh_logintime=1524184965; yaozh_user=558625%09marjey_lee; db_w_auth=525652%09marjey_lee; " \
                   "UtzD_f52b_lastact=1524184966%09uc.php%09; " \
                   "UtzD_f52b_auth=7d1e904voqI9fjYRKNtdFE4RmProWhGXeS2%2B3H4M3NgOupT0iKriPlwluMJeANFr9Pbn5kqbvgyRehcefYmAy" \
                   "%2BdajaA; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1524185011 "
    cookies = get_cookies(orig_cookies)
    text = get_text(url, cookies)
    if text is not None:
        content = parse_content(text)
        if content is not None:
            save_to_db(content, url)

# if __name__ == '__main__':
#     url = "https://db.yaozh.com/fangji/10000066.html"
#     orig_cookies = "think_language=zh-CN; _ga=GA1.2.830504101.1524124260; _gat=1; " \
#                    "MEIQIA_EXTRA_TRACK_ID=13RqSPm12f7KHh5DfpAFU6TMhSw; _gid=GA1.2.1951402781.1524124295; yaozh_userId=558625; " \
#                    "yaozh_uidhas=1; yaozh_mylogin=1524124374; WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; " \
#                    "MEIQIA_EXTRA_TRACK_ID=13RqSPm12f7KHh5DfpAFU6TMhSw; _ga=GA1.3.830504101.1524124260; bigdata_use_tips=1; " \
#                    "UtzD_f52b_saltkey=PSGT3ShA; UtzD_f52b_lastvisit=1524126106; PHPSESSID=nvolivjtqa0l8q1bsb0kpgjdo5; " \
#                    "UtzD_f52b_ulastactivity=1524124368%7C0; UtzD_f52b_creditnotice=0D0D2D0D0D0D0D0D0D525652; " \
#                    "UtzD_f52b_creditbase=0D0D0D0D0D0D0D0D0; UtzD_f52b_creditrule=%E6%AF%8F%E5%A4%A9%E7%99%BB%E5%BD%95; " \
#                    "Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1524129361,1524129722,1524131643,1524184952; " \
#                    "yaozh_logintime=1524184965; yaozh_user=558625%09marjey_lee; db_w_auth=525652%09marjey_lee; " \
#                    "UtzD_f52b_lastact=1524184966%09uc.php%09; " \
#                    "UtzD_f52b_auth=7d1e904voqI9fjYRKNtdFE4RmProWhGXeS2%2B3H4M3NgOupT0iKriPlwluMJeANFr9Pbn5kqbvgyRehcefYmAy" \
#                    "%2BdajaA; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1524185011 "
#     cookies = get_cookies(orig_cookies)
#     text = get_text(url, cookies)
#     if text is not None:
#         content = parse_content(text)
#         if content is not None:
#             save_to_db(content)
