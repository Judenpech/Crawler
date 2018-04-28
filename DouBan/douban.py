import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillBookList(blist, html):
    soup = BeautifulSoup(html, "html.parser")
    content = soup.find(name="div", id="content")
    title = content.find("h1").string
    book = []
    desc = []
    for i in content.find(name="div", attrs="article").find_all("h2"):
        book.append(i.a.string)
    for i in content.find_all(name='p', attrs="subject-abstract color-gray"):
        desc.append(i.string.strip())
    for i in range(len(book)):
        blist.append([book[i], desc[i]])
    return title


def printBookList(title, blist):
    print("{:-^80}".format(title))
    tplt = "{0:20}\t{1:{2}^40}"
    print("{0:^20}\t{1:{2}^40}".format("书名", "详细信息", chr(12288)))
    for i in range(len(blist)):
        print(tplt.format(blist[i][0], blist[i][1], chr(12288)))


def main():
    url="https://book.douban.com/chart?subcat=I"
    #url = "https://book.douban.com/chart?subcat=F"
    binfo = []
    html = getHTMLText(url)
    title = fillBookList(binfo, html)
    printBookList(title, binfo)


main()
