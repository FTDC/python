import json
import os
import re
from _md5 import md5
from multiprocessing.pool import Pool
from urllib.parse import urlencode
from urllib.request import Request, urlopen

import requests
from requests.exceptions import HTTPError

from Support.Helper import dd


def get_index_page():
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
    print(responseJson['data'])

    return responseJson['data']


def download_image(url):
    print("Downloading .....", url)
    fileName = "time.microsecond" + ".jpg"
    # dd(url)
    # exit()
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # print(response.content)
            saveImage(response.content)
            # return response.content
        return None
    except ConnectionError:
        return None


def saveImage(content):
    # print(content)
    # exit()
    file_path = '{0}/{1}.{2}'.format(os.getcwd(), md5(content).hexdigest(), 'jpg')
    print(file_path)
    if not os.path.exists(file_path):
        with open(file_path, 'wb') as f:
            f.write(content)
            f.close()


def get_page(url):
    print(url)
    req = Request(url)
    req.add_header("user-agent",
                   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36")
    # req.add_header("user-agent","")
    html = urlopen(req).read().decode('utf-8')
    # print(html)

    # pattern = re.compile('gallery: JSON.parse\("(.*)\),', re.S)
    pattern = re.compile('gallery: JSON.parse\("(.*)"\),', re.S)

    result = re.search(pattern, html)
    jsonString = result.group(1).replace("\\", '')
    print(jsonString, "json")
    # exit()
    if result:
        jsonImgs = json.loads(jsonString)
        urlList = jsonImgs['sub_images']

        urlimg = []
        for img in urlList:
            urlimg.append(img["url"])
            # print(img["url"])
            download_image(img['url'])
        # dd(urlimg)

        # 子线程里面不能申明多线程
        # pool = Pool()
        # group = urlimg
        # pool.map(download_image, group)
        # pool.join()
        # pool.close()

        # print(urlList)

    # print(html.read().decode('utf-8'))


# listAritic
def main(offset):
    # dump(get_index_page())
    for item in get_index_page():
        # dump(item)
        url = "https://www.toutiao.com" + item["open_url"]
        print(requests.get("https://www.toutiao.com" + item["open_url"]).text)

        get_page(url)
        # exit()


if __name__ == '__main__':
    pool = Pool()
    # group = ([x * 20 for x in range(1, 4)])
    # # dump(group)
    # pool.map(main, group)
    # pool.join()
    pool.close()
    main(1)
