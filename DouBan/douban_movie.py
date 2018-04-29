import requests
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""


def fillMovieList(mlist,html):
    soup=BeautifulSoup(html,"html.parser")
    nowplaying=soup.find(name="div",id="nowplaying")

    pass

def printMovieList():
    print()

def main():
    url = "https://movie.douban.com/cinema/nowplaying/fuzhou/"
    minfo=[]
    html=getHTMLText(url)
    fillMovieList(minfo,html)
    printMovieList(minfo)