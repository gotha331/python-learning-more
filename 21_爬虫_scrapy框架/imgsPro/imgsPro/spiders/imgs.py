import scrapy
from imgsPro.items import ImgsproItem


class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')

        for div in div_list:
            # 注意：页面设置了图片懒加载，使用伪属性src2获取图片src
            src = div.xpath('./div/a/img/@src2').extract_first()

            print(src)

            item = ImgsproItem()
            item['src'] = src

            # 提交item到管道
            yield item
