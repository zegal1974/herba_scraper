from lxml import etree

from herba_scraper.scraper import Scraper


class TestScrapeFunctions:
    def setup_method(self):
        self.scraper = Scraper("https://example.com")

    def test_fitler(self):
        assert self.scraper.filter(None, "test 1", r"test (\d+)") == "1"

    def test_get_id_s(self):
        assert self.scraper.get_id(None, "https://example.com/id") == "id"
        assert self.scraper.get_id(
            None, "https://example.com/abc/def/id") == "id"
        assert self.scraper.get_id(None, "https://example.com/id.html") == "id"

    def test_substring_after_s(self):
        assert self.scraper.substring_after(
            None, 'header test', 'header') == 'test'


class TestScraperElementBase:
    def setup_method(self):
        self.scraper = Scraper("https://example.com")
        html = '<div><a href="http://example.com/id">Example</a></div>'
        root = etree.XML(html)
        self.doc = etree.ElementTree(root)
        self.config = {
            'fields': [
                {'name': 'title', 'css': 'a/text()'},
                {'name': 'url', 'css': 'a[href]'},
                {'name': 'id', 'css': 'fn:get_id(a[href])'}
            ]
        }

    def test_parse_element(self):
        result = self.scraper.parse_element(self.doc, self.config)
        assert result['title'] == 'Example'
        assert result['url'] == 'http://example.com/id'
        assert result['id'] == 'id'


class TestScraperElementClass:
    def setup_method(self):
        self.scraper = Scraper("https://example.com")
        html = '<div class="test"><a href="http://example.com/id">Example</a></div>'
        root = etree.XML(html)
        self.doc = etree.ElementTree(root)
        self.config = {
            'fields': [
                {'name': 'title', 'css': '.test a/text()'},
                {'name': 'url', 'css': 'a/@href'},
                {'name': 'id', 'css': 'fn:get_id(a/@href)'}
            ]
        }

    def test_parse_element(self):
        result = self.scraper.parse_element(self.doc, self.config)
        assert result['title'] == 'Example'
        assert result['url'] == 'http://example.com/id'
        assert result['id'] == 'id'


class TestScraperTree:
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
