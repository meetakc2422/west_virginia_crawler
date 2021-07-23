import scrapy
import csv
from scrapy.selector import  Selector
import time
from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
path = "E:\Desktop\west_Virginia\chromedriver.exe"
a_list = []
b_list = []
class WvSpider(scrapy.Spider):
    name = 'wv'
    # allowed_domains = ['https://www.wvlegislature.gov/bill_status/Bills_all_bills.cfm?year=2021']
    start_urls = ['https://www.google.com']

    def parse(self, response):
        try:
            driver = webdriver.Chrome(path, options=chrome_options)
            driver.get("https://www.wvlegislature.gov/bill_status/Bills_all_bills.cfm?year=2021&sessiontype=rs&btype=bill")
            sel = Selector(text=driver.page_source)
            bills = sel.xpath("//tr/td[@class='tdborder'][1]/a/@href").getall()
            for a in bills:
                a_list.append('https://www.wvlegislature.gov/bill_status/'+a)
            for b in a_list:
                driver.get(b)
                sel_1 = Selector(text=driver.page_source)
                pdf = sel_1.xpath('//div[@id="bhistcontent"]//tbody/tr[6]/td[2]/a[2]/@href').get()
                b_list.append("https://www.wvlegislature.gov"+pdf)

        # status = response.xpath("//tr/td[@class='tdborder'][3]/text()").getall()
            # doc_name = response.xpath("//tr/td[@class='tdborder'][2]/text()").getall()
            with open(R"E:\Desktop\west_Virginia\out_2.csv","w",newline="",encoding='utf8') as myfile:
                csv_wwriter = csv.writer(myfile,delimiter=",")
                # csv_wwriter.writerow(["Bill_no.","Status"])
                for i in b_list:
                    csv_wwriter.writerow([i])
            #     for c in zip(doc_name):
            #         csv_wwriter.writerow([c])
        #     myfile.close()
        except Exception as e:
            print(e)