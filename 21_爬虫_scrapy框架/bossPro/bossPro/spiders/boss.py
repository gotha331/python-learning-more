import scrapy
from bossPro.items import BossproItem


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101110100/?query=python']

    url = 'https://www.zhipin.com/c101110100/?query=python&page=%d'
    page_num = 2

    # 回调函数接收item
    def parse_detail(self, response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        item['job_desc'] = job_desc
        print(job_desc)

        yield item

    # 解析首页中的岗位名称
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')

        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('.//span[@class="job-name"]/a/text()').extract_first()
            item['job_name'] = job_name
            print(job_name)
            detail_url = 'https://www.zhipin.com' + li.xpath('.//span[@class="job-name"]/a/@href').extract_first()

            # 对详情页发请求，获取详情页的页面源码数据
            # 手动请求的发送

            # 请求传参：meta={},可以将meta字典传递给请求对应的回调函数
            yield scrapy.Request(url=detail_url, callback=self.parse_detail, meta={'item': item})

        # 分页操作
        if self.page_num <= 3:
            new_url = format(self.url % self.page_num)
            # print(new_url)
            self.page_num += 1

            yield scrapy.Request(new_url, callback=self.parse)
