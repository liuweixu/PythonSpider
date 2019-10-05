# 用Pyquery重写崔庆才的《Python3网络爬虫开发实战》的猫眼爬取
import requests
from pyquery import PyQuery as pq
import time


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }
    html = requests.get(url=url, headers=headers)
    return html.text


def parse_one_page(html):
    doc = pq(html)
    items = doc('dd').items()
    for item in items:
        item1 = item.find('.board-item-main .board-item-content .movie-item-info')  # 空格表示嵌套
        item2 = item.find('.board-index')
        print('名次:' + item2.text())
        name = item1.find('.name').text()
        star = item1.find('.star').text()
        time = item1.find('.releasetime').text()
        score = item1.siblings('.movie-item-number .score .integer').text() + item1.siblings(
            '.movie-item-number .score .fraction').text()
        print('电影名:' + name + '\n' +
              star + '\n' + time + '\n' + '评分:' + score + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)  # 设置偏移量
    html = get_one_page(url)
    parse_one_page(html)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(1)  # 由于现在猫眼多了反爬虫，如果速度过快则无响应，所以要添加延时等待。
