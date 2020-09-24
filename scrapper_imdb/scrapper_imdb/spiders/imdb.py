import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapper_imdb.items import ScrapperImdbItem


class ImdbSpider(CrawlSpider):
    ''' Get informations about films sorted by IMDb Rating Descending) '''
    name = 'imdb'
    allowed_domains = ['www.imdb.com']

    def start_requests(self):
        yield scrapy.Request(url='https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc')

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//h3[@class='lister-item-header']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//a[@class='lister-page-next next-page'])[2]"))
    )

    def parse_item(self, response):
        item = ScrapperImdbItem()

        item["Title"] = response.xpath("normalize-space(//div[@class='title_wrapper']/h1/text()[1])").get()
        item["Year"] = response.xpath("//span[@id='titleYear']/a/text()").get()
        item["Rating_value"] = response.xpath("//span[@itemprop='ratingValue']/text()").get()
        item["Rating_count"] = response.xpath("normalize-space(//span[@itemprop='ratingCount']/text())").get()
        item["Description"] = response.xpath('normalize-space(//*[@id="title-overview-widget"]/div[2]/div[1]/div[1]/div/div[1]/div/div/text())').get()
        item["Director"] = response.xpath("(//div[@class='credit_summary_item'])[1]/a/text()").get()
        item["Duration"] = response.xpath("normalize-space(//div[@class='txt-block']/time/text())").get()
        item["Genre"] = response.xpath("(//div[@class='subtext']/a)[1]/text()").get()
        item["Country"] = response.xpath('//*[@id="titleDetails"]/div[2]/a/text()').get()
        item["Language"] = response.xpath('//*[@id="titleDetails"]/div[3]/a/text()').get()
        item["Budget"] = response.xpath("(//div[@class='txt-block'])[14]/text()[2]").get()
        item["Box_office_USA"] = response.xpath('normalize-space(//*[@id="titleDetails"]/div[8]/text()[2])').get()
        item["Box_office_world"] = response.xpath("normalize-space((//div[@class='txt-block'])[17]/text()[2])").get()
        item['Url'] = response.url

        return item
        #
        # yield {
        #     "Title": response.xpath("normalize-space(//div[@class='title_wrapper']/h1/text()[1])").get(),
        #     "Year": response.xpath("//span[@id='titleYear']/a/text()").get(),
        #     "Rating value": response.xpath("//span[@itemprop='ratingValue']/text()").get(),
        #     "Rating count": response.xpath("normalize-space(//span[@itemprop='ratingCount']/text())").get(),
        #     "Description": response.xpath("normalize-space(//div[@class='ipc-html-content ipc-html-content--base']/div/text())").get(),
        #     "Director": response.xpath("(//div[@class='credit_summary_item'])[1]/a/text()").get(),
        #     "Duration": response.xpath("normalize-space(//div[@class='txt-block']/time/text())").get(),
        #     "Genre": response.xpath("(//div[@class='subtext']/a)[1]/text()").get(),
        #     "Movies production company": response.xpath("(//div[@class='txt-block']/a)[9]/text()").get(),
        #     "Language": response.xpath("(//div[@class='txt-block']/a)[7]/text()").get(),
        #     "Budget": response.xpath("(//div[@class='txt-block'])[14]/text()[2]").get(),
        #     "Box office USA": response.xpath("normalize-space((//div[@class='txt-block'])[16]/text()[2])").get(),
        #     "Box office world": response.xpath("normalize-space((//div[@class='txt-block'])[17]/text()[2])").get(),
        #     'Url': response.url
        # }
