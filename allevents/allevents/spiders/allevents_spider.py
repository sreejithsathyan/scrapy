# -*- coding: utf-8 -*-
import scrapy
#from scrapy.spider import BaseSpider
#from scrapy.selector import HtmlXPathSelector
#from scrapy.selector import selector
from scrapy.http import Request


class AlleventsSpiderSpider(scrapy.Spider):
    name = 'allevents_spider'
    allowed_domains = ['https://allevents.in']
    #start_urls = list1
    start_urls = ['https://allevents.in/new%20delhi/all#']

    def parse(self, response):
        links = []
        print links
        for link in set(response.xpath('//a/@href').extract()):
            if len(link) > 1:
                if link.startswith("https://allevents.in/new%20delhi/"):
                    links.append(link)
                    print link
        for link in links:
            yield scrapy.Request(link,callback=self.parse_following_urls,dont_filter=True)

    def parse_following_urls(self,response):
        title = response.xpath('//h1[@class="overlay-h1"]//text()').extract()
	#print title
        time = response.xpath('//ul[@class="meta-list"]//text()').extract()[2].split('\t')[12]
	#print time
        address = response.xpath('//ul[@class="meta-list"]//text()').extract()[33].split('\t')[6]
	#print address
        organizer = response.xpath('//ul[@class="meta-list"]//text()').extract()[40]
	#print organizer
        followers = response.xpath('//div[@class="detail"]//text()').extract()[3]
	#print folowers_count
        event = response.xpath('//div[@class="detail"]//text()').extract()[10]
	#print event_count
        description = response.xpath('//div[@property="schema:description"]//text()').extract_first().lstrip()
	#print description
	#Give the extracted content row wise
        output = {
			"Title":title,
			"Time":time,
			"Address":address,
			"Organizer" :organizer,
			"followers_count" :followers,
			"event_count" :event,
			"description" :description
		}
	yield output
