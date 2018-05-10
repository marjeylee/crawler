"""
获取一页数据
"""
from selenium import webdriver


def get_cookie(cookie_str):
    """
    获取cookies
    :param cookie_str:
    :return:
    """
    cookie = {}
    return_cookie = []
    cs = cookie_str.split(';')
    for c in cs:
        kv = c.split('=')
        cookie[kv[0].strip(' ')] = kv[1].strip(' ')
    keys = cookie.keys()
    for k in keys:
        tmp_c = {'name': k, 'value': cookie[k]}
        return_cookie.append(tmp_c)
    return return_cookie


def get_orig_data(url):
    """
    获得最原始的数据
    :param url: 待爬取页面
    :return:
    """

    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    chrome_options.add_argument(
        'user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 '
        'Safari/537.36"')
    cookie_str = 'think_language=zh-CN; _ga=GA1.2.830504101.1524124260; _gat=1; ' \
                 'MEIQIA_EXTRA_TRACK_ID=13RqSPm12f7KHh5DfpAFU6TMhSw; _gid=GA1.2.1951402781.1524124295; ' \
                 'yaozh_userId=558625; yaozh_uidhas=1; yaozh_mylogin=1524124374; ' \
                 'WAF_SESSION_ID=7d88ae0fc48bffa022729657cf09807d; MEIQIA_EXTRA_TRACK_ID=13RqSPm12f7KHh5DfpAFU6TMhSw; ' \
                 '_ga=GA1.3.830504101.1524124260; bigdata_use_tips=1; UtzD_f52b_saltkey=PSGT3ShA; ' \
                 'UtzD_f52b_lastvisit=1524126106; PHPSESSID=vfk7u66fuasiia08ovrsd77bu1; ' \
                 'Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1524124259,1524129082,1524129361,1524129722; ' \
                 'yaozh_logintime=1524129735; yaozh_user=558625%09marjey_lee; db_w_auth=525652%09marjey_lee; ' \
                 'UtzD_f52b_lastact=1524129736%09uc.php%09; ' \
                 'UtzD_f52b_auth=1477XgQXVtUODyfOK%2F%2B2aFXkfL4FlCfZZAXO4bJj4z5nxwMMxXZkXU6f' \
                 '%2FEqjmSqtkOT6CW3knSrScdrqzTUr666ldqs; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1524129739 '
    browser = webdriver.Chrome('D:\\software\\chromedriver.exe', chrome_options=chrome_options)

    cookie = get_cookie(cookie_str)
    browser.get(url)
    cookoes = browser.get_cookies()
    for c in cookie:
        browser.add_cookie({'name': 'password', 'value': 'youpassword'})
        
    print(browser.page_source)
    browser.close()


if __name__ == '__main__':
    url = 'https://db.yaozh.com/fangji/10000066.html'
    ori_data = get_orig_data(url)
