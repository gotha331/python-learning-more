import requests
import re
import os

# 需求： 爬取糗事百科中热图板块下所有的热图图片
if __name__ == "__main__":
    # 创建一个文件夹，保存所有的图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')

    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    # 设置一个通用的url模版
    url = "https://www.qiushibaike.com/imgrank/page/%d/"

    # url = "https://www.qiushibaike.com/imgrank/"

    for pageNum in range(1, 3):
        # 对应页码的url
        new_url = format(url % pageNum)

        # 1.使用通用爬虫对URL对应的一整张页面进行爬取
        page_text = requests.get(url=new_url, headers=headers).text

        # 2.使用聚焦爬虫将页面中所有热图进行解析/提取
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)
        print(img_src_list)

        for src in img_src_list:
            # 拼接出一个完整的图片url
            src = "https:" + src
            # 请求到了图片的二进制数据
            img_data = requests.get(url=src, headers=headers).content

            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片存储的路径
            img_path = './qiutuLibs/' + img_name

            with open(img_path, 'wb') as fp:
                fp.write(img_data)
                print(img_name, "下载成功！！")

    print("over !!!")
