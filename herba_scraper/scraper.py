# from urllib.parse import urljoin
from lxml import etree


class Scraper:
    def __init__(self, url_base):
        self.url_base = url_base
        self.ns = etree.FunctionNamespace(
            "http://www.w3.org/2005/xpath-functions")
        self.ns.prefix = "fn"
        self.add_function("match", self.match)
        self.add_function("get_id", self.get_id)
        self.add_function("substring-after", self.substring_after)

    def add_function(self, name, function):
        self.ns[name] = function

    def match(self, context, text, pattern):
        match = pattern.match(text)
        if match:
            return match.group(1).strip()
        else:
            return ""

    def get_id(self, context, link):
        print(link)
        if link is None:
            return None
        if isinstance(link,  list):
            link = link[0]

        return link.split('/')[-1].split('.')[0]

    def substring_after(self, context, text, delimiter):
        return text.split(delimiter, 1)[1].strip()

    def parse_element(self, element, config):
        if 'fields' not in config:
            return None
        result = {}
        for field in config['fields']:
            if field['css'] is None or field['name'] is None:
                continue

            value = element.xpath(field['css'])
            if isinstance(value, list):
                result[field['name']] = value[0].strip()
            else:
                result[field['name']] = value.strip()

        return result
