import requests
import json

if __name__ == "__main__":
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    # 批量获取不同企业的id值
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    id_list = []  # 存储企业的id
    xkzs_list = []  # 存储企业的许可证书

    for page in range(1, 6):
        data = {
            "on": "true",
            "page": 1,
            "pageSize": 15,
            "productName": "",
            "conditionType": 1,
            "applyname": "",
            "applysn": ""
        }

        json_ids = requests.post(url=url, data=data, headers=headers).json()

        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    # 获取许可证书详情的url
    url2 = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
    for id in id_list:
        data2 = {
            "id": id
        }

        xkzs_info = requests.post(url=url2, data=data2, headers=headers).json()
        xkzs_list.append(xkzs_info)

    fp = open('./xkzsList.json', 'w', encoding="utf-8")

    json.dump(xkzs_list, fp=fp, ensure_ascii=False)

    print("over !!!")
