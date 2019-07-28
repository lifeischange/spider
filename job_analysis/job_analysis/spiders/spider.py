# conding:utf-8
import scrapy
import re
from job_analysis.items import JobAnalysisItem

class  zhipinSpider(scrapy.Spider):
    name="toys"

    def start_requests(self):
        urls=['https://www.zhipin.com/']
        meta={"number":0,"start":1}        
        headers={'Connection':'close',"user-agent":"Mozilla/5.0(Windows NT 6.1;Win64;x64) AppleWebKit/537.36(KHTML,like Gecko) Chrome/74.0.3729.169 Safari/537.36"}
        for url in urls:
            yield scrapy.FormRequest(url=url,meta=meta,headers=headers,callback=self.parse)

    def parse(self,response):
        job_list=response.xpath('//div[@class="job-list"]/ul/li')
        for job in job_list:

            yield self.parse_item(job)
        next_link=response.xpath('//a[@ka="page-next" and @class!="next disabled"]/@href').extract()
        print("nextpageis**********************%s"%next_link)
        city_number=response.meta['number']
        print(response.meta['number'])
        if len(next_link)>0:
            url="https://www.zhipin.com"+next_link[0]
            yield scrapy.Request(url=url,callback=self.parse,meta=response.meta)
        else:
            for city in response.meta['citys']:
                url="https://www.zhipin.com/"+"?city="+city
                yield scrapy.Request(url=url,callback=self.parse,meta=response.meta)
            

    def parse_item(self,content):
        items=JobAnalysisItem()
        items['title']=content.xpath('.//div[@class="job-title"]/text()').extract()[0]
        items['salary']=content.xpath('.//div[@class="info-primary"]//span/text()').extract()[0]
        info1=content.xpath('//div[@class="info-primary"]/p/text()').extract()
        items['address']=info1[0]
        items['experiment']=info1[1]
        items['education']=info1[2]
        items['company']=content.xpath('.//div[@class="company-text"]/h3/a/text()').extract()[0]
        info2=content.xpath('.//div[@class="company-text"]/p/text()').extract()
        items['size']=info2[-1]
        items['industry']=info2[0]

        return items
