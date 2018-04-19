# 爬取京东商品页面
import requests


def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text[:1000])
    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "https://item.jd.com/4675696.html"
    getHtml(url)
