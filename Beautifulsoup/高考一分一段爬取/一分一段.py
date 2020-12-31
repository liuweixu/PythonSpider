import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = "http://edu.sina.com.cn/gaokao/2019-06-14/doc-ihvhiqay5598618.shtml"
url = "http://kaoshi.edu.sina.com.cn/college/scorelist?tab=file&wl=&local="
provinces = ['-','北京','天津','上海','重庆','河北','河南','山东','山西','安徽','江西','江苏','浙江','湖北','湖南',\
             '广东','广西','云南','贵州','四川','陕西','青海','宁夏','黑龙江','吉林','辽宁','西藏','新疆','内蒙古','海南','福建','甘肃']


def page_parse(url):
    for pro in range(19, 20):
        if pro == 26 or pro == 27:
            continue
        url_pro = url + str(pro)
        for year in [2019,2018,2017]:
            url_year = url_pro + '&syear=' + str(year)
            for i in range(1, 72):
                url1 = url_year + '&page=' + str(i)
                print(url1)
                txt = requests.get(url=url1)
                txt.encoding = 'utf-8'
                txt = txt.text
                # print(html.xpath('//*[@id="score"]/div[2]/table/tbody/tr/td'))
                soup = BeautifulSoup(txt, 'lxml')
                # print(soup)
                with open('一分一段/{}一分一段.txt'.format(provinces[pro]), 'a+',encoding='utf-8') as f:
                    number = 1
                    for td in soup.select('.tabsContainer tr td')[7:]:
                        if number % 7 == 0:
                            number += 1
                            continue
                        elif number % 7 < 6:
                            f.write(td.get_text() + ',')
                            number += 1
                        else:
                            f.write(td.get_text() + '\n')
                            number += 1
                    print('省（直辖市）：{}.第{}页'.format(provinces[pro], i))

def PlusOne():
    for pro in range(1, 32):
        if pro == 26 or pro == 27:
            continue
        with open('一分一段/{}一分一段.txt'.format(provinces[pro]), 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write('年份,考生所在地,考生类别,分数段,本段人数,累计人数\n' + content)

def ToCsv():
    for pro in range(1, 32):
        if pro == 26 or pro == 27:
            continue
        dataset = pd.read_csv('一分一段/{}一分一段.txt'.format(provinces[pro]), sep=',', header=0, encoding='utf-8')
        dataset.to_csv('一分一段/{}一分一段.csv'.format(provinces[pro]), index=False, encoding='utf-8')  # 保存为csv格式

        

if __name__ == '__main__':
    page_parse(url)
    PlusOne()
    ToCsv()