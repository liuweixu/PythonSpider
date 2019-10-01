# encoding='utf-8'
import requests
from urllib.parse import urlencode

links = []
base_url = "https://bcy.net/apiv3/rank/list/itemInfo?"


def getHTMLText(page):
    # 构建请求头
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-CN;q=0.8,en;q=0.7,ja-CN;q=0.6,ja;q=0.5",
        "x-requested-with": "xmlhttprequest",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
    }
    # 构建参数
    params = {
        'p': page,
        'ttype': 'illust',
        'sub_type': 'week',
        'date': '20190923'
    }
    # 利用urlencode将参数解析为带有"&"链接的的字符串，和base_url组成可以访问的链接。
    url = base_url + urlencode(params)
    txt = requests.get(url, headers=headers, timeout=50)
    if txt.status_code == 200:
        return txt.json()  # 返回json文件
    else:
        return None


# 解析，不过由于返回的是json文件，可以利用json的特点（类似字典）来查找自己需要找的信息。
def parse_page(json):
    if json:
        for i in range(20):
            ls = json['data']['top_list_item_info'][i]['item_detail']['multi']
            for item in ls:
                links.append(item['path'])


def Image_save(links, num):
    for i in range(1, num + 1):
        html = requests.get(links[i - 1])
        with open("./Image/{}.jpg".format(i), "wb") as f:
            f.write(html.content)


if __name__ == "__main__":
    for page in range(1, 4):
        json = getHTMLText(page)
        parse_page(json)
    length = len(links)
    Image_save(links, length)
