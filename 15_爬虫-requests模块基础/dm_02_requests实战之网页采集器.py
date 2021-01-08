# 反爬机制之 UA伪装
# UA: User-Agent(请求载体的身份标识)
# UA检测： 门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，说明该请求是正常请求
# 如果检测到请求的载体身份标识不是基于某一款浏览器，则表示该请求为不正常请求（爬虫），则服务器端很可能拒绝该请求

# UA伪装：让爬虫对应的请求载体身份标识伪装成某一浏览器
import requests

if __name__ == '__main__':
    # UA伪装：将对应的User-Agent伪装到一个字典中
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    # 1.指定url
    url = "https://www.sogou.com/web"
    # 处理url携带的参数：封装到字典中
    kw = input("enter a world:")
    param = {
        'query': kw
    }

    # 2.对指定的url发起的请求对应的url是携带参数的，并且请求过程中处理的参数
    response = requests.get(url=url, params=param, headers=headers)
    # 3.获取响应数据
    page_text = response.text

    fileName = kw + '.html'

    # 4.持久化存储
    with open(fileName, 'w', encoding="utf-8") as fp:
        fp.write(page_text)
        fp.close()

    print(fileName, "保存成功")
