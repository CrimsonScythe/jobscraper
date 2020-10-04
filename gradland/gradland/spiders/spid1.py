import scrapy
import pickle
import requests

class GradSpider(scrapy.Spider):

    with open('C:\\Users\hasee\\jobscraper\\listings.pkl', 'rb') as f:
        newlst = pickle.load(f)

    print(len(newlst))

    keywords = ['limit', 'search']
    translst = [item for item in newlst if ('limit' not in item and 'search' not in item)]

    final_lst = list(set(translst))

    print(len(final_lst))

    name = "quotes"
    i=len(final_lst)
    ls = []
    def start_requests(self):
        urls = self.final_lst

        for url in urls:
            self.i-=1
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.body
        self.ls.append([page])

        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
            # f.write(response.body)
        # self.log('Saved file %s' % filename)
        
        if (self.i <= 2):
            with open('responses.pkl', 'wb') as f:
                pickle.dump(self.ls, f)