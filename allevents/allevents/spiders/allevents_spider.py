# -*- coding: utf-8 -*-
import scrapy
from allevents.items import AlleventsItem
#from scrapy.selector import HtmlXpathSelector
#from scrapy.selector import selector
from scrapy.http import Request
"""import requests
response = requests.get("https://allevents.in/new%20delhi/all#")
page=response.content
def getURL(page):
    	start_link = page.find("a href")
    	if start_link == -1:
        	return None, 0
    	start_quote = page.find('"https://allevents.in/new%20delhi/', start_link)
    	end_quote = page.find('"', start_quote + 1)
    	url = page[start_quote + 1: end_quote]
    	return url, end_quote
list1=[]
while True:
    url, n = getURL(page)
    page = page[n:]
    if url != "https://allevents.in/new%20delhi/all":
	list1.append(url)
    else:
        break
#print len(list1)
#print list1[:]"""

class AlleventsSpiderSpider(scrapy.Spider):
    name = 'allevents_spider'
    allowed_domains = ['https://allevents.in']
    #start_urls = list1
    start_urls = ['https://allevents.in/new%20delhi/all#']

    def parse(self, response):
	
	for link in set(response.xpath('//a/@href').extract()):
            #item = Links()
            if len(link) > 1:
                if link.startswith("https://allevents.in/new%20delhi/"):
                    item = link
		    print item[:]


	"""item = []
        for link in set(response.xpath('//a/@href').extract()):
            #item = Links()
            if len(link) > 1:
                if link.startswith("https://allevents.in/new%20delhi/"):
                    
                    item = link
		    #print item[:]
		yield scrapy.Request(item,callback=self.parse_events)"""

    def parse_events(self,response):
	
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
