import scrapy
import csv

class WvSpider(scrapy.Spider):
    name = 'wv'
    allowed_domains = ['https://www.wvlegislature.gov/bill_status/Bills_all_bills.cfm?year=2021']
    start_urls = ['https://www.wvlegislature.gov/bill_status/Bills_all_bills.cfm?year=2021&sessiontype=rs&btype=bill']

    def parse(self, response):
            # bills = response.xpath("//tr/td[@class='tdborder'][1]/a[@href]/text()").getall()
        # status = response.xpath("//tr/td[@class='tdborder'][3]/text()").getall()
        doc_name = response.xpath("//tr/td[@class='tdborder'][2]/text()").getall()
        with open(R"E:\Desktop\west_Virginia\output_1.csv","w",newline="",encoding='utf8') as myfile:
            csv_wwriter = csv.writer(myfile,delimiter=",")
            csv_wwriter.writerow(["Bill_no.","Status"])
            for c in zip(doc_name):
                csv_wwriter.writerow([c])
            myfile.close()
