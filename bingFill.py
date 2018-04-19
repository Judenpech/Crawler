# bing提交搜索关键词
import requests


def getHtml(url, keyword):
    kv = {"q": keyword}  # bing关键词提交接口
    hds = {"headers": "Mozilla/5.0"}
    try:
        r = requests.get(url, params=kv, headers=hds)
        print(r.request.url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(len(r.text))
        print(r.text[:3000])
    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "http://cn.bing.com/search"
    keyword = "福建中医药大学"
    getHtml(url, keyword)
