import scrapy
from crawler.items import Hotdeal
from datetime import datetime

# 참고코드 출처 : https://uslifelog.tistory.com/45
# class APT2U_Spider(scrapy.Spider):
#     name = "APT2U"  #spider 이름
#     allowed_domains = ["www.apt2you.com"]   #크롤링할 최상위 도메인
#     start_urls = ["http://www.apt2you.com/houseSaleSimpleInfo.do"]  #실제 크롤링할 주소
     
#     def parse(self, response):
#         hxs = Selector(response)    #지정된 주소에서 전체 소스코드를 가져옴
#         selects =[] #전체 소스코드 중에서 필요한 영역만 잘라내서 담을 리스트
#         selects = hxs.xpath('//tbody[@class="line"]/tr')    #필요한 영역을 잘라서 리스트에 저장
#         items = [] #데이터를 Item별로 구별해서 담을 리스트
#         for sel in selects:
#             item = APT2UItem() #item 객체 선언 
#             item['aptname'] = sel.xpath('th[@scope="row"]/a[@href="#none"]/text()').extract() #주택명 추출
#             item['link'] = sel.xpath('th[@scope="row"]/a/@onclick').re('\d+') #링크 추출
#             item['link'][0] = "http://www.apt2you.com/houseSaleDetailInfo.do?manageNo="+item['link'][0] #전체링크주소구성
#             item['company'] = sel.xpath('td[1]/text()').extract() #건설업체 추출
#             item['receiptdate'] = sel.xpath('normalize-space(td[2]/text())').extract() #청약기간 추출
#             item['result_date'] = sel.xpath('td[@class="end"]/text()').extract() #당첨자발표일 추출
#             items.append(item) #Item 1개 세트를 리스트에 담음
#         return items

class ClienSpider(scrapy.Spider):
    name = "clien"

    def start_requests(self):
        urls = [
            'https://www.clien.net/service/board/jirum',
        ]
        # https://www.clien.net/service/board/jirum?&od=T31&po=0
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        titles = response.xpath('//*[@id="div_content"]/div[10]/div/div/div/span/a[1]/text()').extract()
        links = response.xpath('//*[@id="div_content"]/div[10]/div/div/div/span/a[1]/@href').extract()
        # comments_links = response.xpath('//*[@id="div_content"]/div[10]/div/div/div/span/a[2]/@href').extract()
        times = response.xpath('//*[@id="div_content"]/div[10]/div/div/div/span/span/text()').extract()

        print("크롤링")
        print(titles)
        print(times)
        print(links)
        new_items = []
        for item in zip(titles, links, times):
            scraped_info = {
                'title' : item[0].strip(),
                'link' : "https://www.clien.net"+item[1].strip(),
                'time' : item[2].strip(),
            }
            new_item = Hotdeal()
            new_item["title"] = item[0].strip()
            new_item["link"] = "https://www.clien.net"+item[1].strip()
            new_item["time"] = item[2].strip()
            new_items.append(new_item)
            print(new_item)
            yield new_item
        # print(new_items)
        # return new_items
        
        print("크롤링끝")
    


class PpomppuSpider(scrapy.Spider):
    name = "ppomppu"

    def start_requests(self):
        urls = [
            'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        titles = response.xpath('//*[@id="revolution_main_table"]//tr/td[4]/table//tr/td[2]/a/font/text()').extract()
        links = response.xpath('//*[@id="revolution_main_table"]//tr/td[4]/table//tr/td[2]/a/@href').extract()
        # comments_links = response.xpath('//*[@id="div_content"]/div[10]/div/div/div/span/a[2]/@href').extract()
        times = response.xpath('//*[@id="revolution_main_table"]//tr/td[5]/@title').extract()
        times = times[1:] # 뽐뿌게시판 공지사항 때문에 1칸씩 밀려서 시간 저장
        
        print("크롤링")
        print(titles)
        print(links)
        # print(comments_links)
        print(times)
        # 시간양식을 맞추기 위해서 데이터 수정
        # for item in zip(titles, links, times):
        #     print(item[0],item[1],"20"+item[2][:-3].replace(".","-",2))
        
        for item in zip(titles, links, times):
            scraped_info = {
                'title' : item[0].strip(),
                'link' : "http://www.ppomppu.co.kr/zboard/"+item[1].strip(),
                'time' : "20"+item[2][:-3].replace(".","-",2)+":00",
            }
            yield scraped_info
        
        print("크롤링끝")
    

class Ppomppu4Spider(scrapy.Spider):
    name = "ppomppu4"
    def start_requests(self):
        urls = [
            'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu4',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        titles = response.xpath('//*[@id="revolution_main_table"]//tr/td[4]/table//tr/td[2]/a/font/text()').extract()
        links = response.xpath('//*[@id="revolution_main_table"]//tr/td[4]/table//tr/td[2]/a/@href').extract()
        # comments_links = response.xpath('//*[@id="div_content"]/div[10]/div/div/div/span/a[2]/@href').extract()
        times = response.xpath('//*[@id="revolution_main_table"]//tr/td[5]/@title').extract()
        times = times[1:] # 뽐뿌게시판 공지사항 때문에 1칸씩 밀려서 시간 저장
        
        print("크롤링")
        print(titles)
        print(links)
        # print(comments_links)
        print(times)
        # 시간양식을 맞추기 위해서 데이터 수정
        # for item in zip(titles, links, times):
        #     print(item[0],item[1],"20"+item[2][:-3].replace(".","-",2))
        
        for item in zip(titles, links, times):
            scraped_info = {
                'title' : item[0].strip(),
                'link' : "http://www.ppomppu.co.kr/zboard/"+item[1].strip(),
                'time' : "20"+item[2][:-3].replace(".","-",2)+":00",
            }
            yield scraped_info
        
        print("크롤링끝")


class RuliwebSpider(scrapy.Spider):
    name = "ruliweb"
    def start_requests(self):
        urls = [
            'https://bbs.ruliweb.com/market/board/1020',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #루리웹 크롤링하는 시간은 오늘 날짜가 나와있지 않기때문에 추가
        tday = str(datetime.today().strftime("%Y-%m-%d"))
        tday = tday+" "
        titles = response.xpath('//*[@id="board_list"]/div/div[2]/table/tbody/tr/td[3]/div/a/text()').extract()
        links = response.xpath('//*[@id="board_list"]/div/div[2]/table/tbody/tr/td[3]/div/a/@href').extract()
        times = response.xpath('//*[@id="board_list"]/div/div[2]/table/tbody/tr/td[7]/text()').extract()
        times = times[5:]# 루리웹에서는 상위 5개 항목이 고정적으로 있는 공지사항이기 때문에 6번째부터시작
        
        print("크롤링")
        print(titles)
        print(links)
        print(times)

        for item in zip(titles, links, times):
            if len(item[2].strip())>5:
                scraped_info = {
                    'title' : item[0].strip(),
                    'link' : item[1].strip(),
                    'time' : item[2].strip().replace(".","-",2)+" 00:00:00",
                }
            else:
                scraped_info = {
                    'title' : item[0].strip(),
                    'link' : item[1].strip(),
                    'time' : tday+item[2].strip()+":00",
                }
            yield scraped_info
        print("크롤링끝")


class QuasarzoneSpider(scrapy.Spider):
    name = "quasarzone"
    def start_requests(self):
        urls = [
            'https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #퀘이사존 크롤링하는 시간은 오늘 날짜가 나와있지 않기때문에 추가
        tday = str(datetime.today().strftime("%Y-%m-%d"))
        tday = tday+" "
        
        titles_candi = response.xpath('//*[@id="fboardlist"]/div[1]/ul/li[@class="list-item"]/div[3]/a[@class="item-subject"]/text()').extract()
        links = response.xpath('//*[@id="fboardlist"]/div[1]/ul/li[@class="list-item"]/div[3]/a[@class="item-subject"]/@href').extract()
        times = response.xpath('//*[@id="fboardlist"]/div[1]/ul/li[@class="list-item"]/div[3]/div/span[4]/span/text()').extract()

        #퀘이사존 데이터에 빈칸으로 입력된 것들이 있어서 제거
        titles = []
        for title in titles_candi:
            if title.strip():
                titles.append(title.strip())
        print("크롤링")
        print(titles)
        print(links)
        print(times)

        for item in zip(titles, links, times):
            scraped_info = {
                'title' : item[0],
                'link' : item[1].strip(),
                'time' : tday+item[2].strip()+":00",
            }
            yield scraped_info
        print("크롤링끝")
class CoolenjoySpider(scrapy.Spider):
    name = "coolenjoy"
    def start_requests(self):
        urls = [
            'http://www.coolenjoy.net/bbs/jirum',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        tday = str(datetime.today().strftime("%Y-%m-%d"))
        tday = tday+" "
        titles = response.xpath('//*[@id="fboardlist"]/div/table/tbody/tr/td[contains(@class,"td_subject")]/a/text()').extract()
        titles = map(lambda x: x.strip(), titles)
        titles = list(filter(lambda x: x!='',titles))
        links = response.xpath('//*[@id="fboardlist"]/div/table/tbody/tr/td[2]/a/@href').extract()
        times = response.xpath('//*[@id="fboardlist"]/div/table/tbody/tr/td[4]/text()').extract()   
        print("크롤링")
        print(titles)
        print(links)
        print(times)
        
        for item in zip(titles[1:], links[1:], times[1:]):
            if len(item[2].strip())>5:
                scraped_info = {
                    'title' : item[0].strip(),
                    'link' : item[1],
                    'time' : "20"+item[2].strip()+" 00:00:00",
                }
            else:
                scraped_info = {
                    'title' : item[0].strip(),
                    'link' : item[1],
                    'time' : tday+item[2].strip()+":00",
                }
            yield scraped_info
        print("크롤링끝")
    
