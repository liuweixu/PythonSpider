import requests
import collections
import os
import time

'''
输入爬取范围的起始时间，例子：想输入2020年12月2日时，应输入20201205，不能输错，否则不能爬取。
'''
print('开始时间：', end='')
start_time = input()
print('结束时间：', end='')
end_time = input()

dicCodesName = collections.defaultdict()

# 建立一个header，字典类型，可以从Google浏览器拷贝。用于伪装成一个浏览器用。
headers = {
    'Referer': 'http://quotes.money.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/87.0.4280.88 Safari/537.36'
}

def CodeNamePage():

    #用于爬取代码，网址如下，count后面的数字可以手动改，我改4148是为了方便一页爬下来所有的代码，这些代码用于后面的爬取数据用。
    url_base = 'http://quotes.money.163.com/hs/service/diyrank.php?host=http%3A%2F%2Fquotes.money.163.com%2Fhs%2Fservice%2Fdiyrank.php&page=0&query=STYPE%3AEQA&fields=NO%2CSYMBOL%2CNAME%2CPRICE%2CPERCENT%2CUPDOWN%2CFIVE_MINUTE%2COPEN%2CYESTCLOSE%2CHIGH%2CLOW%2CVOLUME%2CTURNOVER%2CHS%2CLB%2CWB%2CZF%2CPE%2CMCAP%2CTCAP%2CMFSUM%2CMFRATIO.MFRATIO2%2CMFRATIO.MFRATIO10%2CSNAME%2CCODE%2CANNOUNMT%2CUVSNEWS&sort=PERCENT&order=desc&count=4148&type=query'

    text = requests.get(url_base, headers=headers)
    results = text.json() #最后得到json格式
    # print(results)

    #把代码和对应的公司的名字存到一个字典中
    for result in results['list']:
        dicCodesName[result['CODE']] = result['NAME']

def DataSave():
    num = 0
    for key in dicCodesName.keys():
        num += 1
        stockName = dicCodesName[key]
        stockCode = key
        # 将股票名的一些不符合windows的文件名删掉，便于保存文件
        for s in ['<', '>', '/', '\\', '|', ':', '\"', '*', '?']:
            if s in stockName:
                stockName = stockName.replace(s, '')
        #开始爬取
        data_url = 'http://quotes.money.163.com/service/chddata.html?code={}&start={}&end={}&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'.format(stockCode, start_time, end_time)
        # print(data_url)
        data = requests.get(data_url, headers=headers).text
        data = data.encode()
        # print(data)
        if not os.path.exists('E:/stock_data'):
            os.makedirs('E:/stock_data')
        path = 'E:/stock_data/{}.csv'.format(stockName)
        with open(path, 'wb') as f:  # 保存数据
            f.write(data)
        print('\r' + '已下载：{:.2f}%'.format(num/4148 * 100), end='', flush=True)
        time.sleep(1) #控制爬取时间，避免由于爬取太快被封IP
    print('\n已下载完毕')

if __name__ == "__main__":
    CodeNamePage()
    DataSave()
