# 计算成功爬取页面100次所需时间
import requests, time


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'


if __name__ == "__main__":
    url = "http://www.baidu.com"
    start = time.clock()
    flag = 1
    for i in range(100):
        re = getHTMLText(url)
        if re == "error":
            print("第{}次爬取网页产生异常，程序终止！".format(i + 1), end="")
            flag = 0
            break
    end = time.clock()
    if flag:
        print("成功爬取100次网页的时间为{:.6f}秒。".format(end - start))
    else:
        print("耗时{:.6f}秒。".format(end - start))
