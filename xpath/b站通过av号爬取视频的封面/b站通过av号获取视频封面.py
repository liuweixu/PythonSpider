import requests
from lxml import etree
import os

# 请求头
headers = {
    'Access-Control-Request-Headers': 'range',
    'Access-Control-Request-Method': 'GET',
    'Origin': 'https://www.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    'Referer': 'https://www.bilibili.com'
}
# 图片页所在的网址的请求头，注意去掉'Host: '、'If-None-Match'等等，因为不同的图片这些可能不同。
headers1 = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,\
    image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,ja-CN;q=0.6,ja;q=0.5',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

base_url = "https://www.bilibili.com/video/"


# 获取图片的链接。
def getText(url):
    text = requests.get(url, headers=headers)
    text.encoding = text.apparent_encoding
    if text.status_code == 200:
        return text.text
    else:
        return False


# 获取图片，并下载图片
def getImage(text):
    html = etree.HTML(text)
    image = html.xpath('/html/head/meta[10]/@content')[0]
    title = html.xpath('/html/head/meta[8]/@content')[0]
    if not os.path.exists(av):
        os.makedirs(av)
    r = requests.get(image, headers=headers1)
    with open('./' + av + "/{}".format(image.split("/")[-1]), 'wb') as f:
        print(r)  # 如果是’<Response [200]>‘说明OK，如果是'<Response [403]>'说明需要处理反爬，一般来说加请求头可以了
        f.write(r.content)


if __name__ == '__main__':
    while True:
        av = input("请输入带有'av'的av号：")
        if av[0] != 'a' or av[1] != 'v':
            print("输入的av号有误，请重新输入")
            continue
        url = base_url + av
        text = getText(url)
        if text == False:
            print("输入的av号不存在，请重新输入")
            continue
        else:
            break
    getImage(text)
