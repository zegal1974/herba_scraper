
from urllib.parse import urljoin

from herba_scraper.scraper import Scraper


class JavhubScraper(Scraper):
    def __init__(self, url):
        super().__init__(url)

    def build_url(self, path_segments, page=1):
        if page > 1:
            path_segments.append(page)
        return urljoin(self.url_base, "/".join(str(s) for s in path_segments))

    def url_actor(self, sid=None, page=1):
        if sid is None:
            return self.build_url(["actresses"], page)
        return self.build_url(["star", sid], page)

    def url_director(self, sid=None, page=1):
        if sid is None:
            return self.build_url(["director"], page)
        return self.build_url(["director", sid], page)

    def url_publisher(self, sid=None, page=1):
        if sid is None:
            return self.build_url(["label"], page)
        return self.build_url(["label", sid], page)

    def url_producer(self, sid=None, page=1):
        if sid is None:
            return self.build_url(["studio"], page)
        return self.build_url(["studio", sid], page)

    def url_series(self, sid=None, page=1):
        if sid is None:
            return self.build_url(["series"], page)
        return self.build_url(["series", sid], page)

    def url_genre(self, sid=None, page=1):
        if sid is None:
            return self.build_url(["genre"], page)
        return self.build_url(["genre", sid], page)

    def url_movie(self, code):
        return f"{self.url_base}/{code}"

    def url_thumbnail(self, sid):
        return f"{self.url_base}/pics/thumb/{sid}.jpg"

    def url_cover(self, sid):
        return f"{self.url_base}/pics/cover/{sid}_b.jpg"
