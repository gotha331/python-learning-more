import requests
import json

if __name__ == '__main__':
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    cityName = input("请输入要查询的城市名称：")
    data = {
        "cname": cityName,
        "pid": "",
        "pageIndex": 1,
        "pageSize": 10,
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    fileName = 'kfc_' + cityName + '.json'

    response = requests.post(url=url, data=data, headers=headers)

    store_list = response.json()

    fp = open(fileName, 'w', encoding="utf-8")

    json.dump(store_list, fp=fp, ensure_ascii=False)

    print("over!!!")
