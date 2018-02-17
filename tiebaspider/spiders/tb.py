# -*- coding: utf-8 -*-
import scrapy
import urllib
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tiebaspider.items import TiebaspiderItem


class TbSpider(CrawlSpider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = []

    # 获取贴吧名
    tieba_name = raw_input('请输入贴吧名：')
    tieba_name_encode = urllib.quote(tieba_name)
    url = 'https://tieba.baidu.com/f?kw=' + tieba_name
    start_urls.append(url)

    rules = (
        Rule(LinkExtractor(allow = r'tieba.baidu.com/f\?kw=' + tieba_name_encode + '&ie=utf-8&pn=\d+'), follow = True),
        Rule(LinkExtractor(allow = r'tieba.baidu.com/p/\d+'), callback='parse_item', follow = True),
        Rule(LinkExtractor(allow = r'tieba.baidu.com/p/\d+\?pn=\d+'), callback='parse_item', follow = True),
    )

    def parse_item(self, response):
        # 获取所有的图片url
        image_urls = response.xpath('//cc//img[@class="BDE_Image"]/@src').extract()

        for image_url in image_urls:
            item =  TiebaspiderItem()
            item['image_url'] = image_url

            yield item
