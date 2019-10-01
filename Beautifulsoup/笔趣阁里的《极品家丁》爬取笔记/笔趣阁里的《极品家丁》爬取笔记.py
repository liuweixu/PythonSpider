import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/77.0.3865.90 Safari/537.36"
}

list_url = []
list_title = []
target = "https://www.biqukan.com"


# 爬取笔趣看的《极品家丁》的目录页
def getHtmlList(url):
    text = requests.get(url, headers=headers)
    text.encoding = text.apparent_encoding
    if text.status_code == 200:
        text = text.text
        soup = BeautifulSoup(text, 'lxml')
        soup = soup.prettify()
        soup = BeautifulSoup(soup, 'lxml')
        div = soup.find_all("div", class_="listmain")
        a_soup = div[0].find_all("a")
        for item in a_soup:
            list_url.append(target + item.get("href"))
            list_title.append(item.string.replace("\n", "").strip())
    else:
        return None


# 爬取每个目录文章的内容，由于在笔趣看的书中，每个目录的的内容格式是几乎一样的。
def getHtmlContent(url):
    txt = requests.get(url, headers=headers)
    txt.encoding = txt.apparent_encoding
    if txt.status_code == 200:
        return txt.text
    else:
        return None


# 用Beautifulsoup解析爬取的内容，注意"\xa0"。
def parse_content(txt):
    soup = BeautifulSoup(txt, 'lxml')
    div = soup.find_all('div', class_='showtxt')
    text = div[0].text.replace(" ", "\n").replace("\xa0" * 8, ' ')
    return text


# 保存
def save_text(text, path):
    with open("./极品家丁/{}.txt".format(path), "w", encoding="utf-8") as f:
        f.writelines(text)


if __name__ == '__main__':
    url = 'https://www.biqukan.com/3_3053/'
    getHtmlList(url)
    list_url = list_url[13:]
    list_title = list_title[13:]
    for i in range(len(list_url)):
        text = getHtmlContent(list_url[i])
        text = parse_content(text)
        save_text(text, list_title[i])
        print("\r" + "下载进度：{:.2f}%".format(i / len(list_url) * 100), end="", flush=True)
