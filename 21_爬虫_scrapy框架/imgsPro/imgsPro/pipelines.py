# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class ImgsproPipeline:
#     def process_item(self, item, spider):
#         return item
import scrapy
from scrapy.pipelines.images import ImagesPipeline


# ImagesPipeline专门用于文件下载的管道类，下载过程支持异步和多线程
class imgsPipeline(ImagesPipeline):
    # 对item中的图片进行请求操作
    def get_media_request(self, item, info):
        yield scrapy.Request(item['src'])

    # 定制图片的名称
    def file_path(self, request, response=None, info=None, *, item=None):
        url = request.url

        print(url)
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        return item  # 该返回值会传递给下一个即将被执行的管道类
