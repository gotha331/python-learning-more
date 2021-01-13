import requests
import random
import os
from lxml import etree
from multiprocessing.dummy import Pool

# 需求：爬取梨视频的视频数据
headers = {
    'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

if not os.path.exists('./pearVideo'):
    os.mkdir('./pearVideo')

# 原则：线程池处理的是阻塞且耗时的操作

# 对下述url发起请求解析出视频详情页的url和视频名称
url = "https://www.pearvideo.com/category_5"
page_text = requests.get(url=url, headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
urls = []

for li in li_list:
    detail_url = "https://www.pearvideo.com/" + li.xpath('./div/a/@href')[0]
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    video_id = detail_url.split('/')[-1].split('_')[-1]

    # 对详情页的url发起请求
    detail_page_text = requests.get(url=detail_url, headers=headers).text

    # 从详情页中解析出视频的地址（url）
    o_headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        'Referer': detail_url
    }
    get_video_url = "https://www.pearvideo.com/videoStatus.jsp"
    #
    params = {
        'contId': video_id,
        'mrd': random.random()
    }

    video_details = requests.get(url=get_video_url, params=params, headers=o_headers).json()
    video_url = video_details['videoInfo']['videos']['srcUrl']

    head_url = video_url.rsplit('/', 1)[0] + '/cont-'
    ass_url = video_id + '-' + video_url.rsplit('/', 1)[1].split('-', 1)[1]
    video_real_url = head_url + ass_url

    # print(video_real_url)
    dic = {
        'name': name,
        'url': video_real_url
    }

    urls.append(dic)


def get_video_data(dic):
    p_url = dic['url']
    print(dic['name'], '正在下载...')
    data = requests.get(url=p_url, headers=headers).content
    video_path = './pearVideo/' + dic['name']
    # 持久化存储操作
    with open(video_path, 'wb') as fp:
        fp.write(data)
        print(dic['name'], '下载成功')


# 使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video_data, urls)

pool.close()
pool.join()
