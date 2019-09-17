import scrapy
from golf.itemspga import GolfItem
import pandas as pd

statlistpd = pd.read_csv("pgalinks2.csv")

statlist = list(statlistpd['current'])

class GolfSpider(scrapy.Spider):
    name = "golf_pga"
    download_delay = 0.5
    allowed_domains = ["www.pgatour.com"]
    start_urls = statlist


    def parse(self, response):

        date = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='header']/p/strong/text()").extract()[0]

    	header = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='header']/h1/text()").extract()[0]

        if response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[4]/text()"):

            column4 = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[4]/text()").extract()[0]

        if response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[5]/text()"):	
    	
    	   column5 = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[5]/text()").extract()[0]

        if response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[6]/text()"):

            column6 = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[6]/text()").extract()[0]

        if response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[7]/text()"):

            column7 = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[7]/text()").extract()[0]

        if response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[8]/text()"):

            column8 = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[8]/text()").extract()[0]

        if response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[9]/text()"):

            column9 = response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/thead/tr/th[9]/text()").extract()[0]
    	
        for sel in response.xpath("//body/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/tbody/tr"):

            item = GolfItem()

            playername = sel.xpath("td[@class='player-name']/a/text()").extract()[0]

            if sel.xpath("td[4]/text()"):

                item['PlayerName'] = playername
                item['Statistic'] = header
                item['Variable'] = header + ' - ' + '(' + column4 + ')' 
                item['Value'] = sel.xpath("td[4]/text()").extract()[0]
                item['Date'] = date

                yield item

            if sel.xpath("td[5]/text()"):

                item['PlayerName'] = playername
                item['Statistic'] = header
                item['Variable'] = header + ' - ' + '(' + column5 + ')' 
                item['Value'] = sel.xpath("td[5]/text()").extract()[0]
                item['Date'] = date

                yield item

            if sel.xpath("td[6]/text()"):

                item['PlayerName'] = playername
                item['Statistic'] = header
                item['Variable'] = header + ' - ' + '(' + column6 + ')' 
                item['Value'] = sel.xpath("td[6]/text()").extract()[0]
                item['Date'] = date

                yield item

            if sel.xpath("td[7]/text()"):   

                item['PlayerName'] = playername
                item['Statistic'] = header
                item['Variable'] = header + ' - ' + '(' + column7 + ')' 
                item['Value'] = sel.xpath("td[7]/text()").extract()[0]
                item['Date'] = date

                yield item

            if sel.xpath("td[8]/text()"):      

                item['PlayerName'] = playername
                item['Statistic'] = header
                item['Variable'] = header + ' - ' + '(' + column8 + ')' 
                item['Value'] = sel.xpath("td[8]/text()").extract()[0]
                item['Date'] = date

                yield item

            if sel.xpath("td[9]/text()"):     

                item['PlayerName'] = sel.xpath("td[@class='player-name']/a/text()").extract()[0]
                item['Statistic'] = header
                item['Variable'] = header + ' - ' + '(' + column9 + ')' 
                item['Value'] = sel.xpath("td[9]/text()").extract()[0]
                item['Date'] = date

                yield item          




#response.xpath("//body[@class='sub-theme-fedexcup-playoffs body-pgatour-theme locale-en']/div[@class='wrap']/div[@class='container']/div[@class='page-container']/div[@class='parsys mainParsys']/div[@class='details section']/section[@class='module-statistics-off-the-tee-details ']/div[@class='main-content-off-the-tee-details']/div[@class='details-table-wrap']/table[@id='statsTable']/tbody/tr[@id='playerStatsRow28237']/td[@class='player-name']/a/text()").extract()[0]

#[@class='sub-theme-fedexcup-playoffs body-pgatour-theme locale-en']



#response.xpath("//body/div[@class='container-fluid mt-4 maxWidth']/div[@class='row'][2]/div[@class='col-lg-7']/div[@class='shadow p-3 mb-5 bg-white rounded']/div/table[@class='table table-hover table-borderless table-sm']/tbody/tr[1]/td[2]/a/text()").extract()[0]

