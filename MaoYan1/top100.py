import time

import re
import json
from multiprocessing import Pool

from urllib.request import Request, urlopen

print(time.strftime('%Y-%m-%d %H:%M:%S %w-%Z', time.localtime()))



def get_page_one(url):
    # print(url)
    httpReq = Request(url)
    httpReq.add_header("User-Agent",
                       "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.99")
    httpReq.add_header("Host", "maoyan.com")

    html = urlopen(httpReq)
    return html.read().decode("utf-8")


def getMovieList(html, page):
    pattern = re.compile(
        '<dd>.*?>(\d+)</i>.*?<img.*?data-src="(.*?)".*?<a.*?title.*?>(\S+)</a>.*?<p.*?star.*?>(.*?)</p>.*?<p.*?releasetime.*?>(.*?)</p>.*?</dd>',
        re.S)
    # print("start---")
    items = re.findall(pattern, html)
    print(items)

    for item in items:
        yield {
            "top": item[0],
            "cover": item[1],
            "title": item[2],
            "actor": item[3].strip()[3:],
            "releaseTime": item[4].strip()[5:]
        }


def writeText(item):
    with open("top100.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False) + "\n")
        f.close()


def main(page):
    doc = get_page_one("http://maoyan.com/board/4?offset=" + str(page))

    # print(doc)
    for item in getMovieList(doc, page):
        # print(item)
        writeText(item)


# print(__name__)
if __name__ == "__main__":
    for i in range(10):
        main(i * 10)
    # 多线程
    # pool = Pool()
    # pool.map(main, [i * 10 for i in range(10)])
    # pool.close()
    # pool.join()

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
#
# soup = BS(html.content, "html.parser")
#
# print(soup.title.string)
