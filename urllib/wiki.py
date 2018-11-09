from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
import re

request = Request("https://en.wikipedia.org/wiki/Wiki")

doc = urlopen(request).read().decode("utf-8")

soup = bs(doc, "html.parser")

for wordLink in soup.find_all("a", href=re.compile("^\/wiki")):
    if not re.search("\.jpg|JPG|js", wordLink["href"]):
        print(wordLink.string, "----", wordLink.get("href"))

print(soup.title.string)
