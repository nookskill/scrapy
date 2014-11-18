import time
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from itunes.items import ItunesItem

class MySpider(CrawlSpider):
    name = "itunes"
    allowed_domains = ["apple.com"]

    start_urls = ["https://itunes.apple.com/th/genre/ios-games-action/id7001?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-adventure/id7002?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-arcade/id7003?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-board/id7004?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-card/id7005?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-casino/id7006?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-dice/id7007?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-educational/id7008?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-family/id7009?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-music/id7011?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-puzzle/id7012?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-racing/id7013?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-role-playing/id7014?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-simulation/id7015?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-sports/id7016?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-strategy/id7017?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-trivia/id7018?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-word/id7019?mt=8"

    ] 

    rules = (

        Rule (SgmlLinkExtractor(allow=("&letter=\S", ),restrict_xpaths=('//ul[@class="list alpha"]',))
    , callback="parse_items", follow= True),
        Rule (SgmlLinkExtractor(allow=("&page=\d+", ),restrict_xpaths=('//li/a[@class="paginate-more"]',))
    , callback="parse_items", follow= True),

            
    )


    def parse_items(self, response):
        
        titles = response.xpath("//div[@id='selectedcontent']/div/ul/li")
        items = []
        for titles in titles:
            item = ItunesItem()
            item ["title"] = titles.xpath('a/text()').extract()
            item ["category"] = response.xpath('//ul[@class="list breadcrumb"]/li[3]/a/text()').extract()
            item ["firstdate"] = ''+time.strftime("%x")
            item ["lastdate"] =  ''+time.strftime("%x")
            items.append(item)
        return(items)

'''
    start_urls = ["https://itunes.apple.com/th/genre/ios-games-action/id7001?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-adventure/id7002?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-arcade/id7003?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-board/id7004?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-card/id7005?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-casino/id7006?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-dice/id7007?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-educational/id7008?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-family/id7009?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-music/id7011?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-puzzle/id7012?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-racing/id7013?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-role-playing/id7014?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-simulation/id7015?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-sports/id7016?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-strategy/id7017?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-trivia/id7018?mt=8",
        "https://itunes.apple.com/th/genre/ios-games-word/id7019?mt=8"

    ]        
'''