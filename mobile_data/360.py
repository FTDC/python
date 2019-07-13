#!usr/bin/env python

import os
import urllib2
import urllib
import cookielib
import re

img_url = 'http://channel.360.cn/captcha.php'
login_url = 'http://channel.360.cn/login/login'
data_url = 'http://channel.360.cn/frontdata/index?app_id=3&start=2016-08-04&end=2016-08-04&channel_id=XXX'
username = 'XXX'
password = 'XXX'


def login():
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    print
    'open img url success'
    urllib2.install_opener(opener)
    img_req = urllib2.Request(img_url)
    img_response = opener.open(img_req)
    try:
        out = open('code.png', 'wb')
        # print img_response.read()
        out.write(img_response.read())
        out.flush()
        out.close()
        print
        'get code success'
    except IOError:
        print
        'file wrong'
    img_code = raw_input("please input code: ")
    print
    'your code is %s' % img_code
    # login
    LoginData = {
        'username': username,
        'password': password,
        'validate': img_code,
    };
    login_req = urllib2.Request(login_url, urllib.urlencode(LoginData));
    login_req.add_header('User-Agent', "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0");
    login_response = opener.open(login_req)
    print
    'login success'
    fout = open("Login.html", "w")
    fout.write(login_response.read())
    fout.close()
    # loda data page
    fout = open('Data.html', 'w')
    fout.write(opener.open(data_url).read())
    fout.close()


if __name__ == '__main__':
    login()
