import urllib
from urllib.parse import urlencode

from Support.Helper import dd

__author__ = 'CQC'
# -*- coding:utf-8 -*-

from urllib.request import Request
import re
import webbrowser
import http.cookiejar


# 模拟登录淘宝类
class Taobao:

    # 初始化方法
    def __init__(self):
        # 登录的URL
        self.loginURL = "https://login.taobao.com/member/login.jhtml"
        # 代理IP地址，防止自己的IP被封禁
        self.proxyURL = 'http://120.193.146.97:843'
        # 登录POST数据时发送的头部信息
        self.loginHeaders = {
            'Host': 'login.taobao.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer': 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive'
        }
        # 用户名
        self.username = 'asi1225'
        # ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua = '113#21HoOffFfpmYnf4AGfFRFsbxbsk0Se6Jjof6bFbOdPuPVz8Ikg3pDywsnz9fhK5D16F6bu5gyKE+DaDok0LuKlTxbt9ooD6D1PF64Fbfs61X0idsxWvnoYi3bYofxDzeiKkW2044sPkA/TLK/y5iUMJVbYoYkW/d815Bco7joLNWoyk6k0bnDsJDTFCiW0Ru161WbFiFdPN8DsDNkWVJSy9xbsdWHD5o16FWbFiOGokXRsG+kTSnDri7bYxOk/qfpYKCCl2dwE8K12tUviVO+nWTXAPWQvrH6YKZClQ92atLC1SOHWNEPDOGrMHMbk4OvcCIutNK3FR3aaxhQuxNsmdbNRweLOXFwnYh31PX+0BzxiS6+LGl7UMaIiV88RWmXBuvMvF8EZIKwoLf7g73GEo6jgZaFfSCl3yj/ydHmBixA5l/qwDF7QVytuOF5yFOyzTvs3iAl/PL7BRYKcK0j69bcW35kPbC0pfMmG7Rk+eDB6m7dDuFp/A3TEiho1iOk2b5IkPmsCV0/LGz1Ht6ZZZVt7hXbUfTWH+eVogOKEZ3durlj9K0zpKcEqi9GFgdHxF05PSmLIXUn9z7neRUf5E4gP09xKhJ9AjEx0yRuEBM9yw4Ofk9rPjfc/vZhniFGyWALNZVKXRY3OCYzfjBm8KfXhynAjkVdKr7qiAYOrXyIkRtAZdTtANquqSGT4h/ivzVLV+pvf8bz4RikwqR+1mDXv+gC8JGPLylF96HzBzrXKckb+T4kUABDhegg53ev4EUSu4RpCsy1M70cZU2BF217Vtr1yV6ftkgieTu5t2FUZ9g7vW1x2GEphEjcQUFeNcsQ7pXVHxhaxF/ngqrrArS03ROiE1VxYbbK3P7dilW4n5XFWegXRc1M0HrugWTy7RYeOWM7k/RGL7SJaqiv6i0c2wKsqvECBI9/BxoBBdF0SreqRVMJ2LvduSR1HzxFPFx+TpeFigk/H0UQpUlchb4huUnrbnb4GztxyV7v7vGyLOKAUj7xPB74AJ/'
        # 密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2 = '43da9b707213f4cff4a88703899ad938251faf1cbadc59a379013d213757dd7d077a08418fe1efe911ab5a5ddeb19a3989c2aa5d60917de0a6a7c346468ba28b0f5b13065f55965543382f3e0e24c89e58a3292a6638af1d29f79620e70d1a4f2f97db69cc53b5e294cdbd1c85a9edddb835a48c183a976cb4210f1c18925084'
        self.post = post = {
            'ua': self.ua,
            'TPL_checkcode': '',
            'CtrlVersion': '1,0,0,7',
            'TPL_password': '',
            'TPL_redirect_url': 'http://i.taobao.com/my_taobao.htm?nekot=udm8087E1424147022443',
            'TPL_username': self.username,
            'loginsite': '0',
            'newlogin': '0',
            'from': 'tb',
            'fc': 'default',
            'style': 'default',
            'css_style': '',
            'tid': 'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
            'support': '000001',
            'loginType': '4',
            'minititle': '',
            'minipara': '',
            'umto': 'NaN',
            'pstrong': '3',
            'llnick': '',
            'sign': '',
            'need_sign': '',
            'isIgnore': '',
            'full_redirect': '',
            'popid': '',
            'callback': '',
            'guf': '',
            'not_duplite_str': '',
            'need_user_id': '',
            'poy': '',
            'gvfdcname': '10',
            'gvfdcre': '',
            'from_encoding ': '',
            'sub': '',
            'TPL_password_2': self.password2,
            'loginASR': '1',
            'loginASRSuc': '1',
            'allp': '',
            'oslanguage': 'zh-CN',
            'sr': '1366*768',
            'osVer': 'windows|6.1',
            'naviVer': 'firefox|35'
        }
        # 将POST的数据进行编码转换
        self.postData = urlencode(self.post)
        # 设置代理
        self.proxy = urllib.request.ProxyHandler({'http': self.proxyURL})
        # 设置cookie
        self.cookie = http.cookiejar.LWPCookieJar()
        # 设置cookie处理器
        self.cookieHandler = urllib.request.HTTPCookieProcessor(self.cookie)
        # 设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib.request.build_opener(self.cookieHandler, self.proxy, urllib.request.HTTPHandler)


    # 得到是否需要输入验证码，这次请求的相应有时会不同，有时需要验证有时不需要
    def needIdenCode(self):
        # 第一次登录获取验证码尝试，构建request
        request = urllib.request.Request(self.loginURL, self.postData, self.loginHeaders)
        # 得到第一次登录尝试的相应
        response = self.opener.open(request)
        dd(response)
        # 获取其中的内容
        content = response.read().decode('gbk')
        # 获取状态吗
        status = response.getcode()
        # 状态码为200，获取成功
        if status == 200:
            print
            u"获取请求成功"
            # \u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801这六个字是请输入验证码的utf-8编码
            pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801', re.S)
            result = re.search(pattern, content)
            # 如果找到该字符，代表需要输入验证码
            if result:
                print
                u"此次安全验证异常，您需要输入验证码"
                return content
            # 否则不需要
            else:
                print
                u"此次安全验证通过，您这次不需要输入验证码"
                return False
        else:
            print
            u"获取请求失败"

    # 得到验证码图片
    def getIdenCode(self, page):
        # 得到验证码的图片
        pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"', re.S)
        # 匹配的结果
        matchResult = re.search(pattern, page)
        # 已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            print
            matchResult.group(1)
            return matchResult.group(1)
        else:
            print
            u"没有找到验证码内容"
            return False

    # 程序运行主干
    def main(self):
        # 是否需要验证码，是则得到页面内容，不是则返回False
        needResult = self.needIdenCode()
        if not needResult == False:
            print
            u"您需要手动输入验证码"
            idenCode = self.getIdenCode(needResult)
            # 得到了验证码的链接
            if not idenCode == False:
                print
                u"验证码获取成功"
                print
                u"请在浏览器中输入您看到的验证码"
                webbrowser.open_new_tab(idenCode)
            # 验证码链接为空，无效验证码
            else:
                print
                u"验证码获取失败，请重试"
        else:
            print
            u"不需要输入验证码"


taobao = Taobao()
taobao.main()
