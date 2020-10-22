import scrapy
from bs4 import BeautifulSoup
from qunar.items import gongsiItem


class AaaSpider(scrapy.Spider):
    name = 'aaa'
    allowed_domains = ['nowcoder.com/intern/center']
    start_urls = ['https://nowcoder.com/intern/center/']

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html,"html5lib")
        ul_reco_job_list= soup.find('ul',class_="reco-job-list")
        item = gongsiItem()
        if ul_reco_job_list is not None:
            for div_gongsiItem in ul_reco_job_list.find_all('div'):
                if div_gongsiItem is not None:
                    ul = div_gongsiItem.find('ul')
                    if ul is not None:
                        for li_item in ul.find_all('li'):
                            if li_item is not None:
                                item['name'] =li_item.find('a').get_text()
                                item['url'] = li_item.find('a').get('href')
                                print(item)


