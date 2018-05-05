import requests
import re


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parsePage(mlist, html):
    try:
        title_lt = re.findall(r'data-title\=\".*?\"', html)
        score_lt = re.findall(r'data-score\=\".*?\"', html)
        duration_lt = re.findall(r'data-duration\=\".*?\"', html)
        director_lt = re.findall(r'data-director\=\".*?\"', html)
        actors_lt = re.findall(r'data-actors\=\".*?\"', html)
        for i in range(len(title_lt)):
            title = eval(title_lt[i].split('=')[1])
            score = eval(score_lt[i].split('=')[1])
            duration = eval(duration_lt[i].split('=')[1])
            director = eval(director_lt[i].split('=')[1])
            actors = eval(actors_lt[i].split('=')[1])
            mlist.append([title, score, duration, director, actors])
    except:
        print("")


def printMovieList(mlist):
    tplt = "{0:20}\t{1:10}\t{2:15}\t{3:15}\t{4:25}"
    print(tplt.format("名称", "评分", "时长", "导演", "演员"))
    for m in mlist:
        print(tplt.format(m[0], m[1], m[2], m[3], m[4]))


def main():
    url = "https://movie.douban.com/cinema/nowplaying/fuzhou/"
    minfo = []
    html = getHTMLText(url)
    parsePage(minfo, html)
    printMovieList(minfo)


main()
