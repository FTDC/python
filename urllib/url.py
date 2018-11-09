from urllib.request import Request, urlopen
from urllib import parse

req = Request("https://www.baidu.com")

postData = parse.urlencode([
    ("name", "sd")
])

req.add_header("Host", "www.baidu.com")

req.add_header("Accept-Language", "zh-CN,zh;q=0.9")
# req.add_header("User-Agent",
#                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36")

resp = urlopen(req, data=postData.encode("utf-8"))
# print("sers"+"sdf")


print(resp.read().decode("utf-8"))
