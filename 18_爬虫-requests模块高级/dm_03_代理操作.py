import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
url = "https://www.baidu.com/s?wd=ip"

page_text = requests.get(url=url, headers=headers, proxies={"https": "https://222.162.5.102:9999"}).text

with open('ip.html', 'w', encoding="utf-8") as fp:
    fp.write(page_text)

print("over !!!")

# 反爬机制： 封ip
# 应对策略：反反爬机制 - 使用代理
