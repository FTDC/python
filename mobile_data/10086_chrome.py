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
    getSMSPwd1_btn.click()

    # p_name_input = wait.until(Ec.presence_of_element_located((By.ID, "p_name")))
    # p_name_input.send_keys("15172538022")

    # p_name_input = wait.until(Ec.presence_of_element_located((By.ID, "p_name")))
    # p_name_input.send_keys("15172538022")

    # 输入验证码
    checkCode = input("请输入验证码")
    sms_pwd_l_input = wait.until(Ec.presence_of_element_located((By.ID, "sms_pwd_l")))
    print(checkCode)
    sms_pwd_l_input.send_keys(checkCode)

    # 点击登录
    submit_bt_btn = wait.until(Ec.element_to_be_clickable((By.ID, 'submit_bt')))
    submit_bt_btn.click()

    # print(subbmitBtn)



    # print(driver.page_source)


def main():
    phantomJs()
    # login()
    # get_list_order()
    # list_order()
    # spider_order_data()


if __name__ == '__main__':
    main()
