# -*- coding: utf-8 -*-
import scrapy

from allevents.items import AlleventsItem
class AlleventsSpiderSpider(scrapy.Spider):
    name = 'allevents_spider'
    allowed_domains = ['https://allevents.in']
    start_urls = ['https://allevents.in/new%20delhi/train-the-trainer-workshop/2044484635787135', 'https://allevents.in/new%20delhi/the-hashtag-fest/141862696561758', 'https://allevents.in/new%20delhi/run-for-laadli-a-unique-half-marathon-by-delhi-police/1775805199104598']

    def parse(self, response):
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
