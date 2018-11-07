from lxml import html
import requests
import time

class URLCrawler:

    def __init__(self, starting_url, depth):
        self.starting_url = starting_url
        self.depth = depth
        self.current_depth = 0
        self.depth_links = []
        self.urls = []

    def crawl(self):
        sniper = self.get_link(self.starting_url)
        self.urls.append(sniper)
        self.depth_links.append(sniper.links)

        while self.current_depth < self.depth:
            current_links = []
            for link in self.depth_links[self.current_depth]:
                current_url = self.get_link(link)
                current_links.extend(current_url.links)
                self.urls.append(current_url)
                time.sleep(5)

            self.current_depth += 1
            self.depth_links.append(current_links)

        return self.urls 


    def get_link(self, link):
        start_page = requests.get(link)
        tree = html.fromstring(start_page.text)
        
        url = tree.xpath('//h1[@itemprop="name"]/text()')[0]
        
        return url

crawler = URLCrawler('https://127.0.0.1', 2)
crawler.crawl()