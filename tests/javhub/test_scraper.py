
from herba_scraper.javhub.scraper import JavhubScraper


class TestJavHubScraper:
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
