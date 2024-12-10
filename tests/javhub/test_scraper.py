from lxml import etree
from herba_scraper.javhub.scraper import JavhubScraper


class TestJavHubScraperBase:
    def setup_method(self):
        self.scraper = JavhubScraper("https://example.com")

    def test_build_url(self):
        assert self.scraper.build_url(
            ["search"]) == "https://example.com/search"
        assert self.scraper.build_url(
            ["search"], page=2) == "https://example.com/search/2"

    def test_url_actor(self):
        assert self.scraper.url_actor() == "https://example.com/actresses"
        assert self.scraper.url_actor(
            None, 2) == "https://example.com/actresses/2"
        assert self.scraper.url_actor('abc') == "https://example.com/star/abc"
        assert self.scraper.url_actor(
            'abc', 3) == "https://example.com/star/abc/3"

    def test_url_movie(self):
        assert self.scraper.url_movie(
            'ABC-123') == "https://example.com/ABC-123"


class TestJavHubScraperParse:
    def setup_method(self):
        self.scraper = JavhubScraper("https://example.com")

        file = open('tests/files/movie.html', 'r', encoding='utf-8')
        parser = etree.HTMLParser()
        self.root = etree.fromstring(file.read(), parser)
        # root = self.scraper.build_element(file.read())
        # self.doc = etree.ElementTree(root)

    def test_parse_movie(self):
        data = self.scraper.parse_movie(self.root)

        assert data['cover'] == '/pics/cover/9zf8_b.jpg'
        assert data['name'] == 'テニス終わりの汗だく若妻つむぎさんに密着誘惑で痴女られた昼下がり 明里つむぎ'
        # assert data['gid'] == '55976713876'
        pass
