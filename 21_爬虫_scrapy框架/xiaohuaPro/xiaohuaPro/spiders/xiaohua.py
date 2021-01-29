import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xiaohuar.com/daxue/']

    # 生成一个通用url模板(不可变)
    url = 'http://www.xiaohuar.com/daxue/index_%d.html'
    page_num = 2

    def parse(self, response):
        div_list = response.xpath('//*[@id="wrap"]/div/div/div[@class="col-md-6 col-lg-3"]')
        for div in div_list:
            img_name = div.xpath('./div/div[1]/a/text()').extract_first()
            print(img_name)

        if self.page_num <= 18:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            # 手动请求发送:callback回调函数是专门用于数据解析
            yield scrapy.Request(url=new_url, callback=self.parse)
