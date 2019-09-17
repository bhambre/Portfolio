import scrapy
from golf.itemspgalinks import GolfItem

class GolfSpider(scrapy.Spider):
    name = "golf_pga_links"
    download_delay = 2
    allowed_domains = ["www.pgatour.com"]
    start_urls = [
    "https://www.pgatour.com/stats/categories.ROTT_INQ.html",
    "https://www.pgatour.com/stats/categories.RAPP_INQ.html",
    "https://www.pgatour.com/stats/categories.RARG_INQ.html",
    "https://www.pgatour.com/stats/categories.RPUT_INQ.html",
    "https://www.pgatour.com/stats/categories.RSCR_INQ.html",
    "https://www.pgatour.com/stats/categories.RSTR_INQ.html",
    "https://www.pgatour.com/stats/categories.RMNY_INQ.html",
    "https://www.pgatour.com/stats/categories.RPTS_INQ.html"
    ]

    def parse(self, response):

    	
        for sel in response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='section categories']/section/div[@class='clearfix']/div/div[@class='table-content clearfix']/ul/li"):
            
            item = GolfItem()

            item['link'] = "https://www.pgatour.com" + sel.xpath("a/@href").extract_first()
            
            yield item        




#response.xpath("//body[@class='sub-theme-fedexcup-playoffs body-pgatour-theme locale-en']/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/tbody/tr[@id='playerStatsRow28237']/td[@class='player-name']/a/text()").extract()[0]

#[@class='sub-theme-fedexcup-playoffs body-pgatour-theme locale-en']