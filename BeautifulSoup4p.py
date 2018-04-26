import requests
from bs4 import BeautifulSoup


def getHtml():
    try:
        r = requests.get("http://python123.io/ws/demo.html")
        r.raise_for_status()
        # print(r.status_code)
        # print(r.text[:3000])
        return r.text
    except:
        print("爬取失败")


def useBS4():
    demo = getHtml()
    soup = BeautifulSoup(demo, "html.parser")
    print(soup.prettify())  # 给HTML文档加上空格和换行，增加文档的可读性

    # BeautifulSoup类的基本元素
    print(soup.a)  # 标签
    print(soup.a.name)  # 标签的名字
    print(soup.a.attrs)  # 标签的属性
    print(soup.a.string)  # 标签内非属性字符串

    # 基于bs4库的HTML内容遍历方法


if __name__ == "__main__":
    useBS4()
