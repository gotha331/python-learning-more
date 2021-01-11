import requests
from lxml import etree
from CodeApi import base64_api

if __name__ == "__main__":
    # 封装识别验证码图片的函数
    def getCodeText(imgPath):
        img_path = imgPath
        result = base64_api(uname='shuaishuai', pwd='GUITAR@0314', img=img_path)
        print(result)


    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
    page_text = requests.get(url=url, headers=headers).text
    # 解析验证码图片img中src属性
    tree = etree.HTML(page_text)
    code_img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')[0]
    img_data = requests.get(url=code_img_src, headers=headers).content

    # 将验证码图片保存到本地
    with open('./code.jpg', 'wb') as fp:
        fp.write(img_data)

    # 调用图鉴平台示例程序进行验证码图片数据识别
    getCodeText('./code.jpg')
