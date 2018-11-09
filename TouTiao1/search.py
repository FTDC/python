import re
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import requests
from requests.exceptions import HTTPError
import json

data = {
    'offset': 0,
    'format': 'json',
    'keyword': '街拍',
    'autoload': 'true',
    'count': 20,
    'cur_tab': 3,
    'from': 'gallery'
}

url = "https://www.toutiao.com/search_content/?" + urlencode(data)
try:
    response = requests.get(url)

    if response.status_code == 200:
        print(response.text)
    #     print(response)
    # print("链接错误1")

except HTTPError as hte:
    print("链接错误")

responseJson = json.loads(response.text, encoding="utf-8")

print(responseJson)
print(responseJson['data'])



def get_page(url):
    print(url)
    req = Request(url)
    req.add_header("user-agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36")
    # req.add_header("user-agent","")
    html = urlopen(req).read().decode('utf-8')
    # print(html)

    pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)

    result = re.search(pattern, html)
    if result:
        jsonImgs = json.loads(result)
        print(jsonImgs)
    print(result, "json")

    # print(html.read().decode('utf-8'))


# listAritic
for item in responseJson['data']:
    print(item['open_url'])
    url = "https://www.toutiao.com" + item["open_url"]
    print(requests.get("https://www.toutiao.com" + item["open_url"]).text)

    get_page(url)
    exit()
