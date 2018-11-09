from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import re
import pymysql.cursors

request = Request("https://en.wikipedia.org/wiki/Wiki")

doc = urlopen(request).read().decode("utf-8")

soup = bs(doc, "html.parser")
# 数据库连接
connection = pymysql.connect(host="localhost", user="root", port=3306, password="password", db="python",
                             charset="utf8", cursorclass=pymysql.cursors.DictCursor)
try:

    with connection.cursor() as cursor:
        # 写入数据
        # for wordLink in soup.find_all("a", href=re.compile("^\/wiki")):
        #     if not re.search("\.jpg|JPG|js", wordLink["href"]):
        #         print(wordLink.string, "----", wordLink.get("href"))
        #
        #         # 写入新的记录
        #         sql = "insert into word (`word`, `linkurl`) VALUES (%s, %s)"
        #         res = cursor.execute(sql, (wordLink.get_text(), wordLink.get("href")))
        #
        #         connection.commit()

        # 查询数据
        sql2 = "select id, word, linkurl from  word where id > %s"
        count = cursor.execute(sql2, (20,))
        print(count)
        result = cursor.fetchone();
        print(result)

        result2 = cursor.fetchmany(20);
        print(result2)

        result3 = cursor.fetchall();
        print(result3)

        # connection.commit()

finally:
    connection.close()

# print(soup.title.string)
