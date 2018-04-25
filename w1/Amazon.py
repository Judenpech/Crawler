# 爬取 Amazon 商品页面
import requests


def getHtml(url):
    kv = {"user-agent": "Mozilla/5.0"}
    try:
        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(r.text)
    except:
        print("爬取失败")


if __name__ == "__main__":
    url = "https://www.amazon.cn/dp/B00QJDOLIO/ref=br_bsl_pdt-1?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=desktop-bestsellers-1&pf_rd_r=M1S3BBKF08203QNGZV2W&pf_rd_r=M1S3BBKF08203QNGZV2W&pf_rd_t=36701&pf_rd_p=3851c05c-0a77-4cb4-a09f-3c4339dee85f&pf_rd_p=3851c05c-0a77-4cb4-a09f-3c4339dee85f&pf_rd_i=desktop"
    getHtml(url)
