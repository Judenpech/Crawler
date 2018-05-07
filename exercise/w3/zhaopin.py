# 智联招聘主要城市[互联网/电子商务+计算机软件+IT服务（系统/数据/维护）]爬虫
import requests
from bs4 import BeautifulSoup
import re


def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def getCityList(clst, cityURL):
    html = getHTMLText(cityURL)
    soup = BeautifulSoup(html, "html.parser")
    main_city = soup.find(name='div', attrs={'class': 'main'})
    a = main_city.find_all('a')
    for i in a:
        try:
            clst.append(i.string)
        except:
            continue


def getJobInfo(clst, jobURL, depth, fpath):
    cnt = 0
    for city in clst:
        for page in range(depth):
            url = jobURL + city + "&p=" + str(page+1)
            html=getHTMLText(url)
            try:
                if html=="":
                    continue
                infoDict={}
                soup=BeautifulSoup(html,"html.parser")
                main=soup.find(name='div',attrs={"class":"search_newlist_main"})
                print(main)
                break;
            except:
                print("出错")
                continue
        break;



def main():
    city_list_url = "https://www.zhaopin.com/citymap.html"
    job_info_url = "https://sou.zhaopin.com/jobs/searchresult.ashx?in=210500%3B160400%3B160000&jl="
    depth = 2  # 页数
    output_file = "D:/zhaopin.txt"
    clist = []
    getCityList(clist, city_list_url)
    getJobInfo(clist, job_info_url, depth, output_file)


main()
