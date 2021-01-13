import requests

headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

urls = [
    'http://pic.netbian.com/uploads/allimg/210107/225154-1610031114a8ea.jpg',
    'http://pic.netbian.com/uploads/allimg/210107/214105-1610026865511a.jpg',
    'http://pic.netbian.com/uploads/allimg/200121/230803-1579619283a6c1.jpg'
]


def get_content(url):
    print('正在爬取:', url)
    # get方法是一个阻塞的方法
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        return response.content


def parse_content(content):
    print('响应数据的长度为：', len(content))


for url in urls:
    content = get_content(url)
    parse_content(content)
