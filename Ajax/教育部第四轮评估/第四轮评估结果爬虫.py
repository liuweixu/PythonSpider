import requests
from urllib.parse import urlencode
import os
import pandas as pd

base_url = "https://souky.eol.cn/api/newapi/assess_result?"

if not os.path.exists('第四轮评估'):
    os.mkdir('第四轮评估')

def getHTML(page):
    params = {
        'xid':page,
        'flag':1
    }
    url = base_url + urlencode(params)
    txt = requests.get(url, timeout=50)
    if txt.status_code == 200:
        return txt.json()  # 返回json文件
    else:
        return None

def save(json):
    if json:
        name = json[0]['name']
        path_name = ''
        if page in range(1, 19):
            if not os.path.exists('第四轮评估/人文社科类'):
                os.mkdir('第四轮评估/人文社科类')
            path_name = '第四轮评估/人文社科类'
        elif page in range(19, 33):
            if not os.path.exists('第四轮评估/理学'):
                os.mkdir('第四轮评估/理学')
            path_name = '第四轮评估/理学'
        elif page in range(33, 70):
            if not os.path.exists('第四轮评估/工学'):
                os.mkdir('第四轮评估/工学')
            path_name = '第四轮评估/工学'
        elif page in range(72, 81):
            if not os.path.exists('第四轮评估/农学'):
                os.mkdir('第四轮评估/农学')
            path_name = '第四轮评估/农学'
        elif page in range(81, 92):
            if not os.path.exists('第四轮评估/医学'):
                os.mkdir('第四轮评估/医学')
            path_name = '第四轮评估/医学'
        elif page in range(102, 107):
            if not os.path.exists('第四轮评估/管理学'):
                os.mkdir('第四轮评估/管理学')
            path_name = '第四轮评估/管理学'
        elif page in range(107, 112):
            if not os.path.exists('第四轮评估/设计学'):
                os.mkdir('第四轮评估/设计学')
            path_name = '第四轮评估/设计学'
        with open(path_name+'/{}.txt'.format(name), 'a+', encoding='utf-8') as f:
            f.write('序号,学校代码,学校名称,评选结果,排名百分比\n')
            for college in range(len(json[1])):
                f.write(str(college + 1) + ',')
                f.write(json[1][college]['scode'] + ',')
                f.write(json[1][college]['sname'] + ',')
                f.write(json[1][college]['result'] + ',')
                f.write(json[1][college]['percent'] + '\n')
        dataset = pd.read_csv(path_name+'/{}.txt'.format(name), sep=',', header=0, encoding='utf-8')
        dataset.to_csv(path_name+'/{}.csv'.format(name), index=False, encoding='utf-8')  # 保存为csv格式
        os.remove(path_name+'/{}.txt'.format(name))

if __name__ == '__main__':
    for page in range(1, 112):
        if page in range(70, 72) or page in range(92, 102) or page == 9 or page == 68 or page == 89 or page == 90:
            continue
        json = getHTML(page)
        save(json)
        print('第{}个'.format(page))
        # print(json)