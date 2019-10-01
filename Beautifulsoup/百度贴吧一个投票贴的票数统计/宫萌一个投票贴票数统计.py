import requests
from lxml import etree
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/77.0.3865.90 Safari/537.36'
}

base_url = "https://tieba.baidu.com/p/6037027728?pn="
url = "https://tieba.baidu.com/p/6037027728"

name = []


def get_Maxpage(url):
    text = requests.get(url, headers=headers)
    text.encoding = text.apparent_encoding
    if text.status_code == 200:
        html = etree.HTML(text.text)
        max_page = html.xpath('//*[@id=\"thread_theme_5\"]/div[1]/ul/li[2]/span[2]/text()')[0]
        return int(max_page)
    else:
        return None


def get_Text(url):
    text = requests.get(url, headers=headers)
    text.encoding = text.apparent_encoding
    if text.status_code == 200:
        return text.text
    else:
        return None


def get_Name(text):
    soup = BeautifulSoup(text, 'lxml')
    name1 = soup.select(".d_post_content")
    for i in name1:
        if len(i.get_text()) <= 20:
            str_name = i.get_text().strip()
            str_name = str_name.split('@')[0]
            name.append(str_name)
    name2 = soup.select('.post_bubble_middle_inner')
    for i in name2:
        if len(i.get_text()) <= 20:
            str_name = i.get_text().strip()
            str_name = str_name.split('@')[0]
            name.append(str_name)


if __name__ == '__main__':
    max_page = get_Maxpage(url)
    for page in range(1, max_page + 1):
        url = base_url + str(page)
        text = get_Text(url)
        get_Name(text)
        print("\r" + "已完成的百分比：{:.2f}%".format(page / max_page * 100), end="", flush=True)
    print("\n有重复投票的可能！！！\n")
    print("蕾姆：{}票".format(name.count('蕾姆')))
    print("南宫那月：{}票".format(name.count('南宫那月')))
