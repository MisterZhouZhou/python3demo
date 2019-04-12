import pandas as pd
import requests
import re
import json
import os

# 匹配City_ID中的数字
def convert(x):
    reg = re.compile('(\d+)')
    return reg.search(x).group()

# 读取城市信息
def readCity():
    file = pd.read_csv('city_code.csv')
    # 选择需要的两列信息
    file = file.loc[:, ['City_ID', 'City_CN']]
    # 读取前5行
    file.head()
    file['City_ID_map'] = file['City_ID'].map(convert)
    return file

# 建立城市与代码之间的映射关系
def cityToId(file):
    code_dict = {}
    key = 'City_CN'
    value = 'City_ID_map'
    for k,v in zip(file[key], file[value]):
        code_dict[k] = v
    return code_dict

# 将所得的字典数据存储为 txt 文件
def writeToFile(fileName, codeDict):
    with open(fileName, 'w') as f:
        json.dump(codeDict, f)


# 读取城市txt文件
def readFile(filename):
    with open(filename, 'r') as f:
        text = json.load(f)
    return text

# 天气查询
def query_weather(code):
    url = f'http://wthrcdn.etouch.cn/weather_mini?citykey={code}'
    try:
        info = requests.get(url)
        info.encoding = 'utf-8'
    except requests.ConnectionError:
        raise
    try:
        info_json = info.json()
    except json.JSONDecodeError:
        return '查询失败'
    return info_json

# 天气数据格式化
def formatWeather(info_json):
    # 天气情况
    dataArray = []
    data = info_json['data']
    city = f"城市：{data['city']}\n"
    dataArray.append(city)
    forecast_array = data['forecast']
    for index in range(0,len(forecast_array)):
        day_dict = forecast_array[index]
        dataArray.append(f"日期：{day_dict['date']}\n")
        if index == 0:
            dataArray.append(f"实时温度：{data['wendu']}度\n")
        dataArray.append(f"温度：{day_dict['high']} {day_dict['low']}\n")
        dataArray.append(f"风向：{day_dict['fengxiang']}\n")
        dataArray.append(f"天气：{day_dict['type']}\n")
        if index == 0:
            dataArray.append(f"贴士：{data['ganmao']}\n")
        dataArray.append(f"\n")
    print(''.join(dataArray))

if __name__ == "__main__":
    city = readCity()
    filename = 'city_code.txt'
    if os.path.exists(filename):
        city_json = readFile(filename)
        bj_json = query_weather(city_json['北京'])
        formatWeather(bj_json)
    else:
        writeToFile(filename, cityToId(city))