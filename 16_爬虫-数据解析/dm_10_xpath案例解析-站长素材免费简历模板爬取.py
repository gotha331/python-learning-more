import requests
import os
from lxml import etree

# 需求：爬取站长素材中免费简历模板
if __name__ == "__main__":
    if not os.path.exists('./resumes'):
        os.mkdir('./resumes')

    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    }

    url = "https://aspx.sc.chinaz.com/query.aspx"
    for page in range(1, 3):
        params = {
            'keyword': '免费',
            'issale': '',
            'classID': 864,
            'page': page
        }
        page_text = requests.get(url=url, params=params, headers=headers).text
        tree = etree.HTML(page_text)

        resume_href_list = tree.xpath('//div[@id="container"]/div/a/@href')
        for resume_href in resume_href_list:
            resume_href = 'https:' + resume_href
            resume_details = requests.get(url=resume_href, headers=headers).text
            r_tree = etree.HTML(resume_details)
            down_url = r_tree.xpath('//div[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
            resume_data = requests.get(url=down_url, headers=headers).content
            resume_name = down_url.split('/')[-1]
            resume_path = './resumes/' + resume_name

            with open(resume_path, 'wb') as fp:
                fp.write(resume_data)
                print(resume_name, '写入成功！！！')

        print('第', page, '页写入完成！！！')

    print('over !!!')
