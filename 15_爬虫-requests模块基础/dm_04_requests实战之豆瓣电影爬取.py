import requests
import json

if __name__ == '__main__':
    url = "https://movie.douban.com/j/chart/top_list"
    params = {
        "type": 13,
        "interval_id": "100:90",
        "action": "",
        "start": 0,
        "limit": 20
    }

    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    response = requests.get(url=url, params=params, headers=headers)

    list_data = response.json()

    fp = open('./douban.json', 'w', encoding="utf-8")
    json.dump(list_data, fp=fp, ensure_ascii=False)

    print("over ！！！")
