import re
from urllib.request import Request, urlopen
import urllib
import parser
import http.cookiejar

from bs4 import BeautifulSoup as bs

req = Request('https://www.lipin.com/account/act_selldetail')

doc = urlopen(req)

soup = doc.read().decode("utf-8")

html = bs(soup, "html.parser")
print(html.title.string)
print(html)

if re.search("^用户登陆.*", html.title.string, re.S):
    print(html.title.string)

fromHash = html.input(name="formhash")
print(fromHash)
# 模拟用户登陆
# session_requests = requests.session()

loginFromData = urllib.parse.urlencode([
    ("username", "asi1225"),
    ("password", "ajin9126"),
    ("refer", " https://www.lipin.com/setdata/do_out"),
    ("formhash", "formhash")
])
