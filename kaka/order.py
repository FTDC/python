from datetime import time
from http import cookiejar
from urllib import request
from urllib import parse
from selenium import webdriver

import pymysql
from pyquery import PyQuery as pq
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

# 数据库连接
from kaka.config import *

connection = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USERNAME, port=3306, password=MYSQL_PASSWORD, db=MYSQL_DB,
                             charset="utf8", cursorclass=pymysql.cursors.DictCursor)


def get_order_list(opener):
    header = {
        'Host': 'www.lipin.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': 'PHPSESSID=2df1295e622a96021bbf545a56e1a612; Hm_lvt_2ed7713098d978316125e0be7dbcffc5=1540864044,1541559174,1542164575; Hm_lpvt_2ed7713098d978316125e0be7dbcffc5=1542164575; wq_loginuser=asi1225; wq_apiauth=c413C0xPNtXi3fy1j9epkDN1AL_5zg-k_w4e76oEBnj16wDur-Tb9dWkHKgdNn4dW0Zy',
        'Host': 'www.lipin.com',
        'Referer': 'https://www.lipin.com/account.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }

    httpReq = request.Request(url="https://www.lipin.com/account/act_selldetail", data=None, headers=header)

    html = opener.open(httpReq)
    result = html.read().decode("utf-8")
    # html = req.data
    # res = html.read()
    print(html)
    print(result)

    # print(res.decode(encoding="utf-8"))
    # print(res.decode(encoding='utf-8'))


def login():
    login_data = {
        'username': 'asi1225',
        'password': 'ajin9126',
        'type': 0,
        'refer': '',
        'formhash': '336b9d87'
    }

    login_url = "https://www.lipin.com/signin.html?url=%2Faccount.html&ajax=1"

    head = {
        'User-Agnet': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        'Connection': 'keep-alive'
    }

    logingpostdata = parse.urlencode(login_data).encode('utf-8')

    cookie_filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    req1 = request.Request(url=login_url, data=logingpostdata, headers=head)

    # request.install_opener(opener)

    response1 = opener.open(req1)

    # for item in cookie:
    #     print('Name = %s' % item.name)
    #     print('Value = %s' % item.value)

    # print(response1)
    # exit()

    # get_order_list(opener)

    print(response1.read().decode("utf-8"))

    cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

    print(cookie)


def get_cookie():
    cookie_filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)

    cookie_str = ''
    for item in cookie:
        cookie_str += item.name + "=" + item.value + ";"

    return cookie_str


def get_list_order():
    cookie_filename = 'cookie.txt'
    cookie = cookiejar.MozillaCookieJar(cookie_filename)
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)

    # cookie_str = ''
    # for item in cookie:
    #     cookie_str += item.name + "=" + item.value + ";"
    # print('Name = %s' % item.name)
    # print('Value = %s' % item.value)
    # print(cookie)

    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)

    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': get_cookie(),
        'Host': 'www.lipin.com',
        'Referer': 'https://www.lipin.com/account.html',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }

    httpReq = request.Request(url="https://www.lipin.com/account/act_selldetail", data=None, headers=header)

    # opener.add_handler(header)

    resp = opener.open(httpReq)

    # with open('renren_login.html', 'wb')as f:
    #     f.write(resp.read().decode('utf-8'))

    print(resp.read().decode("utf-8"))


def list_order():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
        'Cookie': 'PHPSESSID=347b653417b9e0675a53c2461107204e; Hm_lvt_2ed7713098d978316125e0be7dbcffc5=1540864044,1541559174,1542164575,1542420092; Hm_lpvt_2ed7713098d978316125e0be7dbcffc5=1542420092; wq_loginuser=asi1225; wq_apiauth=f022xqK7fGdNr4weP3-ysGCb0P5km73U2MrVdMkeZ4LPeICWDZEkM-Bb3SfkzOvwbD6-'
    }
    r = requests.get("https://www.lipin.com/account/act_selldetail", headers=headers)
    text = r.text
    pyquery = pq(text)

    orders = pyquery.find(".sell-records tbody tr")

    its = orders.items()

    for it in its:
        order_id = it.find(".orderid").text()
        # print(it.find(".orderid").text())
        order_detail(order_id)

        # try:
        #
        #     with connection.cursor() as cursor:
        #         # 写入数据
        #         # for wordLink in soup.find_all("a", href=re.compile("^\/wiki")):
        #         #     if not re.search("\.jpg|JPG|js", wordLink["href"]):
        #         #         print(wordLink.string, "----", wordLink.get("href"))
        #         #
        #         #         # 写入新的记录
        #         #         sql = "insert into word (`word`, `linkurl`) VALUES (%s, %s)"
        #         #         res = cursor.execute(sql, (wordLink.get_text(), wordLink.get("href")))
        #         #
        #         #         connection.commit()
        #
        #         # 查询数据
        #         sql2 = "select id, word, linkurl from  word where id > %s"
        #         count = cursor.execute(sql2, (20,))
        #         print(count)
        #         result = cursor.fetchone();
        #         print(result)
        #
        #         result2 = cursor.fetchmany(20);
        #         print(result2)
        #
        #         result3 = cursor.fetchall();
        #         print(result3)
        #
        #         # connection.commit()
        #
        # finally:
        #     connection.close()
        # print(it.attr.href)

    # print(orders.items(".orderid"))
    # print(text)


def order_detail(order_id):
    order_id = '1811170536030950'
    cs = get_cookie()
    print(cs)
    headers = {
        'Host': 'www.lipin.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Cookie': cs,
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    }
    r = requests.get("https://www.lipin.com/account/act_selldetailinfo/order_" + order_id, headers=headers)
    text = r.text

    # print("https://www.lipin.com/account/act_selldetailinfo/order_" + order_id)
    print(text)
    # exit()
    pyquery = pq(text)

    content = pyquery("body > div.content > div > div > div > div > div.prompt-cont > h4")
    if (content.text() == ''):
        # print(content.text())
        # exit()

        orders = pyquery.find(".selldetail-records tbody tr")

        cards = orders.items()
        order_status = pyquery(
            "body > div.view-framework > div.view-framework-body > div.view-framework-main > div > div.box.sellrecords-steps > ul > li:nth-child(4) > h5 > span").text()
        order_deal_time = pyquery(
            "body > div.view-framework > div.view-framework-body > div.view-framework-main > div > div.box.sellrecords-steps > ul > li:nth-child(4) > p").text()

        for card in cards:
            card_id = card.find(".card").text()
            card_passwd = card.find(".code").text()
            card_status = card.find(".state").text()
            deal_time = card.find(".time").text()

            print(card_id, card_passwd, card_status, deal_time, order_status, order_deal_time)

        try:
            with connection.cursor() as cursor:
                sql = "update recycle_card set"
        finally:
            cursor.close()

        # connection.query("select *  from order")

    exit()


def spider_order_data():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT recycle_order_id, channel_no FROM `recycle_order` WHERE pay_status = 0;"
            cursor.execute(sql)
            order_result = cursor.fetchall()
            for order in order_result:
                channel_no = order["channel_no"]
                order_detail(channel_no)
                # sql2 = "SELECT recycle_card_id, card_info, check_result FROM `recycle_card` WHERE `recycle_order_id` = '" + order['recycle_order_id'] + "' ORDER BY `add_time` DESC LIMIT 0, 10"
                # cursor.execute(sql2)
                # card_result = cursor.fetchall()
                # print(channel_no)
                # print(card_result)

            # print(cursor.fetchall())
    finally:
        connection.close()


def phantomJs():
    browser = webdriver.Chrome()
    url = 'https://www.lipin.com/signin.html?url=%2Faccount.html'

    wait = WebDriverWait(browser, 10)
    content = browser.get(url)

    # 获取cookie列表
    cookie_list = browser.get_cookies()
    # 格式化打印cookie
    # for cookie in cookie_list:
    #     cookie_dict[cookie['name']] = cookie['value']

    username_input = wait.until(Ec.presence_of_element_located((By.ID, "username")))
    # print(username_input)
    # exit()
    password_input = wait.until(Ec.presence_of_element_located((By.ID, "password")))

    username_input.send_keys("asi1225")
    password_input.send_keys("ajin9126")
    #

    # time.sleep(1)

    # subbmitBtn = wait.until(
    #     Ec.element_to_be_clickable((By.CSS_SELECTOR, '#login-form-0 > div:nth-child(4) > input.btn.btn-primary')))
    #
    # print(subbmitBtn)

    # subbmitBtn.click()
    # print(driver.page_source)


def main():
    # phantomJs()
    # exit()
    login()
    # get_list_order()
    # list_order()
    spider_order_data()


if __name__ == '__main__':
    main()
