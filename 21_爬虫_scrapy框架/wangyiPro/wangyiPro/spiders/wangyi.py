import scrapy
from selenium import webdriver


class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']

    models_urls = []  # 存储五个板块对应详情页的url

    # 实例化一个浏览器对象
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='./chromedriver.exe')

    # 解析五大板块对应详情页的url
    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[3]/div[2]/div[2]/div/ul')
        alist = [3, 4, 6, 7, 8]

        for index in alist:
            # 国内/国际/.. 板块url
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

        # 依次对每一个板块对应的页面进行请求
        for url in self.models_urls:
            yield scrapy.Request(url, callback=self.parse_model)

    # 解析每一个板块页面中对应新闻的标题和新闻详情页的url
    def parse_model(self, response):
        pass
