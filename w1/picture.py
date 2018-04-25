# 网络图片的爬取和存储
import requests, os


def getPic(url, root):
    path = root + url.split('/')[-1]
    kv = {"user-agent": "Mozilla/5.0"}
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url, headers=kv)
            r.raise_for_status()
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "http://www.fjtcm.edu.cn/u/cms/www/201612/0615563401s4.jpg"
    root = "D://pics//"
    getPic(url, root)
