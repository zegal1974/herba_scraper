from lxml import etree

from herba_scraper.scraper import Scraper


class TestScraper:

    def setup_method(self):
        self.scraper = Scraper("https://example.com")
        html = '<div><a href="http://example.com/id">Example</a></div>'
        root = etree.XML(html)
        self.doc = etree.ElementTree(root)
        self.config = {
            'fields': [
                {'name': 'title', 'css': 'a/text()'},
                {'name': 'url', 'css': 'a/@href'},
                {'name': 'id', 'css': 'fn:get_id(a/@href)'}
            ]
        }

    def test_parse_element(self):
        result = self.scraper.parse_element(self.doc, self.config)
        assert result['title'] == 'Example'
        assert result['url'] == 'http://example.com/id'
        assert result['id'] == 'id'

    # def test_substring_after(self):
    #     assert self.scraper.substring_after(
    #         self.html, 'http://example.com/') == 'id'
