import requests
from lxml import etree

# 需求: 爬取58二手房中的房源信息
if __name__ == "__main__":
    # 爬取到页面源码数据
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    url = "https://xa.58.com/ershoufang/"
    page_text = requests.get(url=url, headers=headers).text

    # print(page_text)
    # 数据解析
    fp = open('./58.txt', 'w', encoding="utf-8")
    tree = etree.HTML(page_text)
    title_list = tree.xpath('//ul[@class="house-list-wrap"]//div[@class="list-info"]/h2/a/text()')

    for title in title_list:
        fp.write(title + '\n')

    fp.close()
    print('over!!!')
