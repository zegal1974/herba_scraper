import requests

from lxml import etree


from urllib.parse import urljoin

from herba_scraper.scraper import Scraper

USER_AGENT_TEMPLATES = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
]

ACCEPT_LANGUAGE = 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
ACCEPT = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7'

HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47',
    "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    "Accept-Language": 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    "cookies": {'existmag': 'all'}
}

ACTORS_CSS = {
    'css': '.item a.avatar-box',
    'fields': [
        {'name': 'sid', 'css': 'fn:get_id(./@href)'},
        {'name': 'avatar', 'css': 'img/@src'},
        {'name': 'name', 'css': 'img/@title'}
    ]
}

ACTOR_CSS = {
    'fields': [
        {'name': 'avatar', 'css': '.avatar-box .photo-frame img/@src'},
        {'name': 'name',  'css': '.avatar-box .photo-info span/text()'},
        {'name': 'birthday',
            'css': '.avatar-box .photo-info p:regex("生日: ")', 'match': '([0-9-]+)'},
        {'name': 'age',
            'css': '.avatar-box .photo-info p:regex("年齡: ")', 'match': '([0-9]+)'},
        {'name': 'height',
            'css': '.avatar-box .photo-info p:regex("身高: ")', 'match': '([0-9]+)'},
        {'name': 'cups',
            'css': '.avatar-box .photo-info p:regex("罩杯: ")', 'match': '([A-Z])'},
        {'name': 'bust',
            'css': '.avatar-box .photo-info p:regex("胸圍: ")', 'match': '([0-9]+)'},
        {'name': 'waist',
            'css': '.avatar-box .photo-info p:regex("腰圍: ")', 'match': '([0-9]+)'},
        {'name': 'hip',
            'css': '.avatar-box .photo-info p:regex("臀圍: ")', 'match': '([0-9]+)'},
        {'name': 'homeland', 'css': '.avatar-box .photo-info p:regex("出生地: ")',
         'function': 'substring_after(:)'},
        {'name': 'hobiies', 'css': '.avatar-box .photo-info p:regex("愛好: ")',
         'function': 'substring_after(:)'},
        {'name': 'summary', 'css': 'a#resultshowall.mypointer',
            'match': '([0-9]+)'}
    ]
}

MOVIES_SUMMARY_CSS = {
    'fields': [
        {'name': 'summary', 'css': 'a#resultshowall.mypointer',
            'match': '([0-9]+)'}
    ]
}

MOVIES_CSS = {
    'css': '.item a.movie-box',
    'fields': [
        {'name': 'code', 'css': './@href', 'function': 'get_id()'},
        {'name': 'thumbnail', 'css': 'img/@src'},
        {'name': 'sid', 'css': 'img/@src', 'function': 'get_id()'},
        {'name': 'name', 'css': 'img/@title'},
        {'name': 'published_on', 'css': 'date:nth-of-type(2)/text()'}
    ]
}

MOVIE_CSS = {
    'fields': [
        {'name': 'cover', 'css': '.row.movie a[href]'},
        # {'name': 'cover', 'css': "//div[@class='row movie']//a/@href"},
        # {'name': 'sid',
        #     'css': "//div[@class='row movie']//a/@href"},
        # {'name': 'name', 'css': '//div[@class="row movie"]//a//img/@title'},
        # # { 'name': 'code', 'css': ' .row.movie p span:regex("識別碼:") ~ span/text()' },
        # {'name': 'published_on',
        #  'css': '//div[@class="row movie"]/div[2]/p/span[contains(text(),"發行日期:")]/../text()'},
        # {'name': 'length', 'css': '//div[@class="row movie"]/div[2]/p/span[contains(text(),"長度:")]/../text()',
        #  'match': '([0-9]+)'},
        # {'name': 'gid',
        #     'css': "script:regex('var gid = ')[fn:filter(., r'var gid = ([0-9]+)')]"}
    ]
}


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

    def fetch_actors(self, page=1):
        return self.fetch_items(self.url_actor(), ACTORS_CSS)

    def fetch_actor(self, sid, all=False):
        content = self.get(self.url_actor(sid))
        if content is None:
            return None

        root = etree.XML(content)
        actor, summary = self.extract_fields(root, ACTOR_CSS)

    def parse_actor(self, sid, root):
        adata = self.parse_element(root, ACTOR_CSS)
        adata['sid'] = sid

        mdata = self.parse_tree(root, MOVIES_CSS)

        return {'actor': adata, 'movies': mdata}

    def parse_movie(self, root):
        data = self.parse_element(root, MOVIE_CSS)

        return data
