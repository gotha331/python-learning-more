import requests
import json

if __name__ == "__main__":
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    data = {
        "on": "true",
        "page": 1,
        "pageSize": 15,
        "productName": "",
        "conditionType": 1,
        "applyname": "",
        "applysn": ""
    }

    response = requests.post(url=url, data=data, headers=headers)

    eps_list = response.json()

    fp = open('./epsList.json', 'w', encoding="utf-8")

    json.dump(eps_list, fp=fp, ensure_ascii=False)

    print("over !!!")
