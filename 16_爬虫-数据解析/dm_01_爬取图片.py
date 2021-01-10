import requests

if __name__ == "__main__":
    # 如何爬取图片数据

    url = "https://pic.qiushibaike.com/system/pictures/12396/123963888/medium/VN4QVFY3813OGYWO.jpg"

    # content(二进制)  text(字符串) json() (对象)
    img_data = requests.get(url=url).content

    with open('./qiutu.jpg', 'wb') as fp:
        fp.write(img_data)

    print("over !!!")

    # 数据解析原理概述：
    # - 解析的局部文本内容都会在标签之间或者标签对应的属性中进行存储
    # - 1.
    # 进行指定标签的定位
    # - 2.
    # 标签或者标签对应的属性中存储的数据值进行提取（解析）
