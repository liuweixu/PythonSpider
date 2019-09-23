from bs4 import BeautifulSoup
import requests, sys

class downloader(object):
    def __init__(self):
        self.server = "http://www.biqukan.com/"
        self.target = "http://www.biqukan.com/1_1094/"
        self.name = []
        self.url = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(url = self.target)   # 获取网页的内容。
        req.encoding = req.apparent_encoding    # 为了防止出现乱码，如果没有加这个的话，会出现乱码的。
        html = req.text
        div_soup = BeautifulSoup(html, "lxml")  # 解析，注意要加上'lxml'
        div = div_soup.find_all('div', class_ = 'listmain') # div的类型是bs4.element.ResultSet，是一个列表，不过在这个列表中，它的长度仅为1。
                                                            # 所以用div[0]读取内容。
        a_soup = BeautifulSoup(str(div[0]), "lxml") # Beautifulsoup()里面传入的是str类型。
        a = a_soup.find_all('a')
        self.nums = len(a[16:])
        for i in a[16:]:
            self.name.append(i.string)
            self.url.append(self.server + i.get('href'))    # i.get('href')是str类型。

    def get_content(self, target):
        req = requests.get(target)
        req.encoding = req.apparent_encoding    # 这个也是为了防止出现乱码的。
        html = req.text

        soup = BeautifulSoup(html, 'lxml')
        texts = soup.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace(' ','\n').replace('\xa0'*8,' ') # 这个我不懂为什么为什么要加这个。反正只要加了这个，
                                                                      # 就会输出需要的内容。
        return texts

    def writer(self, name, path, text):
        with open(path, 'a', encoding= 'utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print("开始下载：")
    for i in range(dl.nums):
        dl.writer(dl.name[i], '一念永恒.txt', dl.get_content(dl.url[i]))
        # print("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.write("\r" + "已下载:%.2f%%" % float(100.0 * i/dl.nums)) # 在一行动态输出，下面的一行也必须要写。
        sys.stdout.flush()
    print("下载结束")
