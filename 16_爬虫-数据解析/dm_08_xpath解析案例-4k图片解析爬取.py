import requests
from lxml import etree
import os

# 需求: 解析下载图片数据 http://pic.netbian.com/4kmeinv/

if __name__ == '__main__':
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }
    url = "http://pic.netbian.com/4kmeinv/"
    # page_text = requests.get(url=url, headers=headers).text
    # tree = etree.HTML(page_text)
    # img_src_list = tree.xpath('//div[@class="slist"]//img/@src')
    #
    # for img_src in img_src_list:
    #     img_src = 'http://pic.netbian.com/' + img_src
    #     img_data = requests.get(url=img_src, headers=headers).content
    #     img_name = img_src.split('/')[-1]
    #     img_path = './4kmeinv/' + img_name
    #
    #     with open(img_path, 'wb') as fp:
    #         fp.write(img_data)
    #         print(img_name, "下载成功！！")
    #
    # print('over !!!')

    # 数据解析：src的属性值 alt属性值
    # page_text = requests.get(url=url, headers=headers).text
    response = requests.get(url=url, headers=headers)
    # 手动设定响应数据的编码格式
    response.encoding = 'gbk'
    page_text = response.text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="slist"]/ul/li')

    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./4kmeinv'):
        os.mkdir('./4kmeinv')

    for li in li_list:
        img_src = "http://pic.netbian.com" + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        # 通用处理中文乱码的解决方案
        # img_name = img_name.encode('iso-8859-1').decode('gbk')
        # print(img_name, img_src)
        # 请求图片进行持久化存储
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = './4kmeinv/' + img_name

        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, "下载成功！！")

    print('over !!!')
