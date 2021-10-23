import scrapy

from ..items import ImbdItem
item = ImbdItem()


class ImbdxSpider(scrapy.Spider):
    name = 'imbdx'
    allowed_domains = ['https://www.imdb.com/chart/top']
    start_urls = ['http://www.imdb.com/chart/top']
    base_url = "https://www.imdb.com"

    def parse(self, response):

        print("-"*100)
        print(response.status)
        movie_name_list = response.xpath(
            ".//tbody[@class='lister-list']/tr/td[2]/a/text()").getall()  # to see movie name

        movie_link = response.xpath(
            ".//tbody[@class='lister-list']/tr/td[2]/a/@href").getall()

        for i in movie_link:
            movie_page = self.base_url + i
            print(movie_page)
            yield scrapy.Request(movie_page, callback=self.movie_details, dont_filter=1)
        print("-"*100)

    def movie_details(self, response):

        print(response.status)
        movie_name = response.xpath(".//h1/text()").get()
        # print(movie_name)

        info_data = [
            "Release date",
            "Country of origin",
            "Official sites",
            "Language",
            "Also known as",
            "Filming locations",
            "Production company"
        ]

    # checking if item maches our requirements
        data = response.xpath(
            ".//ul[@class= 'ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base']/li")
        all_data = []
        for i in data:
            info = i.xpath(".//text()").getall()
            all_data.append(info)
            # print(info)                             #uncomment to see what is done

        others = {}
        for i in all_data:
            if i[0] in info_data:
                print("{} -----> {}".format(i[0], i[1:]))

                others[i[0]] = i[1:]

                
                

                


    # finding plot:

        plot = response.xpath(
            "//div[@class='ipc-html-content ipc-html-content--base'][1]/div/text()").get()
        print("Plot ------>", plot)

    # time_stamp:
        time_stamp = response.xpath(
            ".//ul[@data-testid= 'hero-title-block__metadata']/li/text()")[-1].get()
        # print("Duration ----->",time_stamp)

    # ratings
        ratings = response.xpath(
            "//div[@data-testid='hero-rating-bar__aggregate-rating__score']/span/text()").get()
        # print("ratings ------> ",ratings)

    # all casts
        all_cast = {}
        casts = response.xpath(
            ".//div[@class ='StyledComponents__CastItemWrapper-y9ygcu-7 hTEaNu']")
        for i in casts:
            cast_name = i.xpath(".//div/a/text()").get()
            cast_role = i.xpath(".//span/text()").get()
            all_cast[cast_name] = cast_role
        # print(all_cast)

    # directors
        drwr = response.xpath(
            ".//ul[@class= 'ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt']/li")
        director = drwr[0].xpath(".//div/ul/li/a/text()").get()
        writer = drwr[1].xpath(".//div/ul/li/a/text()").getall()
        # print("director ----->",director)
        # print("writer----->",writer)

        print("-"*100)

        

        item["movie_name"] = movie_name
        item["ratings"] = ratings
        item["director"] = director
        item["others"] = others    
        item["duration"] = time_stamp
        item["plot"] = plot
        item["Playing_as"] = all_cast
        item["writer"] = writer
        yield item


