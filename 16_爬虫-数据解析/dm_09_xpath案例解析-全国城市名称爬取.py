import requests
from lxml import etree

# 需求: 解析出所有城市名称 https://www.aqistudy.cn/historydata/
if __name__ == '__main__':
    # headers = {
    #     'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    # }

    # url = "https://www.aqistudy.cn/historydata/"
    # page_text = requests.get(url=url, headers=headers).text
    #
    # tree = etree.HTML(page_text)
    # # 热门城市
    # hot_li_list = tree.xpath('//div[@class="hot"]/div[@class="bottom"]/ul/li')
    # hot_city_names = []
    # all_city_names = []
    # # 解析到了热门城市的城市名称
    # for li in hot_li_list:
    #     hot_city_name = li.xpath('./a/text()')[0]
    #     hot_city_names.append(hot_city_name)
    #
    # all_li_list = tree.xpath('//div[@class="all"]/div[@class="bottom"]/ul/div[2]/li')
    # # 解析到了所有城市的城市名称
    # for li in all_li_list:
    #     city_name = li.xpath('./a/text()')[0]
    #     all_city_names.append(city_name)
    # print(all_city_names, len(all_city_names))

    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    url = "https://www.aqistudy.cn/historydata/"
    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    # 解析到热门城市和所有城市对应的a标签
    # //div[@class="bottom"]/ul/li/a  热门城市a标签的层级关系
    # //div[@class="bottom"]/ul/div[2]/li/a  全部城市a标签的层级关系
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a | //div[@class="bottom"]/ul/div[2]/li/a')

    all_city_names = []
    for a in a_list:
        city_name = a.xpath('./text()')[0]
        all_city_names.append(city_name)

    print(all_city_names)
    print(len(all_city_names))
