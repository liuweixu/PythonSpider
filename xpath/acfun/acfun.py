import requests
from bs4 import BeautifulSoup
from lxml import etree
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/77.0.3865.90 Safari/537.36'
}


def getHtml(url):
    text = requests.get(url, headers=headers)
    text.encoding = text.apparent_encoding
    if text.status_code == 200:
        return text.text
    else:
        return None


def parse_page(text):
    html = etree.HTML(text)
    return html


def getImageSrc(html):
    image_src = html.xpath('//*[@id="bangumiList"]/div/ul/li/a/div[1]/img/@src')
    return image_src


def getTitle(html):
    title = html.xpath('//*[@id="bangumiList"]/div/ul/li/a/div[2]/@title')
    return title


def getNumOfPeople(html):
    numOfPeople = html.xpath('//*[@id="bangumiList"]/div/ul/li/a/div[1]/div/text()')
    return numOfPeople


def getnumOfAnime(html):
    numOfAnime = html.xpath('//*[@id="bangumiList"]/div/ul/li/a/div[2]/em/text()')
    return numOfAnime


if __name__ == '__main__':
    path = "ImageOfAcFun"
    if not os.path.exists(path):
        os.makedirs(path)
    with open("./" + path + "/Acfun番剧.txt", "w", encoding="utf-8") as f:
        base_url = "https://www.acfun.cn/bangumilist?filters=10,20,30,40,50,805306368&pageNum="
        for page in range(1, 12):
            url = base_url + str(page)
            text = getHtml(url)
            html = parse_page(text)
            image_src = getImageSrc(html)
            title = getTitle(html)
            numOfPeople = getNumOfPeople(html)
            numOfAnime = getnumOfAnime(html)
            for i in range(len(title)):
                f.write("{}的图片的链接：{}".format(title[i], image_src[i]) + "\n")
                f.write("{}的集数：{}".format(title[i], numOfAnime[i]) + "\n")
                f.write("受欢迎程度：{}".format(numOfPeople[i]) + "\n")
                f.write("-----------------------------------------------------------------------------\n")
                print("\r" + "第{}页的下载进度：{:.2f}%".format(page, i / len(title) * 100), end="", flush=True)
