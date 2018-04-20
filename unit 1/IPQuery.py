# IP地址归属地的自动查询
import requests


def getHtml(url, ip):
    kv = {"user-agent": "Mozilla/5.0"}
    try:
        r = requests.get(url + ip)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.status_code)
        print(r.request.url)
        print(r.text[-2500:])
    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "http://www.ip138.com/ips138.asp?ip="
    ip = "210.34.74.201"
    getHtml(url, ip)
