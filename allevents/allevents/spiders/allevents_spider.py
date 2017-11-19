# -*- coding: utf-8 -*-
import scrapy

from allevents.items import AlleventsItem
class AlleventsSpiderSpider(scrapy.Spider):
    name = 'allevents_spider'
    allowed_domains = ['https://allevents.in']
    start_urls = ['https://allevents.in/new%20delhi/expressionism-art-workshop-2017/80006190664762','https://allevents.in/noida/carnival-de-cuisine/80001719226909']

    def parse(self, response):
        title = response.xpath('//h1[@class="overlay-h1"]//text()').extract()
	print title
	time = response.xpath('//ul[@class="meta-list"]//text()').extract()[2].split('\t')[12]
	print time
	address = response.xpath('//ul[@class="meta-list"]//text()').extract()[33].split('\t')[6]
	print address
	#Give the extracted content row wise
        output = {
			"title":title,
			"time":time,
			"address":address
		}
	yield output
