import json
import urllib
from datetime import time
from http import cookiejar
from urllib import request
from urllib import parse
from selenium import webdriver

import pymysql
from pyquery import PyQuery as pq
import requests
import redis
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

# 数据库连接
from mobile_data.config import *

red = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASS)

# connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USERNAME, port=3306, password=MYSQL_PASSWORD, db=MYSQL_DB,                             charset="utf8", cursorclass=pymysql.cursors.DictCursor)
from taobao.config import SERVICE_ARGS


def phantomJs():
    # browser = webdriver.PhantomJS(service_args=SERVICE_ARGS)
    browser = webdriver.Chrome(service_args=SERVICE_ARGS)
    wait = WebDriverWait(browser, 10)

    browser.set_window_size(1400, 900)
    # browser = webdriver.PhantomJS()
    url = 'https://login.10086.cn/login.html'

    # content = \
    browser.get(url)

    cookie = {}

    # 获取cookie列表
    for i in browser.get_cookies():
        cookie[i["name"]] = i["value"]

    cookie_text = json.dumps(cookie)

    red.set("15172538022_cookie", cookie_text)

    #  切换到验证码登录的选项
    sms_login_tab_btn = wait.until(Ec.element_to_be_clickable((By.ID, 'sms_login_1')))
    sms_login_tab_btn.click()

    #  填充手机号码和发送短信
    sms_name_input = wait.until(Ec.presence_of_element_located((By.ID, "sms_name")))
    sms_name_input.send_keys("15172538022")

    #   发送短信
    getSMSPwd1_btn = wait.until(Ec.element_to_be_clickable((By.ID, 'getSMSPwd1')))
    # getSMSPwd1_btn.click()

    # print(subbmitBtn)

    # print(driver.page_source)


def getRandomCodeAction():
    login_data = {
        'userName': '15172538022',
        'type': "01",
        'channelID': '12003'
    }

    url = "https://login.10086.cn/sendRandomCodeAction.action"

    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        # 'Cookie': 'CmLocation=270|270; collect_id=3uf1pjm2gbkmpqf3eho9o9gkiqar43ys; verifyCode=05bc66af4d1b431287d2c638ac6dbe7bff6169a2; CmProvid=bj; WT_FPC=id=288397308106c73aa131562896765709:lv=1562899459480:ss=1562896765709; sendflag=20190712162510878824; CaptchaCode=GIBpGX; rdmdmd5=02391778E7E8EE96CEEF569D74BA76CE; lgToken=532ee20c3c6a4c21962a0952e2ddc858',
        'Host': 'login.10086.cn',
        'Origin': 'https://login.10086.cn',
        'Referer': 'https://login.10086.cn/login.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'Xa-before': loadToken()
    }

    print(header)

    logingpostdata = parse.urlencode(login_data).encode('utf-8')

    response1 = requests.post(url, data=logingpostdata, headers=header)

    if response1.status_code == 200:
        cookies = response1.cookies
        print(cookies)

    # content = json.loads(response1.content.decode("utf-8"))

    print(response1.content)

    # return content['result']

    # cookie_filename = 'cookie.txt'
    # cookie = cookiejar.MozillaCookieJar(cookie_filename)
    # handler = request.HTTPCookieProcessor(cookie)
    # opener = request.build_opener(handler)
    # req1 = request.Request(url=login_url, data=logingpostdata, headers=head, method="POST")
    #
    # # request.install_opener(opener)
    #
    # response1 = opener.open(req1)
    #
    # print(response1.read().decode("utf-8"))
    #
    # cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中


def checkUidAvailable():
    login_data = {

    }

    login_url = "https://login.10086.cn/checkUidAvailable.action"

    head = {
        'Host': 'login.10086.cn',
        'Connection': 'keep-alive',
        'Content-Length': '0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'https://login.10086.cn',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'Referer': 'https://login.10086.cn/login.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cookie': 'collect_id=3uf1pjm2gbkmpqf3eho9o9gkiqar43ys; verifyCode=05bc66af4d1b431287d2c638ac6dbe7bff6169a2; CmLocation=270|270; CmProvid=bj; WT_FPC=id=288397308106c73aa131562896765709:lv=1562926342022:ss=1562926342022; lgToken=67ac78fe17ca4a98bdeff6381c9bf0f4; sendflag=20190713094327558597; CaptchaCode=EAYGRJ; rdmdmd5=5BCD99A5D2DD554B745C29A91BBDDBAC',
    }

    logingpostdata = parse.urlencode(login_data).encode('utf-8')

    cookie_filename = 'cookie1.txt'
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head, method="POST")

    # request.install_opener(opener)

    response1 = opener.open(req1)

    # get_order_list(opener)

    print(response1.read().decode("utf-8"))

    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中


def login():
    cookiejar = cookielib.CookieJar()
    urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookiejar))
    urllib2.install_opener(urlopener)

    urlopener.addheaders.append(('Referer', 'http://www.chinabidding.com.cn/zbw/login/login.jsp'))
    urlopener.addheaders.append(('Accept-Language', 'zh-CN'))
    urlopener.addheaders.append(('Host', 'www.chinabidding.com.cn'))
    urlopener.addheaders.append(('User-Agent', 'Mozilla/5.0 (compatible; MISE 9.0; Windows NT 6.1); Trident/5.0'))
    urlopener.addheaders.append(('Connection', 'Keep-Alive'))

    login_data = {
        'userName': '15172538022',
        'type': "01",
        'channelID': '12003'
    }

    login_url = "https://login.10086.cn/checkUidAvailable.action"

    authcode = input('Please enter the authcode:')
    # authcode=VerifyingCodeRecognization(r"http://192.168.0.106/images/code.jpg")

    # Send login/password to the site and get the session cookie
    urlcontent = urlopener.open(urllib2.Request(login_url, urllib.urlencode(login_data)))
    page = urlcontent.read(500000)

    # Make sure we are logged in, check the returned page content
    print(page)
    return True


def loadToken():
    session = requests.session()
    url = "https://login.10086.cn/loadToken.action"

    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Length': '20',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'collect_id=3uf1pjm2gbkmpqf3eho9o9gkiqar43ys; verifyCode=05bc66af4d1b431287d2c638ac6dbe7bff6169a2; CmLocation=270|270; CmProvid=bj; WT_FPC=id=288397308106c73aa131562896765709:lv=1562926342022:ss=1562926342022; CaptchaCode=EAYGRJ; lgToken=c0572f68f7764b9fa381f1764e1d5565; sendflag=20190713104303981298',
        'Host': 'login.10086.cn',
        'Origin': 'https://login.10086.cn',
        'Referer': 'https://login.10086.cn/login.html',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    post_data = {
        'userName': '15172538022',
        'type': "01",
        'channelID': '12003'
    }

    logingpostdata = parse.urlencode(post_data).encode('utf-8')

    # response1 = requests.post(url, data=logingpostdata, headers=header)
    #
    # if response1.status_code == 200:
    #     cookies = response1.cookies
    #     print(cookies)
    #
    # res = response1.content.decode("utf-8")
    #
    # content = json.loads(res)
    # # print(session.cookies.get_dict())
    #
    # return content['result']
    # print(response1.json())

    cookie = cookiejar.CookieJar()
    # cookie = cookiejar.MozillaCookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    req1 = request.Request(url=url, data=logingpostdata, headers=header, method="POST")

    response1 = opener.open(req1)

    cookieValue = ''
    for item in cookie:
        cookieValue += item.name + '=' + item.value + ';'
    print(cookieValue)

    # cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

    result = response1.read().decode("utf-8")

    content = json.loads(result)

    return content['result']


def main():
    # getCookie()
    # Xa_before = loadToken()
    # print(Xa_before)
    # login()
    # checkUidAvailable()

    # 获取验证码和cookie
    getRandomCodeAction()
    # phantomJs()
    # exit()
    # login()
    # get_list_order()
    # list_order()
    # spider_order_data()


if __name__ == '__main__':
    main()
