# post请求(携带了参数)
# 响应数据是一组json数据
import requests
import json

if __name__ == '__main__':
    # 1.指定url
    post_url = "https://fanyi.baidu.com/sug"
    # 2.UA伪装：将对应的User-Agent伪装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    # 3.post请求处理
    word = input("enter a word:")
    data = {
        "kw": word
    }
    fileName = word + '.json'
    # 4.发送请求
    response = requests.post(url=post_url, data=data, headers=headers)
    # 5.获取响应数据:json方法返回的是object（如果确认响应数据为json类型，才可使用json()）
    dic_obj = response.json()

    print(dic_obj)
    # 6.持久化存储
    fp = open(fileName, 'w', encoding="utf-8")
    json.dump(dic_obj, fp=fp, ensure_ascii=False)
