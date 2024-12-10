# from urllib.parse import urljoin
import re
import requests
from lxml import etree
from lxml.cssselect import CSSSelector

# class ScraperFunctions:
#     def filter(self, _, text, pattern):
#         regex = re.compile(pattern)
#         match = regex.search(text)
#         if match is None:
#             return None
#         return match.group(1).strip()

#     def get_id(self, _, link):
#         if link is None:
#             return None

#         return link.split('/')[-1].split('.')[0]

#     def substring_after(self, _, text, delimiter):
#         return text.split(delimiter, 1)[1].strip()


class Scraper:
    def __init__(self, url_base):
        self.url_base = url_base
        self.ns = etree.FunctionNamespace(
            "http://www.w3.org/2005/xpath-functions")
        self.ns.prefix = 'fn'
        # sfunctions = ScraperFunctions()
        # self.ns['filter'] = sfunctions.filter
        # self.ns['get_id'] = sfunctions.get_id
        # self.ns['substring-after'] = sfunctions.substring_after

        self.add_function("filter", self.filter)
        self.add_function("get_id", self.get_id)
        self.add_function("substring-after", self.substring_after)

    def add_function(self, name, function):
        self.ns[name] = function

    def filter(self, _, text, pattern):
        regex = re.compile(pattern)
        match = regex.match(text)
        if match:
            return match.group(1).strip()
        else:
            return ""

    def get_id(self, _, link):
        print(link)
        if link is None:
            return None
        if isinstance(link,  list):
            link = link[0]

        return link.split('/')[-1].split('.')[0]

    def substring_after(self, _, text, delimiter):
        return text.split(delimiter, 1)[1].strip()

    def parse_element(self, element, config):
        if 'fields' not in config:
            return None

        result = {}
        for field in config['fields']:
            if field['css'] is None or field['name'] is None:
                continue

            sel = CSSSelector(field['css'])
            value = sel(element)
            print(value)
            if value is None or len(value) == 0:
                continue

            if isinstance(value, list):
                result[field['name']] = value[0].strip()
            else:
                result[field['name']] = value.strip()

        return result

    def parse_tree(self, element, config):
        if 'css' not in config:
            return None

        children = element.cssselect(config['css'])
        if children is None or len(children) == 0:
            return None

        return [self.parse_element(child, config) for child in children].compact()

    def get(self, url, headers={}):
        respsonse = requests.get(url, headers=headers)
        if respsonse.status_code == 200:
            return respsonse.content
        else:
            # TODO: handle error
            return None

    def build_element(self, content):
        parser = etree.HTMLParser()
        return etree.fromstring(content, parser)
