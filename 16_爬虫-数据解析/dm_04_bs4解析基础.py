# bs4进行数据解析：
# 数据解析的原理：
#   1.标签定位
#   2.提取标签、标签属性中存储的数据值
# bs4数据解析的原理：
#   1.实例华一个BeautifulSoup对象，并且将页面源码数据加载到该对象中
#   2.通过调用BeautifulSoup对象中相关的属性或者方法进行标签定位和数据提取
# 环境安装
#   - pip install bs4
#   - pip install lxml
# 如何实例化BeautufulSoup对象：
#   - from bs4 import BeautifulSoup
#   - 对象的实例化
#       1.将本地的html文档中的数据加载到该对象中
#           fp = open('./test.html', 'r', encoding="utf-8")
#           soup = BeautifulSoup(fp, 'lxml')
#       2.将互联网上获取的页面源码加载到该对象中
#           page_text= response.text
#           soup = BeautifulSoup(page_text,'lxml)
#   - 提供的用于数据解析的方法和属性：
#       1. soup.tagName: 返回的是文档中第一次出现的tagName对应的标签
#       2. soup.find():
#           - find('tagName'):等同于soup.div
#           - 属性定位：
#               - soup.find('div', class_/id/attr="song")
#       3. soup.find_all('tagName'):返回符合要求的所有标签（列表）
#       4. select：
#           - select('某种选择器（id,class,标签...选择器）')，返回的是一个列表。
#           - 层级选择器:
#               - soup.select('.tang > ul > li > a'): > 表示的是一个层级
#               - soup.select('.tang > ul  a'): 空格表示的是多个层级
#   - 获取标签之间的文本数据
#       - soup.a.text/string/get_text()
#       - text/get_text() 可以获取某一哥标签中的所有文本内容
#       - string：只可以获取该标签下面直系的文本内容
#   - 获取标签中属性值

from bs4 import BeautifulSoup

if __name__ == "__main__":
    # 将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding="utf-8")
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.a)  # soup.tagName 返回的是html中第一次出现的tagName标签
    # print(soup.div)
    # find('tagName'):等同于soup.div
    # print(soup.find('div'))
    # print(soup.find('div', class_="song"))
    # print(soup.find_all('a'))
    # print(soup.select('.tang'))
    # print(soup.select('.tang > ul > li > a')[0])
    # print(soup.select('.tang > ul  a')[0])
    print(soup.select('.tang > ul  a')[0].text)
    print(soup.select('.tang > ul  a')[0].string)
    print(soup.select('.tang > ul  a')[0].get_text())

    print(soup.find('div', class_="song").text)
    print(soup.find('div', class_="song").get_text())
    print(soup.find('div', class_="song").string)
