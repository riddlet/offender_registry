import scrapy
from offender_registry.items import OffenderRegistryItem
import re

class offender_spider(scrapy.Spider):
    name = "maryland"
    allowed_domains = ["www.dpscs.state.md.us"]
    start_urls = [
        "http://www.dpscs.state.md.us/sorSearch/search.do?anchor=offlist&searchType=byName&coords=0%2B0&streetAddress=&radius=0.25&firstnm=&lastnm=&county=Allegany&zip=&filter=ALL&category=ALL&start=211"
        ]

    def parse(self, response):
        for href in response.xpath("//*[@id='results_tab-List']//div[5]/a[1]/@href"):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_dir_contents)
        
    def parse_dir_contents(self, response):
        item = OffenderRegistryItem()
        id_prog = re.compile('id=([0-9]+)')
        id_url = response.url
        item['id_num'] = id_prog.findall(id_url)
        item['name'] = response.xpath('//*[@id="Column800"]/div/div/div[4]/text()').extract() #strip whitespace in pipeline
        item['aliases'] = response.xpath('//*[@id="top_info_container"]/div[4]/text()').extract() #replace unicode char in pipeline
        item['primary_residence'] = response.xpath('//*[@id="top_info_container"]/ul/li[1]/text()').extract() #strip whitespace in pipeline
        item['address_change_date'] = response.xpath('//*[@id="top_info_container"]/ul/li[2]/span[2]/text()').extract()
        item['temp_residence'] = response.xpath('//*[@id="top_info_container"]/ul/li[3]/span[2]/text()').extract()
        item['employ_address'] = response.xpath('//*[@id="top_info_container"]/ul/li[4]/span[2]/text()').extract() #sometimes >1
        item['school_address'] = response.xpath('//*[@id="top_info_container"]/ul/li[5]/span[2]/text()').extract()
        item['convict_date'] = response.xpath('//*[@id="Column800"]/div/div//ul//text()').extract() #text based retrieval
        item['convict_location'] = response.xpath('//*[@id="Column800"]/div/div//ul//text()').extract() #text based retrieval
        item['registr_authority'] = response.xpath('//*[@id="Column800"]/div/div//ul//text()').extract() #text based retrieval
        item['charges'] = response.xpath('//*[@id="Column800"]/div/div//ul//text()').extract() #sometimes >1 and different formats 
        item['charge_details'] = response.xpath('//*[@id="Column800"]/div/div//span[@class="charge_description"]//text()').extract() #join all elements in pipeline
        item['custody_info'] = response.xpath('//*[@id="Column800"]/div/div//text()').extract() #text based retrieval
        item['custody_agency'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract() #strip whitespace in pipeline
        item['registr_status'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract() #strip whitespace in pipeline
        item['tier'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['reg_term'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract() #strip whitespace in pipeline
        item['information_contact'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['current_reg_date'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract() #strip whitespace in pipeline
        item['sex'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['DOB'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['curr_age'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['height'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['weight'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['race'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['skin_tone'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['eye_color'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['hair_color'] = response.xpath('//*[@id="Column800"]/div/div//li//text()').extract()
        item['vehicles'] = response.xpath('//*[@id="Column800"]/div//text()').extract()
        item['image_urls'] = response.xpath('//*[@id="reg_pic_big"]/img/@src').extract()
        yield item
