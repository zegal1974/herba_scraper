from bs4 import BeautifulSoup
import requests
import re

class Jackett:
    def __init__(self, url, apikey):
        self.url = url
        self.apikey = apikey

    def search(self, query):
        params = {"apikey": self.apikey, "t": "search", "q": query}
        response = requests.get(self.url, params=params)
        self.parse(response.content)

    def parse(self, content):
        soup = BeautifulSoup(content, 'html.parser')

        items = soup.find_all('item')

        def get_info(item):
            title = item.find('title').text
            link = item.find('link').text
            content = item.find('comments').text
            size = item.find('size').text
            return {"title": title, "link": link, "content": content, "size": size}

        return [get_info(item) for item in items]
