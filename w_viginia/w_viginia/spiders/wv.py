import scrapy
from scrapy.http import Request
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# path = "E:\Desktop\west_Virginia\chromedriver.exe"
class WvSpider(scrapy.Spider):
    name = 'wv'
    # allowed_domains = ['wvlegislature.gov']
    start_urls = ['https://www.wvlegislature.gov/bill_status/Bills_all_bills.cfm?year=2021&sessiontype=rs&btype=bill']

    def parse(self, response):
        bill = response.xpath('//table[@class="tabborder"]//tr[position() >1]/td[@class="tdborder"][1]/a/text()').extract()
        secondary_url = response.xpath('//table[@class="tabborder"]//tr[position() >1]/td[@class="tdborder"][1]/a/@href').extract()
        for url, c in zip(secondary_url,range(len(bill))):
                abs_url = 'https://www.wvlegislature.gov/bill_status/' + url
                yield Request(url=abs_url,callback=self.parse_more,meta={
                    'Bills':bill[c]
                    })
    def parse_more(self,response):
        doc_url = response.xpath('//div[@id="bhistcontent"]//tr[6]/td[2]/a[1]/@href').extract_first()
        ab_doc_url = "https://www.wvlegislature.gov/" + doc_url
        if 'Doc_Url' in response.meta:
            response.meta['Doc_Url'].append(ab_doc_url)
        else:
            response.meta['Doc_Url'] = ab_doc_url

        yield {'bills':response.meta['Bills'],
               'url':response.meta['Doc_Url'],
               }