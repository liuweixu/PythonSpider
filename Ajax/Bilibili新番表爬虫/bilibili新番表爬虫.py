import requests
from openpyxl import workbook

url = "https://bangumi.bilibili.com/web_api/timeline_global"


# 构建请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/77.0.3865.90 Safari/537.36'
}


# 获取json
def getText(url):
    text = requests.get(url, headers=headers)
    text.encoding = text.apparent_encoding
    if text.status_code == 200:
        return text.json()
    else:
        return None


# 从json获取需要的信息
def parse_Page(json):
    for i in range(len(json['result'])):
        item = json['result'][i]
        for subItem in item['seasons']:
            ws.append([subItem['title'], subItem['pub_time'],
                       item['day_of_week'], item['date'], subItem['cover']])


# 主函数
if __name__ == '__main__':
    json = getText(url)
    wb = workbook.Workbook()
    ws = wb.active
    ws.append(['标题', '播放时间', '周', '天', '封面链接'])
    parse_Page(json)
    wb.save('新番表.xlsx')